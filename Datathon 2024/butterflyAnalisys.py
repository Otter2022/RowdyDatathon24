import pandas as pd
import glob
from datetime import datetime

# Define the function to determine if a date is in spring or fall
def determine_season(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    month = date.month
    if 3 <= month <= 5:  # March to May
        return 'Spring'
    elif 9 <= month <= 11:  # September to November
        return 'Fall'
    else:
        return None  # Return None for other seasons

# List to hold all the DataFrames
dfs = []

# Loop over all CSV files with the format "daily_aqi_by_county_20##.csv"
for file in glob.glob("datathon_data//daily_aqi_by_county_20*.csv"):
    # Read the CSV file
    df = pd.read_csv(file)
    
    # Select the relevant columns
    df_selected = df[['State Name', 'county Name', 'State Code', 'County Code', 'Date','AQI','Category','Defining Parameter']]
    
    # Add the "Season" column based on the date
    df_selected['Season'] = df_selected['Date'].apply(determine_season)
    
    # Filter out rows where the season is neither Fall nor Spring (i.e., None)
    df_filtered = df_selected[df_selected['Season'].notna()]
    
    # Append the filtered DataFrame to the list
    dfs.append(df_filtered)

# Concatenate all DataFrames into one
final_df = pd.concat(dfs, ignore_index=True)

# Display the DataFrame
print(final_df)

# Optionally, save the final DataFrame to a CSV file
final_df.to_csv('data//filtered_aqi_season_data.csv', index=False)

print("Data saved to 'filtered_aqi_season_data.csv'")
