import pandas as pd

# read in observed discharge file, update variables as necessary
file_name = 'grdc.csv'  # update this line
file_path = '/Users/kaysha/Desktop/observed_discharge_station_lists (copy for project)/'
observed_discharge = pd.read_csv(file_path + file_name)
print(f"{file_name} length: {len(observed_discharge)}")
# uncomment below if using multiple files
'''file_name = 'belize.csv'
observed_discharge2 = pd.read_csv(file_path + file_name)
observed_discharge = pd.concat([observed_discharge, observed_discharge2])
print(f"{file_name} length: {len(observed_discharge2)}")'''


# read in upstream area file
file_name = 'ua_central_america.csv'  # update this line based on file
file_path = '/Users/kaysha/Desktop/Hydroshare ua/'
upstream_area = pd.read_csv(file_path + file_name)
upstream_area_column = 'Tot_Drain_'
upstream_area = upstream_area.rename(columns={'HydroID': 'model_id', upstream_area_column: 'upstream_area'})
upstream_area = upstream_area[['model_id', 'upstream_area']]

merged_df = pd.merge(observed_discharge, upstream_area, on='model_id')
merged_df = merged_df.sort_values(by=['model_id'])
print(f"original file length: {len(observed_discharge)}")
print(f"length of merged dataframe: {len(merged_df)}")
print(f"number of model id's in original but not in merged: {len(observed_discharge[~observed_discharge['model_id'].isin(merged_df['model_id'])])}")
print("model id's that aren't in this file: " + observed_discharge[~observed_discharge['model_id'].isin(merged_df['model_id'])]['model_id'].to_string(index=False))
merged_df.to_csv('/Users/kaysha/Desktop/Merged_data/central_america_merged.csv', index=False)
