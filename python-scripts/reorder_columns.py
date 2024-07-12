import pandas as pd

def reorder(csv_file):
    df = pd.read_csv(csv_file)
    df_reorder = df[['DATE', 'SYMBOL', 'P/C', 'EXPIRATION', 'STRIKE-PRICE', 'MARK-PRICE', 'OPEN-INTEREST']] # rearrange column here
    df_reorder.to_csv(csv_file, index=False)


csv_file = input('Enter csv file name: ')
reorder(csv_file)
