import pandas as pd

def rewrite_type_series_float(file_path):
    df = pd.read_csv(file_path)
    df['STRIKE-PRICE'] = df['STRIKE-PRICE'].str.replace(' ', '.').astype(float)
    df.to_csv(file_path)

file_path = input('Enter file path: ')
rewrite_type_series_float(file_path)