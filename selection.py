### Selection Sort ###

def selectionSort(x): # x - tablou de numere
    for i in range(len(x)-1):
        k = i # we choose every element from the list
            # and we compare it with the others, until
            # we find the smallest from the subarray
            # and we swap their places
        for j in range(i+1, len(x)):
            if x[k] > x[j]:
                k = j
        if k != i:
            x[i], x[k] = x[k], x[i]
    return x
