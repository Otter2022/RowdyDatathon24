import pandas as pd

# Load the CSV files into pandas DataFrames
before_df = pd.read_csv("data//states_and_counties.csv")
after_df = pd.read_csv("data//PM2.5_data.csv")

import pandas as pd


# Merge the two DataFrames on 'State Name' and 'State Code'
merged_df = pd.merge(after_df, before_df[['State Code', 'State Abbreviation', 'State Name']],
                     on=['State Name', 'State Code'], how='left')

# Save the result to a new CSV file
merged_df.to_csv("after_with_state_abbreviation.csv", index=False)
