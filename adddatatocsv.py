from collectdatafiles import getdata
import pandas as pd
import os
from datetime import datetime
import time

def addedcolumn(previousdf, newdf):
    added = False
    for column in newdf:
        if column not in previousdf:
            added = True
    return added


def getdataframelist(data):
    dataframelist = []
    for item in data:
        if dataframelist:
            if (dataframelist[-1])["Time"] == datetime.strftime(item[0], "%Y-%m-%d %H:%M:%S"):
                (dataframelist[-1])[item[1]] = item[2]
            else:
                dataframelist.append({'Time' : datetime.strftime(item[0], "%Y-%m-%d %H:%M:%S"), item[1] : item[2]})
        else:
            dataframelist.append({'Time' : datetime.strftime(item[0], "%Y-%m-%d %H:%M:%S"), item[1] : item[2]})
    return dataframelist

def uploadtocsv(datapath, csv):
    if os.path.exists(csv):
        curcsv = pd.read_csv(csv)
        lasttime = datetime.strptime(curcsv['Time'].iloc[-1], "%Y-%m-%d %H:%M:%S")

    
    else:
        lasttime = datetime.strptime('1970/05/26', "%Y/%m/%d") #Can modify if we only want data from a specific time back
    data = getdata(lasttime, datapath)
    dataframelist = getdataframelist(data)
    df = pd.DataFrame(dataframelist).iloc[:-1]
    if not os.path.exists(csv):
        df.to_csv(csv)
    else:
        df2 = pd.concat([curcsv.iloc[:, 1:], df],             # Append two pandas DataFrames
                        ignore_index = True,
                        sort = False)
        newcsv = addedcolumn(curcsv, df)
        if newcsv:
            df2.to_csv(csv)
        else:
            df = df2.iloc[len(curcsv):]
            df.to_csv(csv, mode='a', header=not os.path.exists(csv))

    while True:
        time.sleep(30)
        if not df.empty:
            lasttime = datetime.strptime(df.iloc[-1]['Time'], "%Y-%m-%d %H:%M:%S")
        data = getdata(lasttime, datapath)
        if data:
            dataframelist = getdataframelist(data)
            dftoadd = pd.DataFrame(dataframelist).iloc[:-1]
            newcsv = addedcolumn(df, dftoadd)  
            if newcsv:
                curcsv = pd.read_csv(csv)
                newcsvdf = pd.concat([curcsv.iloc[:, 1:], dftoadd],             # Append two pandas DataFrames
                        ignore_index = True,
                        sort = False)
                newcsvdf.to_csv(csv)
                df = newcsvdf.copy()

                
            else:
                df2 = pd.concat([df, dftoadd],             # Append two pandas DataFrames
                                ignore_index = True,
                                sort = False)
                dftoadd = df2.iloc[len(df):]
                dftoadd.to_csv(csv, mode='a', header=False) 
                if not dftoadd.empty:
                    df = dftoadd.copy()


uploadtocsv('Data/', 'extorrdata.csv')