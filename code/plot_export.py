"""
This is used to export and save the response unit plots into the img/ directory as .png
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os

##### test plot #####

def savePlot(plotted, graph):
    
    directory = "../img/"
    graphic = os.path.join(directory, graph)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(plotted)

    ### default graphic is png format
    fig.savefig(graphic)

if __name__ == '__main__':
    
    test_plot = np.arange(25)
    test_graph = "mytest"
    
    savePlot(test_plot, test_graph)
