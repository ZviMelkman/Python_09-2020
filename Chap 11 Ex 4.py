# Chapter 11 Exercise 4:
from random import randint

check = True
while check:
    num = randint(1, 1000000)
    if num % 7 == 0 and num % 13 and num % 15:
        print("The num: " + str(num) + " is dividable by 7, 13 and 15")
        check = False
    else:
        print("The number: " + str(num) + " is not a match")
