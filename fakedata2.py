from datetime import datetime, timedelta
import numpy as np
import csv
import random
import math
import time
name = "Data/MassSpecData-04439-" + datetime.strftime(datetime.now(), "%Y%m%d-%H%M%S") + ".csv"
f = open(name, 'w', newline = "")
writer = csv.writer(f)
start = time.time()
writer.writerow(["</ConfigurationData>"])
while True:
    f.close()
    time.sleep(1)
    f = open(name, 'a', newline = "")
    writer = csv.writer(f)
    a = random.random()
    if a < 0.15:
        writer.writerow([datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M:%S.%f"), str(998), str(0)])
    else:
        writer.writerow([datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M:%S.%f"), str(998), str(abs(math.sin(math.pi*int(time.time())/20)))])

    writer.writerow([datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M:%S.%f"), str(999), str(1.5*(math.e**(-1*(time.time()-start)/8)))])