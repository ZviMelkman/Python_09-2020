# Chapter 11 Exercise 6:
import random
from random import randint

num = randint(1, 100)
print(str(num))
t1 = "Your number is too small, guess again."
t2 = "Your number is too big, guess again."
guess = True
counter = 0
text_list = [t1, t2]

while guess:
    user_num = int(input("Please guess a number between 1 and 100: "))
    counter += 1
    # print("Counter: " + str(counter))
    if counter % 5 == 0:
        print(random.choice(text_list))
    else:
        if num > user_num:
            print(t1)
        elif num < user_num:
            print(t2)
        else:
            print("You guessed correct!!")
            guess = False
