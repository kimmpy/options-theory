import matplotlib.pyplot as plt
import pandas as pd

def data_analysis (file, message, x, y):
    df = pd.read_csv(file)
    subset_df = df.iloc[:rows]
    if type == 'Line' or type == 'line':
        plt.plot(subset_df[x], subset_df[y])
    elif type == 'Scatter' or type == 'scatter':
        plt.scatter(subset_df[x], subset_df[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(message)
    plt.show()

file = input('Enter file name: ')
message = ''
x = input('Enter x: ')
y = input('Enter y: ')
rows = int(input("How many rows do you want to show? "))
type = input("What type of graph do you want? ")
data_analysis(file, message, x, y)