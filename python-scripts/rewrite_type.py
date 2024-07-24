#-- Some flex report columns have numbers formatted as strings with ' ' instead of '.' --#
#-- Used to fix --#
import pandas as pd

def rewrite_type(file_path):
    df = pd.read_csv(file_path)

    # Replaces ' ' with '.' then converts to float
    df['STRIKE-PRICE'] = df['STRIKE-PRICE'].str.replace(' ', '.').astype(float)
    df.to_csv(file_path)

file_path = input('Enter file path: ')
rewrite_type(file_path)