import pandas as pd

df = pd.read_fwf('flxopint.20240405.txt')
df.to_csv('flxopint.20240405.csv')

csv_input = pd.read_csv('flxopint.20240405.csv')
csv_input['DATE'] = '04 05 2024'
csv_input.to_csv('flxopint.20240405.csv', index=False)
