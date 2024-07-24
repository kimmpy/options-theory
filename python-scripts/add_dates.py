#-- Reads txt file and converts to csv before adding date column --#
import pandas as pd

# Reads txt file then converts to csv
df = pd.read_fwf('flxopint.20240405.txt')
df.to_csv('flxopint.20240405.csv')

# Reads the new csv and adds a data column with the corresponding date in file name
csv_input = pd.read_csv('flxopint.20240405.csv')
csv_input['DATE'] = '04 05 2024'

# Saves to new csv file
csv_input.to_csv('flxopint.20240405.csv', index=False)
