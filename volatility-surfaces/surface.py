import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 


def surface(file):
    df = pd.read_csv(file)
    
    # Extract data
    x = df['TIME-TO-EXPIRATION'].values
    y = df['IV'].values
    z = df['STRIKE-PRICE'].values

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
    ax.set_ylabel('IV')
    ax.set_zlabel('STRIKE-PRICE')
    
    plot_title = input('What is the plot title? ')
    
    plt.savefig(plot_title + '.png')
    plt.show()

file = input("What file would you like to use? ")
surface(file)