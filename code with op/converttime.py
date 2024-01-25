import datetime as dt
import time
print("time.pref_counter()"+str(time.perf_counter()))
print("dt.datetime.now()="+str(dt.datetime.now()))
print("time.time()="+str(time.time()))
print("dt.datetime.now().time()"+str(dt.datetime.now().time()))
print("time.pref_counter()"+str(time.perf_counter()))
for i in range(100):
    pass
print("dt.datetime.now()="+str(dt.datetime.now()))
print("time.time()="+str(time.time()))
print("dt.datetime.now().time()"+str(dt.datetime.now().time()))
print("time.pref_counter()"+str(time.perf_counter()))






