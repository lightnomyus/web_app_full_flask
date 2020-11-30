import csv


def load_from_file(filein):
    # initiate data
    t = 0.000
    plot1 = []
    plot2 = []
    plot3 = []
    plot4 = []

    # open file
    with open(filein, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            data1 = float(row[0]) + 8.0
            data2 = float(row[1]) + 4.0
            data3 = float(row[2])
            data4 = float(row[3]) - 4.0

            plot1.append({'x': t, 'y': data1})
            plot2.append({'x': t, 'y': data2})
            plot3.append({'x': t, 'y': data3})
            plot4.append({'x': t, 'y': data4})
            t = t + 0.008  # t = 0.008 because sampling rate = 125 sps = 1/125 second
            t = round(t, 3)  # round into decimal 3 points. TODO: Fix bug regarding t + 0.008 makes strange result
    plot_ch1 = str(plot1).replace('\'', '')
    plot_ch2 = str(plot2).replace('\'', '')
    plot_ch3 = str(plot3).replace('\'', '')
    plot_ppg = str(plot4).replace('\'', '')
    # return value
    return plot_ch1, plot_ch2, plot_ch3, plot_ppg
