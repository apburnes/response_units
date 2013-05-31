
""" Handle Raster Data for Overlay and Segmentation """

#Import modules
import numpy as np
from numpy import ma
import pysal as ps
from numpy.random import randn
import pandas as pd
import matplotlib.pyplot as plt
from osgeo import gdal, ogr
from osgeo.gdalconst import *
import os, sys, time


def list_rasters(input_dir,file_type):
    """Creates a list of rasters from a defined directory and selected filetype."""
   
    raster_list = []
    
    for data in os.listdir(input_dir):
        if data.endswith(file_type):
            raster_list.append(data)
    return raster_list

def bands_to_array(raster)

    
if __name__ == '__main__':
    myTest()
