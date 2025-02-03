import multiprocessing as mp
from pathlib import Path
from typing import Iterable

import geopandas as gp
import numpy as np
import ray
import shapely
from geopy.distance import geodesic
from shapely.strtree import STRtree

WGS84 = "epsg:4326"
MERCATOR = "epsg:3395"


def geodesic_distance(
    p1: shapely.Point,
    p2: shapely.Point,
    crs: str = WGS84,
) -> float:
    if None in (p1, p2):
        return np.nan
    
    if crs.lower != WGS84:
        p1, p2 = gp.GeoSeries([p1, p2], crs=crs).to_crs(WGS84)

    coords = [[*p.coords][0][::-1] for p in (p1, p2)]

    return geodesic(*coords).meters


class Coast:
    def __init__(
        self,
        source_dataset: Path | str | gp.GeoDataFrame,
        center_to_opposite_meridian: bool = False,
    ):
        if isinstance(source_dataset, (Path, str)):
            self.df = gp.read_file(source_dataset)
            self.df = self.df[["geometry"]].buffer(0).to_crs(WGS84)
        else:
            self.df = source_dataset

        if center_to_opposite_meridian:
            self.df = (
                gp.GeoDataFrame(
                    geometry=[
                        *self.df.geometry,
                        *self.df.geometry.translate(-360, 0),
                    ],
                    crs=WGS84,
                )
                .translate(180, 0)
                .intersection(shapely.box(-180, -90, 180, 90))
            )

        self.df_conformal = self.df.to_crs(MERCATOR)

        self.index = STRtree(self.df_conformal.geometry)
        _ = self.index.query(self.df_conformal.geometry[0])  # initialize index

    @property
    def conformal_boundary(self) -> gp.GeoSeries:
        return self.df_conformal.geometry.boundary

    def nearest_points(
        self,
        points: Iterable[shapely.Point],
        crs: str = WGS84,
    ) -> gp.GeoSeries:
        points = gp.GeoSeries(points, crs=crs)
        if crs.lower() != MERCATOR:
            points = points.to_crs(MERCATOR)

        i = self.index.nearest(points)
        coastlines = self.conformal_boundary[i]
        landmasses = self.df_conformal.geometry[i]

        coast_points = [
            None if l.contains(p) else c.interpolate(c.project(p))
            for p, c, l in zip(points, coastlines, landmasses)
        ]

        return gp.GeoSeries(coast_points, crs=MERCATOR).to_crs(crs)

    def distance(
        self,
        points: Iterable[shapely.Point],
        crs: str = WGS84,
    ) -> np.ndarray:
        points = gp.GeoSeries(points, crs=crs)
        if crs.lower() != WGS84:
            points = points.to_crs(WGS84)

        coast_points = self.nearest_points(points, crs)

        return np.array([
            geodesic_distance(p, c) for p, c in zip(points, coast_points)
        ])


@ray.remote
def calc_dist(
    coast: Coast,
    points: Iterable[shapely.Point],
    crs: str = WGS84,
) -> np.ndarray:
    return coast.distance(points, crs)


def distance_to_coast(
    x: np.ndarray,
    y: np.ndarray,
    coast_file_path: Path | str,
    n_workers: int = mp.cpu_count(),
) -> np.ndarray:
    ray.shutdown()
    ray.init(num_cpus=n_workers)
    batch_size = np.ceil(x.size / n_workers).astype(int)

    coast = Coast(coast_file_path, center_to_opposite_meridian=False)
    _coast = ray.put(coast)
    points = shapely.points(x, y).tolist()

    tasks = []
    while len(points) > 0:
        batch, points = points[:batch_size], points[batch_size:]
        tasks.append(calc_dist.remote(_coast, batch))

    distances = np.concatenate(ray.get(tasks))

    # repeat calculations with opposite central meridian
    x_shifted = x + 180
    x_shifted[x_shifted > 180] -= 360

    coast = Coast(coast.df.copy(), center_to_opposite_meridian=True)
    _coast = ray.put(coast)
    points = shapely.points(x_shifted, y)

    tasks = []
    while len(points) > 0:
        batch, points = points[:batch_size], points[batch_size:]
        tasks.append(calc_dist.remote(_coast, batch))

    distances_with_shift = np.concatenate(ray.get(tasks))

    return np.nanmin(
        [
            distances,
            distances_with_shift,
        ],
        axis=0,
    )


if __name__ == "__main__":
    from itertools import product

    import rasterio as rio
    from rasterio.enums import Resampling
    from rasterio.features import rasterize

    coast_file_path = "/data/work/oemc/task_5.5/GSHHS_shp/h/GSHHS_h_L1.shp"
    # coast_file_path = "/data/work/oemc/task_5.5/GSHHS_shp/c/GSHHS_c_L1.shp"

    grid_deg = 1
    x = np.arange(-180, 180, grid_deg) + grid_deg / 2
    y = np.arange(-90, 90, grid_deg) + grid_deg / 2
    w = x.size
    h = y.size

    x, y = np.array([*product(x, y)]).T

    print(f"computing distance to coast for {x.size} points")

    distance = distance_to_coast(x, y, coast_file_path, 8)

    points = shapely.points(x, y)
    transform = rio.Affine(grid_deg, 0, -180, 0, -grid_deg, 90)
    data = rasterize(
        zip(points, distance),
        out_shape=(h, w),
        transform=transform,
        dtype=np.float32,
    )

    out_file = f"biodiversity_data/coastdist_test_{grid_deg}°.tif"
    with rio.open(
        out_file,
        "w",
        width=w,
        height=h,
        dtype=np.float64,
        transform=transform,
        count=1,
        crs="epsg:4326",
        driver="GTiff",
        interleave="pixel",
        tiled=True,
        blockxsize=256,
        blockysize=256,
        compress="DEFLATE",
        nodata=-9999,
    ) as dst:
        dst.write(data.reshape(1, *data.shape))

    with rio.open(out_file, "r+") as dst:
        dst.build_overviews([2, 4, 8, 16], Resampling.average)
