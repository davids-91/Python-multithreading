import operations
import time
import MyThread


start_time = time.perf_counter()

for x in range(3000):
    operations.random_numbers(1, 1000000)

end_time = time.perf_counter()

elapsed_time = end_time - start_time

print("Without using thread library: " + str(elapsed_time))


start_time = time.perf_counter()

for x in range(3000):
    MyThread.myThread(x).start()

end_time = time.perf_counter()

elapsed_time = end_time - start_time

print("Using thread library: " + str(elapsed_time))
