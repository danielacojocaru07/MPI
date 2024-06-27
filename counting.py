### Counting Sort ###

def countingSort(x): # x - tablou de integers pozitive [1..++];
                     # m - integer;
    f = []
    y = []
    mx = max(x)
    for i in range(mx+1):
        f.append(0)
    for i in range(len(x)):
        f[x[i]] += 1
        y.append(0)
    for i in range(1, len(f)):
        f[i] = f[i-1] + f[i]
    for i in range(len(x)-1, -1, -1):
        y[f[x[i]]-1] = x[i]
        f[x[i]] -= 1
    for i in range(len(x)):
        x[i] = y[i]
    return x
