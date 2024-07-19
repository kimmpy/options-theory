from py_vollib.black_scholes import black_scholes
from py_vollib.black_scholes.implied_volatility import implied_volatility
import pandas as pd

df = pd.read_csv('../../merged-flex-index/GSPC_merged.csv')
implied_vols = []

for index, row in df.iterrows():
    flag = row['P/C'].lower()
    S = row['ADJ CLOSE']
    K = row['STRIKE-PRICE'] 
    T = row['TIME-TO-EXPIRATION'] / 365.0
    r = 0.0
    price = row['MARK-PRICE'] 

    try:
        implied_vol = implied_volatility(price, S, K, T, r, flag)
    except Exception as e:
        # Handle exception (e.g., print error message, log, set implied volatility to NaN)
        print(f"Error occurred for row {index}: {e}")
        implied_vol = 0.0
    print(implied_vol)
    implied_vols.append(implied_vol)
    

print(implied_vols)
df['IV'] = implied_vols
df = df.loc[df['IV']>=0.001]
df_sorted = df.sort_values(by='EXPIRATION')
df_sorted.to_csv('GSPC_test.csv', index=False)
