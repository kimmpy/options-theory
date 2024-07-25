import pandas as pd
import numpy as np
from scipy.stats import norm

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

    if vega==0:
        vega = 0.1
    return vega

#-- Implied volatility using Newton's method --#
def iv(row, tol=1e-6, max_iterations=100):
    flag = row['P/C']
    S = row['ADJ CLOSE']
    K = row['STRIKE-PRICE']
    T = row['TIME-TO-EXPIRATION']/365.0
    r = 0.0
    market_price = row['MARK-PRICE']

    # Initial sigma guess based on historical volatility
    sigma = 0.1569
    min_sigma = 1e-4
    max_sigma = 10.0

    # Newton's method with max iterations to find sigma
    for i in range(0, max_iterations):
        price = bs(S, K, T, r, sigma, flag)
        vega_val = vega(S, K, T, r, sigma)
        price_diff = price - market_price

        if abs(price_diff) < tol:
            return sigma
        
        sigma_update = sigma - price_diff / vega_val
        # Ensure sigma stays within bounds
        sigma = max(min_sigma, min(max_sigma, sigma_update))
        
    return sigma

file = input('Enter file path: ')
df = pd.read_csv(file)

df['IV'] = df.apply(iv, axis=1)

df.to_csv('tmp3.csv')