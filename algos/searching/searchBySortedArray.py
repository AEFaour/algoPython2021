def SBSA(value, xSet):
    for i in range(0, len(xSet)):
        if value == xSet[i]:
            return [i, xSet[i]]
    return None

myArr = [11, 42, 8, 99, 36, 72, 0, 83, 54, 60]

print(SBSA(54, myArr))
print(SBSA(44, myArr))


