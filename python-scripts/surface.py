#-- Plot vol surfaces --#
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import sys


def surface(file, expiration, flag):
    df = pd.read_csv(file)

    # Filters rows based on expiration and flag
    df = df[df['EXPIRATION'] == expiration]
    df = df[df['P/C'] == flag]
    df = df[df['IV']!=0]

    # Extract data
    x = df['TIME-TO-EXPIRATION'].values
    y = df['STRIKE-PRICE'].values
    z = df['IV'].values

    # Ensure x, y, z have the same length
    assert len(x) == len(y) == len(z), "x, y, z arrays must have the same length"

    # Reshape x, y, z to 2D arrays
    x_unique = np.sort(np.unique(x))
    y_unique = np.sort(np.unique(y))
    X, Y = np.meshgrid(x_unique, y_unique)
    
    Z = np.zeros((len(y_unique), len(x_unique)))

    # Populate Z with corresponding z values
    for i in range(len(x)):
        xi = np.where(x_unique == x[i])[0][0]
        yi = np.where(y_unique == y[i])[0][0]
        Z[yi, xi] = z[i]

    fig = plt.figure(figsize=(14, 9))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the surface
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('TIME-TO-EXPIRATION')
    ax.set_ylabel('STRIKE-PRICE')
    ax.set_zlabel('IV')
    
    plot_title = input('What is the plot title? ')
    
    plt.savefig(plot_title + '.png')
    plt.show()
    print(f'Graph plotted successfully!')

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python surface.py <root_path> <expiration> <P/C>')
        sys.exit(1)
    
    path = sys.argv[1]
    expiration = sys.argv[2]
    flag = sys.argv[3]
    
    surface(path, expiration, flag)