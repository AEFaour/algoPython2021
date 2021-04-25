def Split(xSet, i, j):
    axe = xSet[i]
    MinV = i+i
    MaxV = j
    Bool = False

    while Bool == True:
        while MinV <= MaxV and xSet[MinV] <= axe:
            MinV += 1

        while xSet[MaxV] >= axe and MaxV >= MinV:
            MaxV -= 1

        if MaxV < MinV:
            Bool = True
        else:
            y = xSet[MinV]
            xSet[MinV] = xSet[MaxV]
            xSet[MaxV] = y

    y = xSet[i]
    xSet[i] = xSet[MaxV]
    xSet[MaxV] = y

    return MaxV




def sortQuick(xSet, i, j):
    if i < j:
        markPoint = Split(xSet, i, j)

        sortQuick(xSet, i, markPoint -1)
        sortQuick(xSet, markPoint +1, j)


myArr = [11, 42, 8, 99, 36, 72, 0, 83, 54, 60]
print("Starting : ", myArr)
sortQuick(myArr, 0, len(myArr)-1)

print("Result of sort : ", myArr)