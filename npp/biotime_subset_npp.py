#%%
import rasterio.sample
import requests
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime
import gzip
import io
import pandas
import numpy as np
from netCDF4 import Dataset
from scipy.interpolate import RegularGridInterpolator
import rasterio

fn_input = Path(r'C:\DATA\OEMC\T5.5\Input\BIOTIME_subset.csv')
fn_input_new = Path(r'C:\DATA\OEMC\T5.5\Input\BIOTIME_NPP.csv')
fld_npp = Path(r'C:\DATA\OEMC\T5.5\NPP')
fld_out = fld_npp.parent/'NPP_out'
fn_bathy = fn_input.parent/'gebco_2023_sub_ice_topo_geotiff/gebco_2023_sub_ice_topo.vrt'
models = ['vgpm','cbpm','cafe']
sources = {'modis':[2002,2023], 'seawifs':[1997, 2009]}
interps = ['linear', 'nearest']

nlat = 2160
nlon = 4320
spacing = 1./12.
year_start = 1997
year_end = 2023


def ttprint(*args, **kwargs):
  """
  A print function that displays the date and time.
  """
  from datetime import datetime
  import sys

  print(f'[{datetime.now():%H:%M:%S}] ', end='')
  print(*args, **kwargs, flush=True)


def get_lat_lon_grid():
    # Grid is 2160x4320
    '''
    how do we convert rows and columns to lats and lons?
    The rows represent lines of latitude, and the columns coincide with longitude.

    For 1080 by 2160 data, the grid spacing is 1/6 of a degree in both latitude and longitude.

    1080 rows * 1/6 degree per row = 180 degrees of latitude (+90 to -90).
    2160 columns * 1/6 degree per column = 360 degrees of longitude (-180 to +180).

    The north west corner of the start of the hdf file is at +90 lat, -180 lon.

    To obtain the location of the center of any pixel:
    take the number of rows and columns you are away from the NW corner,
    multiply by the grid spacing to get the change in latitude and longitude,
    subtract the change in latitude from +90 lat,
    add the change in longitude to -180 lon;
    shift the latitude down (subtract) by 1/2 of a grid spacing
    and shift the longitude over (add) by 1/2 of a grid spacing
    '''
 
    rows = np.arange(nlat)
    cols = np.arange(nlon)

    lats = 90 - rows * spacing - spacing/2.0
    lons = -180 + cols * spacing + spacing/2.0

    return lats, lons

def extend_grid(data):
    '''
    Extends data grid so that every point can be interpolated
    '''
    dataext = np.full((nlat+2,nlon+2), fill_value=np.nan)
    dataext[1:-1,1:-1] = data

    # wrap around for lon
    dataext[:,0] = dataext[:,-2]
    dataext[:,-1] = dataext[:,1]

    # extend values for lat
    dataext[0,:] = dataext[1,:]
    dataext[-1,:] = dataext[-2,:]

    return dataext

#%%
# http://orca.science.oregonstate.edu/data/1x2/monthly/vgpm.r2022.m.chl.m.sst/hdf/vgpm.m.2002.tar
# http://orca.science.oregonstate.edu/data/2x4/monthly/vgpm.r2022.s.chl.a.sst/hdf/vgpm.s.2002.tar
# http://orca.science.oregonstate.edu/data/2x4/monthly/cbpm2.modis.r2022/hdf/cbpm.m.2002.tar
# http://orca.science.oregonstate.edu/data/2x4/monthly/cbpm2.seawifs.r2022/hdf/cbpm.s.2002.tar
# http://orca.science.oregonstate.edu/data/2x4/monthly/cafe.modis.r2022/hdf/cafe.m.2002.tar
# http://orca.science.oregonstate.edu/data/2x4/monthly/cafe.seawifs.r2022/hdf/cafe.s.2002.tar

# def download_npp_tar():

#     for model in models:
#         for year in range(1997, 2024):
#             for source in sources:
#                 if source=='seawifs':  #SeaWiFS
#                     if model=='vgpm':
#                         link = f'http://orca.science.oregonstate.edu/data/2x4/monthly/vgpm.r2022.s.chl.a.sst/hdf/vgpm.s.{year}.tar'
#                     elif model=='cbpm':
#                         link = f'http://orca.science.oregonstate.edu/data/2x4/monthly/cbpm2.seawifs.r2022/hdf/cbpm.s.{year}.tar'
#                     else: 
#                         link = f'http://orca.science.oregonstate.edu/data/2x4/monthly/cafe.seawifs.r2022/hdf/cafe.s.{year}.tar'
#                 else:            #MODIS
#                     if model=='vgpm':
#                         link = f'http://orca.science.oregonstate.edu/data/2x4/monthly/vgpm.r2022.m.chl.m.sst/hdf/vgpm.m.{year}.tar'
#                     elif model=='cbpm':
#                         link = f'http://orca.science.oregonstate.edu/data/2x4/monthly/cbpm2.modis.r2022/hdf/cbpm.m.{year}.tar'
#                     else:
#                         link = f'http://orca.science.oregonstate.edu/data/2x4/monthly/cafe.modis.r2022/hdf/cafe.m.{year}.tar'

#             fld_out = fld_npp/f''
                
#             response = requests.get(link)
#             if not response.ok:
#                 print(f'Cannot read ')

#%%
def download_npp():
    for model in models:
        for source in sources:
            print(source)
            if source == 'seawifs':
                if model=='vgpm':
                    link = f'http://orca.science.oregonstate.edu/data/2x4/monthly/vgpm.r2022.s.chl.a.sst/hdf/'
                elif model=='cbpm':
                    link = f'http://orca.science.oregonstate.edu/data/2x4/monthly/cbpm2.seawifs.r2022/hdf/'
                else: 
                    link = f'http://orca.science.oregonstate.edu/data/2x4/monthly/cafe.seawifs.r2022/hdf/'
            else:            #MODIS
                if model=='vgpm':
                    link = f'http://orca.science.oregonstate.edu/data/2x4/monthly/vgpm.r2022.m.chl.m.sst/hdf/'
                elif model=='cbpm':
                    link = f'http://orca.science.oregonstate.edu/data/2x4/monthly/cbpm2.modis.r2022/hdf/'
                else:
                    link = f'http://orca.science.oregonstate.edu/data/2x4/monthly/cafe.modis.r2022/hdf/'

            print(link)
            response = requests.get(link, timeout=10)
            if not response.ok:
                print(f'Problem with reading from web: {model=}, {source=}, {link=}')          
            else:
                soup = BeautifulSoup(response.content, 'html.parser')
                files = soup.find_all('a')
                for file in files:
                    filename = file.get('href')                        
                    if filename.endswith('.hdf.gz'):
                        print(f'{datetime.now().strftime("%Y/%m/%d %H:%M:%S")}:  Downloading {model=}, {source=}, {filename=} ...', end='', flush=True)
                        sf = filename.split('.')
                        outfilename = f'{model}.{source}.{sf[1]}.hdf'
                        outfile = fld_npp/outfilename
                        if outfile.exists():
                            if outfile.stat().st_size>0:
                                print(f'File {outfilename} already exists, skipping.')
                                continue

                        filelink = link+file.get('href')
                        response = requests.get(filelink)
                        if not response.ok:
                            print(f'Cannot download! ', response.status_code)
                        else:
                            try:
                                raw = io.BytesIO(response.content)
                                gz = gzip.GzipFile(fileobj=raw,mode='rb')
                                print(f'Saving to {outfilename}.')
                                
                                with open(outfile,'wb') as fid:
                                    fid.write(gz.read())
                            except:
                                print('\tError while saving !!!')


def calc_stats_peryear_new():
    fld_out_new = fld_out/'new_202411'
    df = pandas.read_csv(fn_input_new)
    df = df.rename(columns={'Unnamed: 0':'rowid'})    

    dfs = df[['siteID','LATITUDE','LONGITUDE']]
    print(f'Size of dataset: {len(dfs)}')

    dfs = dfs.drop_duplicates()
    print(f'Number of unique siteID, lat, lon: {len(dfs)}')
    print(f"Number of unique lat, lon: {len(dfs[['LATITUDE','LONGITUDE']].drop_duplicates())}")

    inlat = dfs['LATITUDE'].values
    inlon = dfs['LONGITUDE'].values
    insites = dfs['siteID'].values
    inlatlon = np.c_[inlat,inlon]

    lats, lons = get_lat_lon_grid()
    # Extend lat lon grid
    lats = np.r_[lats[0]+spacing, lats, lats[-1]-spacing]
    lons = np.r_[lons[0]-spacing, lons, lons[-1]+spacing]

    print('Calcualting statistics ...')
    
    #count_months={}
    for model in models: 
        print(model)
        stats={}
        for interp in interps:
            stats[f'{model}_{interp}']=[]
        for year in range(year_start, year_end+1):
            print(f'\t{year}')
            if year<=2002:
                source='seawifs'
            else:
                source='modis'
            files = sorted(list(fld_npp.glob(f'{model}.{source}.{year}*.hdf')))
            
            #count_months[f'{model}_{year}'] = len(files)
            data_year = np.empty((len(interps), len(files), len(inlat)))
            for i, fn in enumerate(files):
                with Dataset(fn) as nc:
                    data_npp = nc['npp'][:]
                    data_npp[data_npp<0] = np.nan
                    data_npp = extend_grid(data_npp)
                
                rgi = RegularGridInterpolator((lats, lons), data_npp)

                for j, interp in enumerate(interps):                    
                    data_interp = rgi(inlatlon, method=interp)
                    data_year[j,i,:] = data_interp

            for j,interp in enumerate(interps):
                # its possible that some points have some nan's in data
                dfss = pandas.DataFrame(dict(
                    cnt = (~np.isnan(data_year[j,:,:])).sum(axis=0),
                    min = np.nanmin(data_year[j,:,:], axis=0),
                    max = np.nanmax(data_year[j,:,:], axis=0),
                    mean = np.nanmean(data_year[j,:,:], axis=0),
                    std = np.nanstd(data_year[j,:,:], axis=0)
                ))
                dfss['year']=year+1
                dfss['siteID'] = insites
                stats[f'{model}_{interp}'].append(dfss)
                
        for modint in stats.keys():
            print(f'Saving sttistics for: {modint}')
            dfss = pandas.concat(stats[modint])
            dfss = dfss.set_index(['siteID','year'])

            dfm = df.copy()
            dfm = dfm.rename(columns={'YEAR':'year'}).set_index(['siteID','year']).join(dfss)
            dfm = dfm.reset_index()

            fn_out = fld_out_new/f'{modint}_stats.parquet'
            dfm.to_parquet(fn_out, compression='zstd')

     
def calc_stats_peryear():
    df = pandas.read_csv(fn_input) 
    df = df.rename(columns={'Unnamed: 0':'rowid'})
    inlat = df['rarefyID_y'].values
    inlon = df['rarefyID_x'].values
    inlatlon = np.c_[inlat,inlon]

    lats, lons = get_lat_lon_grid()
    # Extend lat lon grid
    lats = np.r_[lats[0]+spacing, lats, lats[-1]-spacing]
    lons = np.r_[lons[0]-spacing, lons, lons[-1]+spacing]

    print('Calcualting statistics ...')
    stats={}
    count_months={}
    for model in models:       
        print(model)
        for interp in interps:
            stats[f'{model}_{interp}']={} 
        for year in range(year_start, year_end+1):
            print(f'\t{year}')
            if year<=2002:
                source='seawifs'
            else:
                source='modis'
            files = sorted(list(fld_npp.glob(f'{model}.{source}.{year}*.hdf')))
            
            count_months[f'{model}_{year}'] = len(files)
            data_year = np.empty((len(interps), len(files), len(inlat)))
            for i, fn in enumerate(files):
                with Dataset(fn) as nc:
                    data_npp = nc['npp'][:]
                    data_npp[data_npp<0] = np.nan
                    data_npp = extend_grid(data_npp)
                
                rgi = RegularGridInterpolator((lats, lons), data_npp)

                for j, interp in enumerate(interps):                    
                    data_interp = rgi(inlatlon, method=interp)
                    data_year[j,i,:] = data_interp


            for j,interp in enumerate(interps):
                # its possible that some points have some nan's in data
                stats[f'{model}_{interp}'][f'cnt_{year}'] = (~np.isnan(data_year[j,:,:])).sum(axis=0)
                stats[f'{model}_{interp}'][f'min_{year}'] = np.nanmin(data_year[j,:,:], axis=0)
                stats[f'{model}_{interp}'][f'max_{year}'] = np.nanmax(data_year[j,:,:], axis=0)
                stats[f'{model}_{interp}'][f'mean_{year}'] = np.nanmean(data_year[j,:,:], axis=0)
                stats[f'{model}_{interp}'][f'std_{year}'] = np.nanstd(data_year[j,:,:], axis=0)
    
    # Export count of months per model per year
    data_cm = list(map(lambda x: x.split('_') + [count_months[x]], count_months.keys()))
    df_cm = pandas.DataFrame(data_cm, columns=['model','year','count'])
    fn_out = fld_out/'count_months.csv'
    df_cm.to_csv(fn_out, header=True, sep='\t')

    # Export statistics
    for modint in stats.keys():
        stat = stats[modint]

        dfs = pandas.DataFrame(stat)
        dfs = dfs[sorted(dfs.columns)]

        dfm = df.copy()
        dfm = pandas.concat((dfm, dfs), axis = 1)

        fn_out = fld_out/f'{modint}_stats.parquet'
        dfm.to_parquet(fn_out, compression='zstd')

def row_select_years(r):
    cols = list(filter(lambda x: x.name.startswith('cnt_'),r))

def calc_stats_fromyearmean():
    for model in models:
        for interp in interps:
            print(f'{model} {interp}')       
            modint = f'{model}_{interp}'

            fn_in = fld_out/f'{modint}_stats.parquet'
            df = pandas.read_parquet(fn_in)            

            cols = np.array(list(filter(lambda x: x.startswith('cnt_'), df.columns)))
            years = np.array(list(map(lambda x:int(x.split('_')[1]), cols)))

            mask_years = ~df.apply(lambda r: (r['startYear']<=years) & (years<=r['endYear']), axis='columns', result_type='expand').values
            mask_counts = ~df.apply(lambda r: r[cols].values==12, axis='columns', result_type='expand').values

            cols_mean = [f'mean_{year}' for year in years]
            data = df.loc[:,cols_mean].values
            data[mask_years | mask_counts] = np.nan

            
            df['cnt_years'] = np.isfinite(data).sum(axis=1)
            df['min_years'] = np.nanmin(data,axis=1)
            df['max_years'] = np.nanmax(data,axis=1)
            df['mean_years'] = np.nanmean(data, axis=1)
            df['std_years'] = np.nanstd(data, axis=1)
            
            df.to_parquet(fn_in)


def calc_stats_frommonthsmean():
    for model in models:
        for interp in interps:
            # model=models[0]; interp=interps[0]
            print(f'{model} {interp}')       
            modint = f'{model}_{interp}'
            fn_in = fld_out/f'{modint}_stats.parquet'
            df = pandas.read_parquet(fn_in)

            inlat = df['rarefyID_y'].values
            inlon = df['rarefyID_x'].values
            inlatlon = np.c_[inlat,inlon]

            lats, lons = get_lat_lon_grid()
            # Extend lat lon grid
            lats = np.r_[lats[0]+spacing, lats, lats[-1]-spacing]
            lons = np.r_[lons[0]-spacing, lons, lons[-1]+spacing]

            data = np.empty((len(df), 0))

            for year in range(year_start, year_end+1):
                print(f'\t{year}')
                if year<=2002:
                    source='seawifs'
                else:
                    source='modis'
                files = sorted(list(fld_npp.glob(f'{model}.{source}.{year}*.hdf')))
                # Skip years with less then 12 months of data
                if len(files)<12:
                    continue
                
                data_year = np.empty((len(df), 12))
                for i, fn in enumerate(files):
                    with Dataset(fn) as nc:
                        data_npp = nc['npp'][:]
                        data_npp[data_npp<0] = np.nan
                        data_npp = extend_grid(data_npp)
                    
                    rgi = RegularGridInterpolator((lats, lons), data_npp)
            
                    data_interp = rgi(inlatlon, method=interp)
                    data_year[:,i] = data_interp

                mask_years = ~df.apply(lambda r: (r['startYear']<=year) & (year<=r['endYear']), axis='columns', result_type='expand').values
                data_year[mask_years,:]=np.nan
                data = np.c_[data, data_year]

            df['cnt_months'] = np.isfinite(data).sum(axis=1)
            df['min_months'] = np.nanmin(data,axis=1)
            df['max_months'] = np.nanmax(data,axis=1)
            df['mean_months'] = np.nanmean(data, axis=1)
            df['std_months'] = np.nanstd(data, axis=1)

            df.to_parquet(fn_in)

def calc_timeseries():
    df = pandas.read_csv(fn_input) 
    df = df.rename(columns={'Unnamed: 0':'rowid'})
    inlat = df['rarefyID_y'].values
    inlon = df['rarefyID_x'].values
    inlatlon = np.c_[inlat,inlon]

    lats, lons = get_lat_lon_grid()
    # Extend lat lon grid
    lats = np.r_[lats[0]+spacing, lats, lats[-1]-spacing]
    lons = np.r_[lons[0]-spacing, lons, lons[-1]+spacing]

    start_date = datetime(1997,10,1)
    end_date = datetime(2023,12,1)
    time_index = pandas.date_range(start_date,end_date,freq="MS")

    all_data = {t: {} for t in time_index}
    for model in models:         
        # model=models[0]; 
        print(f'{model}')  
        for year in range(year_start, year_end+1):
            # year = year_start
            print(f'\t{year}')
            if year<=2002:
                source='seawifs'
            else:
                source='modis'
            files = sorted(list(fld_npp.glob(f'{model}.{source}.{year}*.hdf')))

            #data_year = np.empty((len(interps), len(files), len(inlat)))
            for i, fn in enumerate(files):
                # i=0; fn=files[i]
                with Dataset(fn) as nc:
                    # nc = Dataset(fn)
                    data_npp = nc['npp'][:]
                    data_npp[data_npp<0] = np.nan
                    data_npp = extend_grid(data_npp)
                    date = datetime.strptime(nc.getncattr('Start Time String'),'%m/%d/%Y %H:%M:%S')                    
                rgi = RegularGridInterpolator((lats, lons), data_npp)

                for j, interp in enumerate(interps):     
                    # interp=interps[0]                                   
                    data_interp = rgi(inlatlon, method=interp)
                    modint = f'{model}_{interp}'
                    all_data[date][modint]=data_interp

    for model in models:
        for interp in interps:
            modint = f'{model}_{interp}'
            cols = [date.strftime('%Y_%m') for date in sorted(all_data.keys())]
            dfo = pandas.DataFrame(index = df['rowid'], columns=cols)
            for date in all_data.keys():
                data = all_data[date].get(modint, np.empty(len(df['rowid'])))
                colname = date.strftime('%Y_%m')
                dfo[colname] = data

            dfo.to_parquet(fld_out/f'{modint}_ts.parquet')


def add_bathymetry():
    bathy = rasterio.open(fn_bathy)

    for model in models:
        for interp in interps:
            # model=models[0]; interp=interps[0]
            print(f'{model} {interp}')       
            modint = f'{model}_{interp}'
            fn_in = fld_out/f'{modint}_stats.parquet'
            df = pandas.read_parquet(fn_in)

            lonlat = df[['rarefyID_x','rarefyID_y']].values
            data = np.array(list(rasterio.sample.sample_gen(bathy, lonlat, 1, masked=True)))
            df['bathymetry'] = data

            df.to_parquet(fn_in)


def distance_to_coast():
    from coast_distance import distance_to_coast
    fn_coast = fn_input.parent/'gshhg-shp-2.3.7\GSHHS_shp\h\GSHHS_h_L1.shp'  

    import os
    import sys
    os.environ['GDAL_DATA'] = os.path.join(f'{os.sep}'.join(sys.executable.split(os.sep)[:-1]), 'Library', 'share', 'gdal')

    for model in models:
        for interp in interps:
            # model=models[0]; interp=interps[0]
            ttprint(f'{model} {interp}')       
            modint = f'{model}_{interp}'
            fn_in = fld_out/f'{modint}_stats.parquet'
            df = pandas.read_parquet(fn_in)

            lon, lat = df['rarefyID_x'].values, df['rarefyID_y'].values

            distance = distance_to_coast(lon, lat, fn_coast)

            df['dist_coast'] = distance

            df.to_parquet(fn_in)


if __name__=='__main__':
    #download_npp()
    #calc_stats_peryear()
    #calc_stats_frommonthsmean()
    #add_bathymetry()
    #distance_to_coast()
    #calc_timeseries()
    calc_stats_peryear_new()