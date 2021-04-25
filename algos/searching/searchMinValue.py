def FindMinMaxValues(xSet):

    MaxV = xSet[0]
    MinV = xSet[0]
    for i in range(len(xSet)):
        if(MaxV < xSet[i]):
            MaxV = xSet[i]

        if(MinV > xSet[i]):
            MinV = xSet[i]
    return print("min = {} and max = {}".format(MinV, MaxV))

myArr = [11, 42, 8, 99, 36, 72, 0, 83, 54, 60]

FindMinMaxValues(myArr)


