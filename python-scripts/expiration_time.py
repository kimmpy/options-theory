#-- Adds time to expiration column --#
import pandas as pd
import datetime as dt

def expiration(file):
    # ONLY parses through 'DATE' and 'EXPIRATION' columns
    df = pd.read_csv(file, parse_dates=['DATE', 'EXPIRATION'])

    # IMPORTANT! csv files saves datetime as string, so you have to convert them back into datetime
    #df['DATE'] = pd.to_datetime(df['DATE'])
    #df['EXPIRATION'] = pd.to_datetime(df['EXPIRATION'])
    
    # Subtracts expiration from data and adds to new column then saves to new csv
    df['TIME-TO-EXPIRATION'] = (df['EXPIRATION'] - df['DATE']).dt.days
    df.to_csv(file)


file = input('Input file name: ')

expiration(file)
