from concurrent.futures import ProcessPoolExecutor, as_completed
import time

def task(sr_no):
    print(f"task {sr_no} started")
    time.sleep(1)
    print(f"task {sr_no} Completed")

start = time.time()

#executor.submit() submits a function to be executed and return a future object

with ProcessPoolExecutor() as executor:
    # a future object allows us to check the status of submitted function
    futures = [executor.submit(task, i) for i in range(5)]

# as_completed iterates over future objects and return them in order of completion
for f in as_completed(futures):
    f.result()

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


