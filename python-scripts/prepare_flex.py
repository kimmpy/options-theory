#-- Reads txt file and converts to csv before adding date column --#
import pandas as pd
import sys
from datetime import datetime

"""
* Extracts Date from file name then adds it as DateTime to new column
* Converts Expiration to DateTime
* Adds a new column that subtracts Expiration from DateTime to get Time-To-Expiration
* Converts new file to CSV
"""
def prepare_flex(file):
    df = pd.read_fwf(file)

    # Assuming file name is in format flxopint.YYYYMMDD.txt
    # Extract file name
    file_name = file.split('/')[-1]

    # Extract date, converts to DateTime, then adds to new column
    date_str = file_name.split('.')[1]
    date = datetime.strptime(date_str, '%Y%m%d')
    df['DATE'] = date

    # Changing expiration column from string to datetime
    df['EXPIRATION'] = pd.to_datetime(df['EXPIRATION'], format='%m %d %Y')
    df['EXPIRATION'] = df['EXPIRATION'].dt.strftime('%Y-%m-%d')

    # Convert 'EXPIRATION' and 'DATE' to datetime
    df['EXPIRATION'] = pd.to_datetime(df['EXPIRATION'])
    df['DATE'] = pd.to_datetime(df['DATE'])

    # Calculate the difference in days and add as a new column 'DAYS_TO_EXPIRATION'
    df['TIME-TO-EXPIRATION'] = (df['EXPIRATION'] - df['DATE']).dt.days

    # Convert Strike Price from string to float
    df['STRIKE-PRICE'] = df['STRIKE-PRICE'].str.replace(' ', '.').astype(float)

    # Fix column order, convert file to csv, then save as new file
    df = df[['SYMBOL', 'P/C', 'DATE', 'EXPIRATION', 'TIME-TO-EXPIRATION', 'STRIKE-PRICE', 'MARK-PRICE', 'OPEN-INTEREST']]
    output_file = file.replace('.txt', '.csv')
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    file=sys.argv[1]
    prepare_flex(file)