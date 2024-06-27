### Merge Sort ###

def mergeSort(x):
    if len(x) > 1:
        m = len(x) // 2
        x1 = mergeSort(x[:m])
        x2 = mergeSort(x[m:])
        x = merge(x1, x2)
    return x

def merge(x1, x2):
    i = j = 0
    aux = []
    while (i < len(x1)) and (j < len(x2)):
        if x1[i] <= x2[j]:
            aux.append(x1[i])
            i += 1
        else:
            aux.append(x2[j])
            j += 1

    while i < len(x1):
        aux.append(x1[i])
        i += 1

    while j < len(x2):
        aux.append(x2[j])
        j += 1

    return aux
