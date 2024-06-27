### Quick Sort ###

def quickSort(x, low, high):
    if low < high:
        pi = partition(x, low, high)
        quickSort(x, low, pi - 1)
        quickSort(x, pi + 1, high)
    return x

def partition(x, low, high):
    pivot = x[high]
    i = low - 1

    for j in range(low, high):
        if x[j] <= pivot:
            i = i + 1
            x[i], x[j] = x[j], x[i]

    x[i + 1], x[high] = x[high], x[i + 1]
    return i + 1
    