import numpy as np
from scipy.stats import norm
import pandas as pd
N = norm.cdf

def bs_vega(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return S * norm.pdf(d1) * np.sqrt(T)

def bs_call(S, K, T, r, vol):
    d1 = (np.log(S/K) + (r + 0.5*vol**2)*T) / (vol*np.sqrt(T))
    d2 = d1 - vol * np.sqrt(T)
    return S * N(d1) - np.exp(-r * T) * K * N(d2)

def find_vol_call(target_value, S, K, T, r, *args):
    MAX_ITERATIONS = 100000
    PRECISION = 1.0e-5
    sigma = 0.5
    for i in range(0, MAX_ITERATIONS):
        price = bs_call(S, K, T, r, sigma)
        vega = bs_vega(S, K, T, r, sigma)
        diff = target_value - price  # root
        if (abs(diff) < PRECISION):
            return sigma
        sigma = sigma + diff/vega # f(x) / f'(x)
    return sigma # value wasn't found, return best guess so far

def bs_put(S, K, T, r, vol):
    d1 = (np.log(S/K) + (r + 0.5*vol**2)*T) / (vol*np.sqrt(T))
    d2 = d1 - vol * np.sqrt(T)
    return K * np.exp(-r * T) * N(-d2) - S * N(-d1)

def find_vol_put(target_value, S, K, T, r, *args):
    MAX_ITERATIONS = 100
    PRECISION = 1.0e-5
    sigma = 0.5
    for i in range(0, MAX_ITERATIONS):
        price = bs_put(S, K, T, r, sigma)
        vega = bs_vega(S, K, T, r, sigma)
        diff = target_value - price  # root
        if (abs(diff) < PRECISION):
            return sigma
        sigma = sigma + diff/vega # f(x) / f'(x)
    return sigma # value wasn't found, return best guess so far


"""
S = 38892.800781
K = 391.16
T = 74/365.0
r = 0.0
vol = 0.15

V_market = bs_put(S, K, T, r, vol)
implied_vol = find_vol_put(V_market, S, K, T, r)

print ('Implied vol: %.2f%%' % (implied_vol))
print ('Market price = %.2f' % V_market)
print ('Model price = %.2f' % bs_put(S, K, T, r, implied_vol))

d1 = (np.log(S/K) + (r + 0.5*vol**2)*T) / (vol*np.sqrt(T))
d2 = d1 - vol * np.sqrt(T)
print(K * np.exp(-r * T) * N(d2) - S * N(d1))
print(S * N(d1) - np.exp(-r * T) * K * N(d2))
"""
df = pd.read_csv('../repo/data/merged-flex-index/RUT_merged.csv')
implied_vols = []

for index, row in df.iterrows():
    flag = row['P/C'].lower()
    S = row['ADJ CLOSE']
    K = row['STRIKE-PRICE']
    T = row['TIME-TO-EXPIRATION'] / 365.0
    r = 0.0
    vol_guess = 0.15

    if (flag=='c'):
        v_market = bs_call(S, K, T, r, vol_guess)
        implied_vol = find_vol_call(v_market, S, K, T, r)
    elif (flag=='p'):
        v_market = bs_put(S, K, T, r, vol_guess)
        implied_vol = find_vol_put(v_market, S, K, T, r)
    
    implied_vols.append(implied_vol*100)
    

print(implied_vols)
df['IV'] = implied_vols
df.to_csv('RUT_iv.csv', index=False)
