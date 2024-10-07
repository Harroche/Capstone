def calc(a:list[int],b:list[list[int]])->list[int]:
    preSum = []
    retArr = []
    for num in a:
        if(len(preSum) != 0):
            preSum.append(preSum[len(preSum)-1]+num)
        else:
            preSum.append(num)
    for lo,hi in b:
        if(lo == 0):
            retArr.append(preSum[hi])
        else:
            retArr.append(preSum[hi]-preSum[lo-1])
    return retArr
