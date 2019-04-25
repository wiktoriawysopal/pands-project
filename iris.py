# Wiktoria Wysopal, 22/04/2019
# Iris Data Set analysis

#Importing packages such as Numpy, Pandas and Matplot to calculate statistics and create graphs 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Loading the iris data set for analysis
data = np.genfromtxt('iris.txt', delimiter=",")
