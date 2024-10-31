from random import randint

def check_calc(a,b):
    n = len(a)
    c = [0] * n
    d = [0] * n
    c[0] = a[0]
    for i in range(1,n):
        c[i] += a[i] + c[i-1]
    for i in range(n):
        if b[i][0] - 1 >= 0:
            d[i] = c[b[i][1]]- c[b[i][0] - 1]
        else:
            d[i] = c[b[i][1]]
    return d