import pandas as pd
import glob

def combine_csv_dfs(path, output_name, rm_unnamed0):
    files = sorted(glob.glob(path + '/**/*.csv', recursive=False))
    
    combined_df = pd.DataFrame()

    for file in files:
        temp_df = pd.read_csv(file)
        combined_df = pd.concat([combined_df, temp_df])

    if (rm_unnamed0):
        combined_df.drop('Unnamed: 0', inplace=True, axis=1)

    combined_df.to_csv(output_name)




path = input('Enter path: ')
output_name = input('Enter output file name: ')
rm_unnamed0 = input('Remove Unnamed: 0 column? ')
combine_csv_dfs(path, output_name, rm_unnamed0)
