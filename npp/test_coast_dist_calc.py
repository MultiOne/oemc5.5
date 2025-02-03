import pandas as pd
import geopandas as gp
from geopy.distance import geodesic
from shapely.strtree import STRtree
import shapely

df = pd.read_parquet("biodiversity_data/cafe_nearest_stats.parquet")

x = df.rarefyID_x
y = df.rarefyID_y

print(
    x.min(), x.max(),
    y.min(), y.max()
)


import numpy as np
x = np.arange(-180, 180, 2)
y = np.arange(-90, 90, 2)
w = x.size
h = y.size

from itertools import product

x, y = np.array([*product(x, y)]).T


points = shapely.points([*zip(x, y)])

pdf = gp.GeoDataFrame(geometry=points, crs="epsg:4326")

sdf = gp.read_file("/data/work/oemc/task_5.5/GSHHS_shp/h/GSHHS_h_L1.shp").buffer(0)

sdf_shift = gp.GeoDataFrame(geometry=[
    *sdf.geometry,
    *sdf.translate(-360, 0).geometry,
], crs="epsg:4326").translate(180)

sdf_shift = sdf_shift.buffer(0).intersection(shapely.box(-180, -90, 180, 90))

x_shift = x + 180
x_shift[x_shift > 180] -= 360
points_shift = shapely.points([*zip(x_shift, y)])

pdf_shift = gp.GeoDataFrame(geometry=points_shift, crs="epsg:4326")

pdf_merc = pdf.to_crs("epsg:3395")
pdf_shift_merc = pdf_shift.to_crs("epsg:3395")

sdf_merc = sdf.to_crs("epsg:3395")
sdf_shift_merc = sdf_shift.to_crs("epsg:3395")
coast_idx = STRtree(sdf_merc.geometry)
coast_shift_idx = STRtree(sdf_shift_merc.geometry)

coast_points = []
coast_points_shift = []
for i, (p, ps) in enumerate(zip(pdf_merc.geometry, pdf_shift_merc.geometry)):
    c = sdf_merc.geometry[coast_idx.nearest(p)]
    if p.intersects(c):
        coast_points.append(None)
        coast_points_shift.append(None)
        continue
    
    cb = c.boundary
    coast_points.append(cb.interpolate(cb.project(p)))

    c = sdf_shift_merc.geometry[coast_shift_idx.nearest(ps)]
    cb = c.boundary
    coast_points_shift.append(cb.interpolate(cb.project(ps)))

    if (i+1) % 1000 == 0:
        print(f"coast found for point {i+1} of {len(points)}")

coast_points = gp.GeoSeries(coast_points, crs="epsg:3395").to_crs("epsg:4326")
coast_points_shift = gp.GeoSeries(coast_points_shift, crs="epsg:3395").to_crs("epsg:4326")

dists = []
for i, (p, ps, cp, cps) in enumerate(zip(
        pdf.geometry,
        pdf_shift.geometry,
        coast_points,
        coast_points_shift,
)):
    if cp is None:
        dists.append(0)
        continue

    dists.append(min(
        geodesic([*p.coords][0][::-1], [*cp.coords][0][::-1]).meters,
        geodesic([*ps.coords][0][::-1], [*cps.coords][0][::-1]).meters,
    ))
    
    if (i+1) % 1000 == 0:
        print(f"coast dist calculated for point {i+1} of {len(points)}")

pdf["coast_dist"] = dists
pdf.to_file("biodiversity_data/points_dist.gpkg", driver="GPKG")

import rasterio as rio
from rasterio.features import rasterize
transform = rio.Affine(
    2, 0, -180,
    0, -2, 90,
)

data = rasterize(
    zip(points, dists),
    out_shape=(h, w),
    transform=transform,
    dtype=np.float64,
)

with rio.open(
        "biodiversity_data/coastdist_test.tif", "w",
        driver="GTiff",
        width=w,
        height=h,
        transform=transform,
        crs="epsg:4326",
        count=1,
        dtype=np.float64,
) as dst:
    dst.write(data.reshape(1, *data.shape))
