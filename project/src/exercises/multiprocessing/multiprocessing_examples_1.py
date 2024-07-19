import time
import multiprocessing
def task(sr_no):
    print(f"task {sr_no} started")
    time.sleep(1)
    print(f"task {sr_no} Completed")

start = time.time()

process1 = multiprocessing.Process(target=task, args=[1])
process2 = multiprocessing.Process(target=task, args=[2])

process1.start()
process2.start()

# join makes sure pur provcesse4s will finish before executing rest of the script
process1.join()
process2.join()

end = time.time()

print(f" The Execution time : {end - start:.2f} seconds")

import os

cpuCount = os.cpu_count()
print("Number of CPUs in the system:", cpuCount)




end = time.time()

print(f" The Execution time : {end - start:.2f} seconds")

import os

cpuCount = os.cpu_count()
print("Number of CPUs in the system:", cpuCount)


