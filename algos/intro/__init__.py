str = input("Enter your number, please : ")
x = int(str)
y = 1
for z in range(2, x + 1):
    print(z)
    y *= z
print(x, "! = ", y)


