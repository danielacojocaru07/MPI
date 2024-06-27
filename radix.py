### Radix Sort ###

def radixSort(x):
    k = len(str(max(x))) # nr. maxim de cifre pe care
                         # le pot avea numerele din tablou
    for i in range(k):
        x = counting(x, 9, i)
    return x

def counting(x, m, c):
    f = [] # frecventele cumulate asociate
    y = [] # tabloul auxiliar
    for i in range(m+1):
        f.append(0) # lista goala
                    # (cu 9 elemente de 0 --> 
                    # cifrele posibile din numar)
    for i in range(len(x)) :
        j = ((x[i] // pow(10, c)) % 10) #
        f[j] += 1
        y.append(0)
    for i in range(1, len(f)):
        f[i] = f[i-1] + f[i]
    for i in range(len(x)-1, -1, -1):
        j = (x[i] // pow(10, c)) % 10
        y[f[j]-1] = x[i]
        f[j] -= 1
    for i in range(len(x)):
        x[i] = y[i]
    return x
