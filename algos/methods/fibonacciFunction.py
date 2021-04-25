def Fibonacci(x):
    if(x==0):
        return 0
    elif x ==1:
        return 1
    else:
        return Fibonacci(x-1) + Fibonacci(x-2)

for i in range(11):
    result = Fibonacci(i)
    print("{} : {}".format(i, result))