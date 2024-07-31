import pandas as pd
import sys

#--- Rename all index columns into uppercase ---#
def rename_columns_index(path):
    df = pd.read_csv(path)
    df = df.rename(columns=
            {df.columns[0]: 'DATE', df.columns[1]: 'OPEN', 
            df.columns[2]: 'HIGH', df.columns[3]: 'LOW', df.columns[4]: 'CLOSE', 
            df.columns[5]: 'ADJ-CLOSE', df.columns[6]: 'VOLUME'}
            )
    df.to_csv(path, index=False)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python rename_columns_index.py <path>')
        sys.exit(1)
    
    path = sys.argv[1]
    rename_columns_index(path)