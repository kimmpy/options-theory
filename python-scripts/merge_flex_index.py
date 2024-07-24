#-- Merges flex index csv files --#
import pandas as pd

def merge(flex_file, index_name, symbol, output_file):
    flex_df = pd.read_csv(flex_file)
    index_df = pd.read_csv(index_name)

    # Filters flex_df based on underlying stock symbol
    filtered_flex_df = flex_df[flex_df['SYMBOL'].str.contains(symbol, na=False)]
    
    # Merges the filtered_flex_df and index_df based on date
    merged_df = filtered_flex_df.merge(index_df, how='inner', on='DATE')

    merged_df.to_csv(output_file)

flex_file = input('Enter flex report file path: ')
index_file = input('Enter underlying stock file path: ')
symbol = input('Enter filter: ')
output_file = input('Enter name of output file: ')

merge(flex_file, index_file, symbol, output_file)