import pandas as pd

def string_to_datetime(file_name):
    df = pd.read_csv(file_name)
    df = df[df['EXPIRATION'].str.contains('2024')]
    df['EXPIRATION'] = pd.to_datetime(df['EXPIRATION'], format='%m %d %Y')
    df.to_csv(file_name)

file_name = input('Enter file name: ')
string_to_datetime(file_name)
