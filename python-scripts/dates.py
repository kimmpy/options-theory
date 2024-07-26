#-- Reads txt file and converts to csv before adding date column --#
import pandas as pd
import sys
from datetime import datetime
# Reads txt file then converts to csv
def add_dates(file):
    df = pd.read_fwf(file)
    # df.to_csv(file)

    #--- Assuming file name is in format flxopint.YYYYMMDD.txt ---#
    # Extract file name
    file_name = file.split('/')[-1]

    # Extract date then convert to datetime
    date_str = file_name.split('.')[1]
    date = datetime.strptime(date_str, '%Y%m%d')

    # Changing expiration column from string to datetime
    df['EXPIRATION'] = pd.to_datetime(df['EXPIRATION'], format='%m %d %Y')
    # # Fixing format
    df['EXPIRATION'] = df['EXPIRATION'].dt.strftime('%Y-%m-%d')

    # Reads the new csv and adds a date column with the corresponding date in file name
    df['DATE'] = date

    # Convert 'EXPIRATION' and 'DATE' to datetime
    df['EXPIRATION'] = pd.to_datetime(df['EXPIRATION'])
    df['DATE'] = pd.to_datetime(df['DATE'])

    # Calculate the difference in days and add as a new column 'DAYS_TO_EXPIRATION'
    df['TIME-TO-EXPIRATION'] = (df['EXPIRATION'] - df['DATE']).dt.days

    # Saves to new csv file
    df = df[['SYMBOL', 'P/C', 'DATE', 'EXPIRATION', 'TIME-TO-EXPIRATION', 'STRIKE-PRICE', 'MARK-PRICE', 'OPEN-INTEREST']]
    output_file = file.replace('.txt', '.csv')
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    file=sys.argv[1]
    add_dates(file)