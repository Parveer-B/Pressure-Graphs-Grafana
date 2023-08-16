import os
import csv
from datetime import datetime
outputpath = "data/" #location of output files
files = os.listdir(outputpath)
print(files[-1])

with open(outputpath + files[-1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    times = []
    for row in csv_reader:
        times.append(row)
datestring = times[-1][0]
dt_object1 = datetime.strptime(datestring, "%Y/%m/%d %H:%M:%S.%f")
print(dt_object1)
        