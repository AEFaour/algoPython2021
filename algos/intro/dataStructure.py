
from collections import deque
MyList = [59, 17, 30, 68, 22, 45, 97, 10, 5, 38]

print(MyList)

print(MyList[0])

print(MyList[1])

MyList[1] = 19

print(MyList[1])

print(MyList)

for i in range(len(MyList)):
    print("Item", i + 1, "=", MyList[i])

sum = 0

for j in range(len(MyList)):
    sum += MyList[j]
    print(sum)

sum_1 = 0
k = 0
while k < (len(MyList) // 2):
    sum_1 += MyList[k]
    k = k + 1
print(sum_1)

###############################################################################################################

stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

print(stack)

item = stack.pop()

print("The deleted value is : ", item)

print(stack)

###############################################################################################################

myDeque = deque()

myDeque.append(1)
myDeque.append(2)
myDeque.append(3)
myDeque.append(4)
myDeque.append(5)

print(myDeque)

element =  myDeque.popleft()

print("The deleted value is : ", element)

print(myDeque)

###############################################################################################################

myDict = dict({"a" : 1, "b" : 2, "c" : 3, "d" : 4})
print(myDict)
print(myDict["d"])

mySecondDict = {}

mySecondDict["I"] = 1
mySecondDict["II"] = 2
mySecondDict["III"] = 3
mySecondDict["IV"] = 4
mySecondDict["V"] = 5

mySecondDict["II"] = "Hello World"
print(mySecondDict)