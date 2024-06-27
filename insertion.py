### Insertion Sort ###

def insertionSort(x): # x - tablou de numere
    for i in range(1, len(x)):
        aux = x[i]
        j = i - 1
        while (j >= 0) and (aux < x[j]):
            x[j+1] = x[j]
            j -= 1
        x[j+1] = aux

    return x
