import time
import multiprocessing

processes = []

def task(sr_no):
    print(f"task {sr_no} started")
    time.sleep(1)
    print(f"task {sr_no} Completed")

start = time.time()

process1 = multiprocessing.Process(target=task, args=[1])
process2 = multiprocessing.Process(target=task, args=[2])

for i in range(10):
    process =  multiprocessing.Process(target=task, args=[i])
    processes.append(process)
    process.start()

# join the processes
for process in processes:
    process.join()

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


