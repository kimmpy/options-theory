import pandas as pd

def string_to_datetime(file_name):
    df = pd.read_csv(file_name)
    df['DATE'] = pd.to_datetime(df['DATE'], format='%m %d %Y')
    df.to_csv(file_name)

file_name = ('Enter file name: ')
string_to_datetime(file_name)
