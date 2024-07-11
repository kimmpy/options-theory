import matplotlib.pyplot as plt
import pandas as pd

def data_analysis (file, message, x, y):
    df = pd.read_csv(file)
    subset_df = df.iloc[:1000]
    plt.plot(subset_df[x], subset_df[y])
    plt.title(message)
    plt.show()

file = input('Enter file name: ')
message = ''
x = input('Enter x: ')
y = input('Enter y: ')
data_analysis(file, message, x, y)