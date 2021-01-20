import csv


def load_from_file(filein):
    # initiate data
    t = 0.000
    time_list = []
    plot1 = []
    plot2 = []
    plot3 = []
    temp_plot4 = []
    plot4 = []

    # open file
    with open(filein, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            # data1 = float(row[0]) + 8.0
            # data2 = float(row[1]) + 4.0
            # data3 = float(row[2])
            # data4 = float(row[3]) - 4.0
            data1 = int(row[0]) * 0.00019152753 + 1  # ADJUST THIS FORMULA TO ADJUST THE GRAPH SCALING
            data2 = int(row[1]) * 0.00019152753 - 181  # ADJUST THIS FORMULA TO ADJUST THE GRAPH SCALING
            data3 = int(row[2]) * 0.00019152753 - 197  # ADJUST THIS FORMULA TO ADJUST THE GRAPH SCALING
            # data4 = int(row[3]) * 0.01 - 23  # ADJUST THIS FORMULA TO ADJUST THE GRAPH SCALING
            data4 = int(row[3])

            plot1.append({'x': t, 'y': data1})
            plot2.append({'x': t, 'y': data2})
            plot3.append({'x': t, 'y': data3})
            temp_plot4.append(data4)
            time_list.append(t)

            t = t + 0.008  # t = 0.008 because sampling rate = 125 sps = 1/125 second
            t = round(t, 3)  # round into decimal 3 points. TODO: Fix bug regarding t + 0.008 makes strange result
    plot_ch1 = str(plot1).replace('\'', '')
    plot_ch2 = str(plot2).replace('\'', '')
    plot_ch3 = str(plot3).replace('\'', '')

    # processing ppg
    ppg_max = max(temp_plot4)
    ppg_min = min(temp_plot4)
    for i in range(0, len(temp_plot4)):
        temp_plot4[i] = (temp_plot4[i] - ppg_min) / (ppg_max - ppg_min)
        plot4.append({'x': time_list[i], 'y': temp_plot4[i]})
    plot_ppg = str(plot4).replace('\'', '')

    # return value
    return plot_ch1, plot_ch2, plot_ch3, plot_ppg
