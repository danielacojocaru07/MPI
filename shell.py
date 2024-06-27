### Shell Sort ###

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
    