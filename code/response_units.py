import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os

sample_points = pd.read_csv("./data/point_data.csv")

##### test plot #####

def savePlots(plotted, graph):
    ### filetype = ".png"
    ### directory = "./img/"
    ##graphic = os.path.join(directory, graph, filetype)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(plotted)
    fig.savefig(graph)

test_plot = np.arange(10)
test_graph = "test_graph"

savePlots(test_plot, test_graph)
