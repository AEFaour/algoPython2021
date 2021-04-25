def sortSelection(xSet):
    print("Starting : ", xSet)
    for i in range(len(xSet)-1):
        for j in range(i+1, len(xSet)):
            if xSet[i] > xSet[j]:
                y = xSet[j]
                xSet[j] = xSet[i]
                xSet[i] = y
            print("The sorting's state at step ({}-{}) is {}".format(i, j, xSet))

sortSelection([11, 42, 8, 99, 36, 72, 0, 83, 54,60 ])
