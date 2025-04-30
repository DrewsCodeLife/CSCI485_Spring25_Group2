'''
Author: Drew Mortenson, with ChatGPT's guidance (eda_chat.txt)
'''

import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of this script
data_folder = os.path.join(script_dir, 'section_of_road')

# Define the station metadata manually (you already have it)
station_metadata = {
    715898: {"Type": "Mainline", "Lat": 33.880149, "Lon": -118.021730},
    715901: {"Type": "On Ramp", "Lat": 33.883681, "Lon": -118.027733},
    762355: {"Type": "Off Ramp", "Lat": 33.883681, "Lon": -118.027733},
    716899: {"Type": "Mainline", "Lat": 33.883681, "Lon": -118.027733},
    716900: {"Type": "Mainline", "Lat": 33.887208, "Lon": -118.033784},
    715903: {"Type": "On Ramp", "Lat": 33.887208, "Lon": -118.033784},
    762353: {"Type": "Mainline", "Lat": 33.890681, "Lon": -118.040822},
    775012: {"Type": "Mainline", "Lat": 33.892658, "Lon": -118.044406},
    716904: {"Type": "Mainline", "Lat": 33.894742, "Lon": -118.048204},
    716903: {"Type": "Off Ramp", "Lat": 33.894742, "Lon": -118.048204},
    715905: {"Type": "On Ramp", "Lat": 33.894742, "Lon": -118.048204},
    718358: {"Type": "Mainline", "Lat": 33.897164, "Lon": -118.052409},
    769625: {"Type": "Mainline", "Lat": 33.900495, "Lon": -118.058289}, 
    769626: {"Type": "Off Ramp", "Lat": 33.900495, "Lon": -118.058289},
    762357: {"Type": "On Ramp", "Lat": 33.905090, "Lon": -118.065005}, # This is labelled as an Off Ramp on PeMS. It geographically cannot be an offramp.
    718081: {"Type": "Mainline", "Lat": 33.905090, "Lon": -118.065005},  
    718360: {"Type": "Mainline", "Lat": 33.907708, "Lon": -118.067623},
}

# Placeholder list to collect per-station DataFrames
all_stations_data = []

# Loop through your station IDs
for station_id, meta in station_metadata.items():
    # Build expected filenames based on your naming scheme
    if meta['Type'] == 'Mainline':
        flow_occ_file = f'Mainline VDS {station_id} Flow & Occup.xlsx'
        speed_q_file = f'Mainline VDS {station_id} Speed & Q.xlsx'
    else:  # OnRamp or OffRamp
        flow_occ_file = f'{meta["Type"]} VDS {station_id} Flow & Occup.xlsx'
        speed_q_file = None  # No speed/Q for ramps

    # Read the flow/occupancy data
    flow_occ_path = os.path.join(data_folder, flow_occ_file)
    flow_occ_df = pd.read_excel(flow_occ_path)

    # If Mainline, also read speed/Q
    if speed_q_file:
        speed_q_path = os.path.join(data_folder, speed_q_file)
        speed_q_df = pd.read_excel(speed_q_path)
        # Merge flow_occ_df and speed_q_df on the time column
        merged_df = pd.merge(flow_occ_df, speed_q_df, on='5 Minutes')
    else:
        merged_df = flow_occ_df.copy()

    # Add metadata columns
    merged_df['Station_ID'] = station_id
    merged_df['Station_Type'] = meta['Type']
    merged_df['Latitude'] = meta['Lat']
    merged_df['Longitude'] = meta['Lon']

    # Append to the full list
    all_stations_data.append(merged_df)

# Concatenate all station DataFrames into one big DataFrame
full_data = pd.concat(all_stations_data, ignore_index=True)

# Save master DataFrame
full_data.to_pickle('full_station_data.pkl')  # Fast loading
full_data.to_csv('full_station_data.csv', index=False)  # Human-readable backup
