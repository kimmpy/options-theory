import pandas as pd
import numpy as np
from scipy.stats import norm
import os
import sys

#-- Black-Scholes formula to find price --#
def bs(S, K, T, r, sigma, flag):
    # Calculates d1 and d2
    d1 = np.float64(np.log(S / K) + (r + 0.5 * np.float64(sigma)**2) * T) / (np.float64(sigma) * np.sqrt(T))
    d2 = np.float64(d1 - np.float64(sigma) * np.sqrt(T))

    # Selects formula based on call or put 
    if flag == 'C':
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

#-- Calculates options Greek Vega --#
def vega(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    vega = S * norm.pdf(d1) * np.sqrt(T)

    if vega == 0:
        vega = 0.1
    
    return vega

#-- Implied volatility using Newton's method --#
def iv(row):
    flag = row['P/C']
    S = row['ADJ-CLOSE']
    K = row['STRIKE-PRICE']
    T = row['TIME-TO-EXPIRATION']/365.0
    r = 0.0
    market_price = row['MARK-PRICE']

    # Initial sigma guess based on historical volatility
    sigma = 5
    min_sigma = 1e-4
    max_sigma = 5
    price_diff = 0.05

    # Newton's method with max iterations to find sigma
    while price_diff > 1e-6:
        price = bs(S, K, T, r, sigma, flag)
        vega_val = vega(S, K, T, r, sigma)
        price_diff = price - market_price
        
        sigma_update = sigma - price_diff / vega_val
        
        # Ensure sigma stays within bounds
        sigma = max(min_sigma, min(max_sigma, sigma_update))

        if sigma==0.0001:
            return 0.0
        
    print(row.name)
    return sigma

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python iv_manual.py <root_path> <symbol>')
        sys.exit(1)
    
    path = sys.argv[1]
    symbol = sys.argv[2]
    df = pd.read_csv(path)
    df['IV'] = df.apply(iv, axis=1)

    # Get absolute path, output file name based on directory name
    abs_path = os.path.abspath(path)
    dir_name = os.path.basename(abs_path)
    symbol = dir_name[:len(symbol)]
    
    output_name = os.path.join(os.path.dirname(path), f'{symbol}_iv.csv')

    df.to_csv(output_name, index=False)