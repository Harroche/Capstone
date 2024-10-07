def calc(a,b):
    c = []
    d = []
    nValue = 0
    alen = len(a)-1
    for i in range(0, alen+1):
        nValue = nValue + a[i]
        c.append(nValue)
        
    for interval in b:
        value = 0
        if(interval[0] == 0):
            value = c[interval[1]]
        else:
            value = c[interval[1]] - c[interval[0]-1]
        d.append(value)
    return d