#-- Changes date columns from string (ex: 'xx xx 20xx') to DateTime
import pandas as pd

def string_to_datetime(file_name):
    df = pd.read_csv(file_name)

    # I forgot why I put this here but probably to fix bug?
    df = df[df['EXPIRATION'].str.contains('2024')]

    # Formats the string into month-day-year format in DateTime
    df['EXPIRATION'] = pd.to_datetime(df['EXPIRATION'], format='%m %d %Y')
    df.to_csv(file_name)

file_name = input('Enter file name: ')
string_to_datetime(file_name)
