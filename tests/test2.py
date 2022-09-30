import pyproj



def transform_lonlat_to_xy(gpgga_data_frame):
    # convert lat_deg_min to lat_deg
    lat_dm_array_str   = gpgga_data_frame['Latitude'].values
    lat_dm_array_float = [float(lat_str) for lat_str in lat_dm_array_str] # str -> float
    lat_d_array_int    = [int(lat_dm_float/100) for lat_dm_float in lat_dm_array_float]
    lat_m_array_float  = [(lat_dm_float/100 - lat_d_array_int[idx_lat]) for idx_lat, lat_dm_float in enumerate(lat_dm_array_float)]
    lat_d_array_float  = [lat_m_float*100/60 for lat_m_float in lat_m_array_float]
    lat_d_array        = [(lat_d_array_int[idx_lat]+lat_d_float) for idx_lat, lat_d_float in enumerate(lat_d_array_float)]

    # convert lon_deg_min to lon_deg
    lon_dm_array_str   = gpgga_data_frame['Longitude'].values
    lon_dm_array_float = [float(lon_str) for lon_str in lon_dm_array_str] # str -> float
    lon_d_array_int    = [int(lon_dm_float/100) for lon_dm_float in lon_dm_array_float]
    lon_m_array_float  = [(lon_dm_float/100 - lon_d_array_int[idx_lon]) for idx_lon, lon_dm_float in enumerate(lon_dm_array_float)]
    lon_d_array_float  = [lon_m_float*100/60 for lon_m_float in lon_m_array_float]
    lon_d_array        = [(lon_d_array_int[idx_lon]+lon_d_float) for idx_lon, lon_d_float in enumerate(lon_d_array_float)]  

     # transform from grs80 to x-y
    grs80 = pyproj.Proj(init='EPSG:6668')
    rect6 = pyproj.Proj(init='EPSG:6680')
    x_tmp, y_tmp  = pyproj.transform(grs80, rect6, lon_d_array, lat_d_array)
    # North:+, South:-
    north_south = gpgga_data_frame['North/South'].values
    y = [-y_tmp[idx_n_e] if n_or_e == 'S' else y_tmp[idx_n_e] for idx_n_e, n_or_e in enumerate(north_south)]
    # East:+, West:-
    east_west = gpgga_data_frame['East/West'].values
    x = [-x_tmp[idx_e_w] if e_or_w == 'W' else x_tmp[idx_e_w] for idx_e_w, e_or_w in enumerate(east_west)]
    # add x and y to data frame
    gpgga_data_frame['x'] = x
    gpgga_data_frame['y'] = y