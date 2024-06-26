import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_predict = pd.Series([i for i in range(1880, 2051)]) # Range from 1880 to 2050
    y_predict = slope*x_predict + intercept
    plt.plot(x_predict, y_predict, 'r')

    # Create second line of best fit
    new_df = df[df['Year'] >= 2000] # Data from 2000 onwards
    new_slope, new_intercept, new_r_value, new_p_value, new_std_err = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    new_x_predict = pd.Series([i for i in range(2000, 2051)]) # Range from 2000 to 2050
    new_y_predict = new_slope*new_x_predict + new_intercept
    plt.plot(new_x_predict, new_y_predict, 'green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()
