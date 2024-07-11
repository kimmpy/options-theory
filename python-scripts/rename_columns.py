import pandas as pd

csv = input('Enter csv file name: ')
df = pd.read_csv(csv)

df = df.rename(columns={df.columns[0]: 'DATE', df.columns[1]: 'OPEN', df.columns[2]: 'HIGH', df.columns[3]: 'LOW', df.columns[4]: 'CLOSE', df.columns[5]: 'ADJ CLOSE', df.columns[6]: 'VOLUME'})
df.to_csv(csv)
