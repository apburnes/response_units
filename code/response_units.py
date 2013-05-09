"""
The response units code will cluster like samplesites to determine a response unit class.
The conservationist will be able to identify like ecological sites prior to visiting the ranch.
"""

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os
import plot_export as pe

sample_points = pd.read_csv("../data/point_data.csv")

myplot = np.arange(25)
mygraph = "test_graph"

pe.savePlot(myplot, mygraph)
