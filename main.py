import pandas as pd

# read in observed discharge file, update variables as necessary
file_name = 'australia.csv'
name_length = len(file_name) - 3
file_path = '/Users/kaysha/Desktop/observed_discharge_station_lists (copy for project)/'
observed_discharge = pd.read_csv(file_path + file_name)
# drop location name from the gauge id
# observed_discharge['gauge_id'] = observed_discharge['gauge_id'].str[name_length:]
# observed_discharge['gauge_id'] = observed_discharge['gauge_id'].astype('string')


# read in upstream area file
file_name = 'ua_australia.csv'
file_path = '/Users/kaysha/Desktop/Hydroshare ua/'
upstream_area = pd.read_csv(file_path + file_name)
upstream_area_column = 'Tot_Drain_'
upstream_area = upstream_area.rename(columns={'HydroID': 'model_id', upstream_area_column: 'upstream_area'})
upstream_area = upstream_area[['model_id', 'upstream_area']]
# upstream_area['model_id'] = upstream_area['model_id'].astype('string')


merged_df = pd.merge(observed_discharge, upstream_area, on='model_id')
merged_df.to_csv('/Users/kaysha/Desktop/Merged_data/australia_merged.csv')
