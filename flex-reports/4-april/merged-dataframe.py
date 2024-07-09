   SYMBOL   P/C   EXPIRATION   STRIKE-PRICE   MARK-PRICE   OPEN-INTEREST   
import pandas as pd
import glob

# Get a list of all TXT files in a directory
txt_files = glob.glob('*.txt')

# Create an empty dataframe to store the combined data
combined_df = pd.DataFrame()

# Loop through each CSV file and append its contents to the combined dataframe
for txt_file in txt_files:
    df = pd.read_fwf(txt_file)
    combined_df = pd.concat([combined_df, df])

# Save dataframe into a csv file (make the csv file before doing this)
combined_df.to_csv('test.csv')
