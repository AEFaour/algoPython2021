def sortDivideConquer(xSet):

    if len(xSet) > 1:
        helfLen = len(xSet) // 2
        arrLeft = xSet[:helfLen]
        arrRight = xSet[helfLen:]

        sortDivideConquer(arrLeft)
        sortDivideConquer(arrRight)

        i=0
        j=0
        k=0

        while i < len(arrLeft) and j < len(arrRight):
            if arrLeft[i] < arrRight[j]:
                xSet[k] = arrLeft[i]
                i += 1
            else:
                xSet[k] = arrRight[j]
                j += 1
            k += 1

        while i < len(arrLeft):
            xSet[k] = arrLeft[i]
            i += 1
            k += 1

        while j < len(arrRight):
            xSet[k] = arrRight[j]
            j += 1
            k += 1

myArr = [11, 42, 8, 99, 36, 72, 0, 83, 54, 60]
print("Starting : ", myArr)
sortDivideConquer(myArr)

print("Result of sort : ", myArr)