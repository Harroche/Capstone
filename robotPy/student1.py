def calc(A,B):
    c = A.copy()
    res = []
    for i in range(1,len(A)):
        c[i] = c[i-1]+c[i]
    for i in range(len(B)):
        if B[i][0] == 0:
            res.append(c[B[i][1]])
        else:
            res.append(c[B[i][1]]-c[B[i][0]-1])
    return res