def SEDV(xSet):
    myDict = dict()

    for xs in xSet:
        myDict[xs] = 0
    mySet = set(myDict.keys())

    print(mySet)

myArr = [2, 3, 4, 3, 8, 6, 8, 2, 3, 4, 9, 2, 5, 6, 8, 4, 7, 11, 12, 11, 10, 13, 0, 11, 1]

SEDV(myArr)