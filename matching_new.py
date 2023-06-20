import os
import pandas as pd
import geopandas as gpd


# read in observed discharge file, update variables as necessary
folder_path = '/Users/kaysha/Desktop/TDX_observed_discharge/60s/'  # update this line with folder
files = os.listdir(folder_path)
for file in files:
    file_path = os.path.join(folder_path, file)
    observed_discharge = pd.read_csv(file_path)
    file_id = file[:10]
    print(f"observed discharge {file_id} read in")
    observed_discharge = observed_discharge.drop(['Unnamed: 0.2', 'Unnamed: 0.1', 'Unnamed: 0', 'geometry', 'HYBAS_ID',
                                                  'SUB_AREA', 'index_right'], axis=1)
    observed_discharge['model_id'] = observed_discharge['model_id'].astype(int)

    # read in upstream area file
    file_name = 'TDX_streamnet_' + file_id + '_01.gpkg'
    file_path = '/Users/kaysha/Downloads/tdxhydro_streams_60s_southamerica/'  # update this line too
    upstream_area = gpd.read_file(file_path + file_name)
    print("upstream area read in")
    upstream_area = upstream_area[['LINKNO', 'DSContArea']]
    upstream_area_column = 'DSContArea'
    upstream_area = upstream_area.rename(columns={'LINKNO': 'streamID'})

    # create new, merged dataframe
    merged_df = pd.merge(observed_discharge, upstream_area, on='streamID')
    merged_df = merged_df.sort_values(by=['streamID'])
    print(f"original file length: {len(observed_discharge)}")
    print(f"length of merged dataframe: {len(merged_df)}")
    merged_df.to_csv('/Users/kaysha/Desktop/Merged_TDX_data/' + file_id + '.csv', index=False)
