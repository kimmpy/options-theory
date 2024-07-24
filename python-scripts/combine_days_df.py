#-- Combine dataframes, sorted, chronologically --#
import pandas as pd
import glob

# Get a list of all TXT files in a directory, sorted
csv_files = sorted(glob.glob('*flxopint*.csv'))

# Create an empty dataframe to store the combined data
combined_df = pd.DataFrame()

# Loop through each CSV file and append its contents to the combined dataframe
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    combined_df = pd.concat([combined_df, df])

# Save dataframe into a csv file
combined_df.to_csv('4_df.csv')
