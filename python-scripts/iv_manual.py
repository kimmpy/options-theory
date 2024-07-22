import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy.optimize import newton

def bs_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 *sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

def bs_put(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 *sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price

def iv(row):
    flag = row['P/C']
    S = row['ADJ CLOSE']
    K = row['STRIKE-PRICE']
    T = row['TIME-TO-EXPIRATION']/365.0
    r = 0.0
    market_price = row['MARK-PRICE']

    def f(sigma, S, K, T, r, market_price):
        if (flag=='C'):
            return bs_call(S, K, T, r, sigma) - market_price
        return bs_put(S, K, T, r, sigma) - market_price
    
    sigma_guess = 0.3

    try:
        # using newton-raphson to find the root
        sigma_imp = newton(f, sigma_guess, args=(S, K, T, r, market_price))
    except RuntimeError:
        # handle cases where convergence fails
        sigma_imp = 0.0

    return sigma_imp

file = input('Enter file path: ')
df = pd.read_csv(file)
df['IV'] = df.apply(iv, axis=1)
print(df['IV'])