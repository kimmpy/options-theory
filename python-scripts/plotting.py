"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../index-data/DJI.csv')

dates = df['DATE']
volumes = df['VOLUME']

plt.figure(figsize=(12, 6))

plt.plot(dates, volumes, marker='o', linestyle='-')

plt.title('Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.xticks(rotation=45)
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(6))

plt.tight_layout()
plt.grid(True)
plt.show()

"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def data_with_date(file_path, plot_title, symbol, column):
    
    df = pd.read_csv(file_path)
    df = df[df['SYMBOL'].str.contains(symbol)]

    #-- extract columns --#
    dates = df['DATE']
    data = df[column]

    # Create scatter plot
    plt.figure(figsize=(20, 12))
    plt.scatter(dates, data, marker='o')

    plt.title(plot_title)
    plt.xlabel('DATE')
    plt.ylabel(column)

    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(15))  # Adjust the number of ticks shown

    plt.tight_layout()
    plt.grid(True)
    plt.savefig(plot_title + '.png')
    plt.show()


file_path = input("Enter file path: ")
plot_title = input("Enter plot title: ")
symbol = input("Enter symbol: ")
column = input("Enter column: ")
data_with_date(file_path, plot_title, symbol, column)