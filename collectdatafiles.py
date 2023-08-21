import os
from datetime import datetime, timedelta
import csv
def collectfiles(lasttime, path): #lastime is a datetime object, collect all relevant data files
    files = os.listdir(path)
    for index, file in reversed(list(enumerate(files))):
        a = str(file).replace('.', '-')
        a = str(a).split('-')
        time = datetime.strptime(" ".join(a[2:4]), "%Y%m%d %H%M%S")
        if time < (lasttime + timedelta(seconds = 1)):
            return files[index:]
    return files

def convertt(value):
    if int(float(value))== 999:
        return "Total Pressure"
    elif int(float(value)) == 998:
        return "Pirani Pressure"
    return str(int(float(value)))


def getdata(lasttime, datapath):
    files = collectfiles(lasttime, datapath)
    pastlasttime = False
    data = []
    for file in files:
        atdata = False
        masssweep = False
        with open(datapath + file) as csv_file:
            csv_data = list(csv.reader(csv_file, delimiter=','))
            for row in csv_data:
                if row:
                    if "<?xml" in row[0]: 
                        atdata = False
                    elif "Mode=\"Trend\"" in row[0]:
                        masssweep = False
                    elif "Mode=\"Mass sweep\"" in row[0]:
                        masssweep = True
                if masssweep == True:
                    continue
                if atdata:
                    rowtime = datetime.strptime(row[0], "%Y/%m/%d %H:%M:%S.%f").replace(microsecond=0)
                    if not pastlasttime:
                        if rowtime > lasttime:
                            pastlasttime = True
                    if pastlasttime:
                        data.append([rowtime, convertt(row[1]), row[2]])

                elif row:
                    if "</ConfigurationData>" in row[0]:
                        atdata = True
                    
    return data

a = getdata(datetime.strptime('2023/08/16 10:28:26', "%Y/%m/%d %H:%M:%S"),'Data/')
Mode="Trend"
Mode="Mass sweep"