def IfSorted(xSet):
    for i in range(0, len(xSet)-1):
        if (xSet[i] > xSet[i +1]):
            return "The array is not Sorted"
    return "The array is Sorted"

arrayX= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arrayY = [5, 0, 9, 2, 4, 6, 7, 1, 8, 3]

print(IfSorted(arrayX))
print(IfSorted(arrayY))