#-- Merges flex index csv files --#
import pandas as pd
import sys

def merge(flex_path, index_path, symbol):
    flex_df = pd.read_csv(flex_path)
    index_df = pd.read_csv(index_path)

    # Filters flex_df based on underlying stock symbol
    pattern = f"(?=.*{symbol})(?=.*[24])"
    filtered_flex_df = flex_df[flex_df['SYMBOL'].str.contains(pattern, na=False)]

    index_df = index_df.rename(columns=
                {index_df.columns[0]: 'DATE', index_df.columns[1]: 'OPEN', 
                index_df.columns[2]: 'HIGH', index_df.columns[3]: 'LOW', index_df.columns[4]: 'CLOSE', 
                index_df.columns[5]: 'ADJ-CLOSE', index_df.columns[6]: 'VOLUME'})
    
    # Merges the filtered_flex_df and index_df based on date
    merged_df = filtered_flex_df.merge(index_df, how='inner', on='DATE')

    # Rename all index columns into uppercase

    merged_df.to_csv(symbol + '.csv', index=False)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python merge_flex_index.py <flex_path> <index_path> <filter>')
        sys.exit(1)
    
    flex_path = sys.argv[1]
    index_path = sys.argv[2]
    symbol = sys.argv[3]

    merge(flex_path, index_path, symbol)