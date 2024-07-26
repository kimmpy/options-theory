#-- Combine all csv files in a given directory and all of its sub-directories --#
import pandas as pd
import glob
import os
import sys

def combine_dfs(path):
    # Sorts before globbing all files with .csv extension
    files = sorted(glob.glob(path + '/*.csv', recursive=False))
    
    # Create empty DataFrame for merging
    combined_df = pd.DataFrame()

    # Loops through each file in the glob and concatinates to combined_df
    for file in files:
        temp_df = pd.read_csv(file)
        combined_df = pd.concat([combined_df, temp_df], ignore_index=True)

    # Output file name based on directory name
    dir_name = os.path.basename(path)
    output_name = os.path.join(os.path.dirname(path), f'{dir_name}.csv')

    combined_df.to_csv(output_name, index=False)


if __name__ == 'main':
    if len(sys.argv) != 2:
        print('Usage: python combine_dfs.py <root_path>')
        sys.exit(1)
    
    path = sys.argv[1]
    combine_dfs(path)