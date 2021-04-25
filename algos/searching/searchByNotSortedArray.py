
def SBNSA(value, xSet):

    MinV = 0
    MaxV = len(xSet) - 1

    while MinV <= MaxV:

        half = (MinV + MaxV) // 2

        if xSet[half] == value:
            return half
        if value > xSet[half]:
            MinV = half + 1
        else:
            MaxV = half - 1
    if MinV > MaxV:
        return None

myArr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(SBNSA(1, myArr))
print(SBNSA(44, myArr))