def sortBubble(xSet):
    print("Starting : ", xSet)
    for i in range(len(xSet)-1, 0, -1):
        for j in range(i):
            if xSet[j] > xSet[j+1]:
                y = xSet[j]
                xSet[j] = xSet[j+1]
                xSet[j+1] = y
            print("The sorting's state at step ({}-{}) is {}".format(i, j, xSet))

sortBubble([11, 42, 8, 99, 36, 72, 0, 83, 54, 60])