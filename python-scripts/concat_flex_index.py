import os
import sys
import pandas as pd

def concat_flex_index(base_dir, symbol):
    dataframes = []
    is_first_dir = True

    # Walk through all subdirectories
    for root, _, files in os.walk(base_dir):
        # Skips the current working directory
        if is_first_dir:
            is_first_dir = False
            continue
        for file_name in files:
            # Check if symbol is in the file name
            if symbol in file_name:
                # Full path to the file
                file_path = os.path.join(root, file_name)
                
                df = pd.read_csv(file_path)
                dataframes.append(df)
    
    # Concatenate all dataframes
    merged_df = pd.concat(dataframes, ignore_index=True)
    merged_df = merged_df.sort_values(by=['DATE', 'EXPIRATION', 'TIME-TO-EXPIRATION'])

    # Save the merged dataframe to a new CSV file
    output_file = os.path.join(base_dir, symbol + '_concat.csv')
    merged_df.to_csv(output_file, index=False)

    print(f"Files concatenated successfully! Output saved to {output_file}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python concat_flex_index.py <base_directory> <symbol>")
        sys.exit(1)

    base_dir = sys.argv[1]
    symbol = sys.argv[2]
    concat_flex_index(base_dir, symbol)