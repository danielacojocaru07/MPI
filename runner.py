from timeit import default_timer as timer
import random

# Add here the sorting algorithm
def shellSort(x):
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    n = len(x)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = x[i]
            j = i
            while j >= interval and x[j - interval] > temp:
                x[j] = x[j - interval]
                j -= interval

            x[j] = temp
        interval //= 2
    return x

x = []
for i in range(100000000): # set the number of elements in the set
    x.append(random.randint(-100, 100))

start = timer()
x = shellSort(x)
end = timer()
print("Execution Time:", round(end - start, 10), "seconds")
