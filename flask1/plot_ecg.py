import csv

threshold = 4.0


def load_from_file(filein):
    # initiate data
    t = 0.000
    time_list = []
    temp_plot1 = []
    temp_plot2 = []
    temp_plot3 = []
    temp_plot4 = []
    plot1 = []
    plot2 = []
    plot3 = []
    plot4 = []

    # open file
    with open(filein, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            data1 = int(row[0]) * 0.00019152753
            data2 = int(row[1]) * 0.00019152753
            data3 = int(row[2]) * 0.00019152753
            data4 = int(row[3])

            temp_plot1.append(data1)
            temp_plot2.append(data2)
            temp_plot3.append(data3)
            temp_plot4.append(data4)
            time_list.append(t)

            t = t + 0.008  # t = 0.008 because sampling rate = 125 sps = 1/125 second
            t = round(t, 3)  # round into decimal 3 points. TODO: Fix bug regarding t + 0.008 makes strange result
    # find average of each channel
    temp_plot1_avg = sum(temp_plot1) / len(temp_plot1)
    temp_plot2_avg = sum(temp_plot2) / len(temp_plot2)
    temp_plot3_avg = sum(temp_plot3) / len(temp_plot3)
    # processing ppg
    ppg_max = max(temp_plot4)
    ppg_min = min(temp_plot4)

    # for loop: assume plot 1, 2, 3, and 4 have same length
    for i in range(0, len(temp_plot1)):
        dev1 = temp_plot1[i] - temp_plot1_avg  # deviation
        dev2 = temp_plot2[i] - temp_plot2_avg  # deviation
        dev3 = temp_plot3[i] - temp_plot3_avg  # deviation

        if abs(dev1) < threshold:
            temp_plot1[i] = dev1 + 4  # 4 is the baseline
        else:
            temp_plot1[i] = 4
        if abs(dev2) < threshold:
            temp_plot2[i] = dev2  # 0 is the baseline
        else:
            temp_plot2[i] = 0
        if abs(dev3) < threshold:
            temp_plot3[i] = dev3 - 4  # -4 is the baseline
        else:
            temp_plot3[i] = -4
        # normalize PPG data
        temp_plot4[i] = (temp_plot4[i] - ppg_min) / (ppg_max - ppg_min)
        # convert to python dictionary
        plot1.append({'x': time_list[i], 'y': temp_plot1[i]})
        plot2.append({'x': time_list[i], 'y': temp_plot2[i]})
        plot3.append({'x': time_list[i], 'y': temp_plot3[i]})
        plot4.append({'x': time_list[i], 'y': temp_plot4[i]})
    # convert python dictionary to string
    plot_ch1 = str(plot1).replace('\'', '')
    plot_ch2 = str(plot2).replace('\'', '')
    plot_ch3 = str(plot3).replace('\'', '')
    plot_ppg = str(plot4).replace('\'', '')

    # return value
    return plot_ch1, plot_ch2, plot_ch3, plot_ppg
