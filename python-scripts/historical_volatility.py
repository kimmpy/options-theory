#-- Prints out historical volatility using ADJ Close --#
import numpy as np
import pandas as pd

df = pd.read_csv('../index-data/DJI.csv')
close = df['ADJ CLOSE'].astype(float)

# Calculate daily logarithmic returns
log_returns = np.log(close / close.shift(1))

# Calculate mean of returns
mean_return = np.mean(log_returns)

# Calculate variance of returns
variance = np.var(log_returns, ddof=1)  # ddof=1 for sample variance

# Annualize the volatility (assuming 252 trading days in a year)
annual_volatility = np.sqrt(variance * 252)

print(f"Historical Volatility: {annual_volatility:.4f}")