import time


def task(sr_no):
    print(f"task {sr_no} started")
    time.sleep(1)
    print(f"task {sr_no} Completed")

start = time.time()

task(1)
task(2)

end = time.time()

print(f" The Execution time : {end - start:.2f} seconds")

import os

cpuCount = os.cpu_count()
print("Number of CPUs in the system:", cpuCount)


