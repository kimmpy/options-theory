#-- Combine all csv files in a given directory and all of its sub-directories --#
import pandas as pd
import glob

def combine_csv_dfs(path, output_name):
    # Sorts before globbing all files with .csv extension
    files = sorted(glob.glob(path + '/*.csv', recursive=False))
    
    # Create empty DataFrame for merging
    combined_df = pd.DataFrame()

    # Loops through each file in the glob and concatinates to combined_df
    for file in files:
        temp_df = pd.read_csv(file)
        combined_df = pd.concat([combined_df, temp_df])

    # Saves to a new csv file
    combined_df.to_csv(output_name)




path = input('Enter path: ')
output_name = input('Enter output file name: ')
combine_csv_dfs(path, output_name)
