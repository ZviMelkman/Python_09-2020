# Chapter 11 Exercise 5:
from random import randint
a = randint(1, 10)
b = randint(1, 10)
small_num = 0
big_num = 0
if a >= b:
    small_num = b
    big_num = a
else:
    small_num = a
    big_num = b
x = big_num
while x <= small_num*big_num:
    print("Small number is: " + str(small_num) + ". Big number is: " + str(big_num))
    if x % small_num == 0 and x % big_num == 0:
        print("Smallest common divider is: " + str(x))
        break
    x += 1
