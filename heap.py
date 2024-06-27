### Heap Sort ###

def heapify(x, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and x[i] < x[l]:
        largest = l
    if r < n and x[largest] < x[r]:
        largest = r

    if largest != i:
        x[i], x[largest] = x[largest], x[i]
        heapify(x, n, largest)

def heapSort(x):
    n = len(x)

    for i in range(n//2, -1, -1):
        heapify(x, n, i)

    for i in range(n-1, 0, -1):
        x[i], x[0] = x[0], x[i]
        heapify(x, i, 0)
    
    return x
    