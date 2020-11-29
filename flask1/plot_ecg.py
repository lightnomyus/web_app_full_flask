import csv
import numpy as np


def load_from_file(filein):
    # change grid
    x_major = np.arange(0, 60.01, 0.2)  # Major Grid = 0.2 second
    x_minor = np.arange(0, 60.01, 0.04)  # Minor Grid = 0.04 second
    y_major = np.arange(-1, 1.6, 0.5)  # Major Grid = 0.5 mV
    y_minor = np.arange(-1, 1.6, 0.1)  # Major Grid = 0.1 mV

    # initiate data
    xs = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    t = 0.000

    # open file
    with open(filein, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            data1 = float(row[0])
            data2 = float(row[1])
            data3 = float(row[2])
            data4 = float(row[3])
            xs.append(float(t))
            y1.append(float(data1))
            y2.append(float(data2))
            y3.append(float(data3))
            y4.append(float(data4))
            t = t + 0.008  # t = 0.008 because sampling rate = 125 sps = 1/125 second
            t = round(t, 3)  # round into decimal 3 points. TODO: Fix bug regarding t + 0.008 makes strange result

    # return value
    return xs, y1, y2, y3, y4
