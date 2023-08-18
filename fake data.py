from datetime import datetime, timedelta
import numpy as np
now = datetime.now()
start = datetime.today() - timedelta(hours=24)
times = np.arange(start, now, timedelta(seconds = 1)).astype(datetime)
randomdatavalues = np.random.rand(len(times))*100
for x in range(len(times)):
    times[x] = datetime.strftime(times[x], "%Y-%m-%d %H:%M:%S")
times2 = np.array(times)
print(times2[0])
tocsv = np.column_stack((times2, randomdatavalues))
np.savetxt("fakedata.csv", tocsv, delimiter=",", fmt = '%s')
#np.savetxt("Data/fakedata" + now.strftime("%Y-%m-%d %H:%M:%S") + ".csv", tocsv, delimiter=",")