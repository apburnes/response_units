"""
This is used to export and save the response unit plots into the img/ directory as .png
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os

##### test plot #####

directory = "../img/"

def savePlot(a_plot, plot_name):
    
    plot_saved = os.path.join(directory, plot_name)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(plotted)

    ### default graphic is png format
    fig.savefig(plot_saved)

def plotXY(x, y):
    plt_name = "xy_sample_sites"
    plot_saved = os.path.join(directory, plt_name)

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.scatter(x,y)

    fig.savefig(plot_saved)


if __name__ == '__main__':
    
   ### test_plot = plt.plotnp.arange(25)
   ### test_graph = "mytest"
    
    savePlot()
    plotXY()
