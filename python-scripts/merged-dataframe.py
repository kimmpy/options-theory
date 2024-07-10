import pandas as pd
import glob

# Get a list of all TXT files in a directory
csv_files = sorted(glob.glob('*flxopint*.csv'))

# Create an empty dataframe to store the combined data
combined_df = pd.DataFrame()

# Loop through each CSV file and append its contents to the combined dataframe
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    combined_df = pd.concat([combined_df, df])

# Save dataframe into a csv file (make the csv file before doing this)
combined_df.drop('Unnamed: 0', inplace=True, axis=1) 
#combined_df.drop('Unnamed: 0.1', inplace=True, axis=1)
combined_df.to_csv('april-df.csv')
