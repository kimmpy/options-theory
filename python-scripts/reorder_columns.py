#-- Changes columns around into correct order for FLEX REPORTS --#
import pandas as pd

def reorder(csv_file):
    df = pd.read_csv(csv_file)

    # Rearrange columns
    df_reorder = df[['DATE', 'SYMBOL', 'P/C', 'EXPIRATION', 'STRIKE-PRICE', 'MARK-PRICE', 'OPEN-INTEREST']]
    df_reorder.to_csv(csv_file, index=False)


csv_file = input('Enter csv file name: ')
reorder(csv_file)
