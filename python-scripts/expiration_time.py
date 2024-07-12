import pandas as pd
import datetime as dt

def expiration (file):
    df = pd.read_csv(file)
    df['DATE'] = pd.to_datetime(df['DATE'])
    df['EXPIRATION'] = pd.to_datetime(df['EXPIRATION'])
    df['TIME-TO-EXPIRATION'] = df['EXPIRATION'] - df['DATE']
    df['TIME-TO-EXPIRATION'] = df['TIME-TO-EXPIRATION'].dt.days
    