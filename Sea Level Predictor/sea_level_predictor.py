import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    sealvl= pd.read_csv('epa-sea-level.csv')
    x = sealvl['Year']
    y = sealvl['CSIRO Adjusted Sea Level']
    # Create scatter plot
    fig, seaplot = plt.subplots()
    plt.scatter(x,y)

    # Create first line of best fit
    reg = linregress(x,y)
    x_pred = pd.Series([i for i in range(1881,2050)])
    y_pred = reg.slope*x_pred + reg.intercept
    plt.plot(x_pred,y_pred,'blue')


    # Create second line of best fit
    line2 = sealvl.loc[sealvl['Year'] >= 2000]
    line2_x = line2['Year']
    line2_y = line2['CSIRO Adjusted Sea Level']
    reg2 = linregress(line2_x,line2_y)
    x_pred2 = pd.Series([i for i in range(2000,2050)])
    y_pred2 = reg2.slope*x_pred2 + reg2.intercept
    plt.plot(x_pred2,y_pred2, 'red')

    # Add labels and title
    seaplot.set_title('Rise in Sea Level')
    seaplot.set_xlabel('Year')
    seaplot.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()