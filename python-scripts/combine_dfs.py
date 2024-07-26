#-- Combine all csv files in a given directory and all of its sub-directories --#
import pandas as pd
import glob
import os
import sys

def combine_dfs(path):
    # Sorts before globbing all files with .csv extension
    files = glob.glob(path + '/csv/*.csv', recursive=False)
    
    # Create empty DataFrame for merging
    combined_df = pd.DataFrame()

    # Loops through each file in the glob and concatinates to combined_df + '/csv/*.csv'
    for file in files:
        temp_df = pd.read_csv(file)
        combined_df = pd.concat([combined_df, temp_df], ignore_index=True)

    # Get absolute path, output file name based on directory name
    abs_path = os.path.abspath(path)
    dir_name = os.path.basename(abs_path)
    output_name = os.path.join(os.path.dirname(path), f'{dir_name}.csv')

    combined_df = combined_df.sort_values(by=['DATE', 'EXPIRATION', 'TIME-TO-EXPIRATION'])
    combined_df = combined_df[combined_df['TIME-TO-EXPIRATION']!=0]
    combined_df.to_csv(output_name, index=False)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python combine_dfs.py <root_path>')
        sys.exit(1)
    
    path = sys.argv[1]
    combine_dfs(path)