import pandas as pd
import datetime as dt

def expiration(file):
    df = pd.read_csv(file, parse_dates=['DATE', 'EXPIRATION'])
    #df['DATE'] = pd.to_datetime(df['DATE'])
    #df['EXPIRATION'] = pd.to_datetime(df['EXPIRATION'])
    
    df['TIME-TO-EXPIRATION'] = (df['EXPIRATION'] - df['DATE']).dt.days
    df.to_csv(file)


file = input('Input file name: ')

expiration(file)
