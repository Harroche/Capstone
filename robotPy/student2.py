def calc(a,b):
    
    length = len(a)
    C = [None] * length 
    D = [None] * length

    #C erstellen
    C[0] = a[0]
    for i in range(1, length):
        C[i] = a[i]+C[i-1]

    for i in range(0, length):
        if b[i][0]-1 < 0:
            D[i] = C[b[i][1]]
        else:
            D[i] = C[b[i][1]] - C[b[i][0]-1]
    return D