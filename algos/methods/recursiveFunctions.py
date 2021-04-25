import time


def counting(x):
    if x == 0:
        print("NOK")
        return
    else:
        time.sleep(1)
        print(x)
        counting(x-1)
        print(x)

time.sleep(1)
counting(5)


def fact(x):
    if x > 0:
      if (x ==0):
         return 1
      else:
         return x * fact(x-1)

print("{} != {}".format(-5, fact(-5)))