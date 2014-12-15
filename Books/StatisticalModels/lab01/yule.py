"""
Solution to Freedman, Statistical Models, lab 1, pp. 295f.

Copyright (c) 2014 Marshall Farrier

Distribution and use of this software without prior written permission
of the authors is strictly prohibitied and will be prosecuted to
the full extent of the law.

by

Marshall Farrier, marshalldfarrier@gmail.com
"""

import matplotlib.pyplot as plt
import pandas as pd

def load_file():
    fname = '../docs/yuledoc.txt'
    data = pd.read_table(fname, sep=' ', skiprows=4, index_col=False,
            header=None, names=['Paup', 'Out', 'Old', 'Pop'])
    return data

def get_deltas(data):
    return data - 100

def prob01():
    """
    Means:
    Paup   -49.65625
    Out    -74.84375
    Old     -0.81250
    Pop     19.96875
    dtype: float64
    SDs:
    Paup    16.487746
    Out     12.796445
    Old      9.106671
    Pop     30.247884
    dtype: float64
    """
    deltas = get_deltas(load_file())
    print("Means:")
    print(deltas.mean(axis=0))
    print("SDs:")
    print(deltas.std(axis=0))

def prob02():
    """
              Paup       Out       Old       Pop
    Paup  1.000000  0.594032  0.395294 -0.593433
    Out   0.594032  1.000000  0.108806 -0.012238
    Old   0.395294  0.108806  1.000000 -0.528132
    Pop  -0.593433 -0.012238 -0.528132  1.000000
    """
    deltas = get_deltas(load_file())
    print(deltas.corr())

def prob03():
    deltas = get_deltas(load_file())
    deltas.plot(x='Paup', y='Out', kind='scatter')
    plt.show()
    plt.close()

def prob04():
    """ (0.76538885366199017, 7.6283220162645762, 13.263420212711734) """
    deltas = get_deltas(load_file())
    r = deltas.iloc[:, :2].corr().loc['Paup', 'Out']
    s_x = deltas.loc[:, 'Out'].std()
    s_y = deltas.loc[:, 'Paup'].std()
    xbar = deltas.loc[:, 'Out'].mean()
    ybar = deltas.loc[:, 'Paup'].mean()
    slope = r * s_y / s_x
    intercept = ybar - slope * xbar
    # SD of residuals
    residuals = deltas.loc[:, 'Paup'] - intercept - slope * deltas.loc[:, 'Out']
    return slope, intercept, residuals.std()
