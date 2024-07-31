#-- Plots scatter plot with date for X-axis -- #
#-- Use merged flex index csvs --#
import pandas as pd
import matplotlib.pyplot as plt
import sys

def plot_strike_iv_time(file_path, plot_title, expiration, time, flag):
    df = pd.read_csv(file_path)

    # Filters for rows for matching expiration/time-to-expiration/flag
    df = df[df['EXPIRATION']==expiration]
    df = df[df['TIME-TO-EXPIRATION']==time]
    df = df[df['P/C']==flag]

    # Extract columns
    x = df['STRIKE-PRICE']
    y = df['IV']

    # Create scatter plot
    plt.figure(figsize=(20, 12))
    plt.scatter(x, y, marker='o')
    plt.plot(x, y, marker='o')

    # Formatting
    plt.title(plot_title)
    plt.xlabel('STRIKE-PRICE')
    plt.ylabel('IV')

    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(15))  # Adjust the number of ticks shown

    plt.tight_layout()
    plt.grid(True)
    plt.show()

    print(f'Graph plotted successfully!')

if __name__ == '__main__':
    if len(sys.argv) != 6:
        print('Usage: python plot_strike_iv.py <root_path> <title> <expiration> <time-to-expiration> <P/C>')
        sys.exit(1)
    
    path = sys.argv[1]
    title = sys.argv[2]
    expiration = sys.argv[3]
    time = int(sys.argv[4])
    flag = sys.argv[5]
    
    plot_strike_iv_time(path, title, expiration, time, flag)