# Chapter 11 Exercise 2:
user_input = True
while user_input:
    age = input("Please enter your age. ")
    if age.isdigit():
        print("Your age is: " + str(int(age) * 12))
        user_input = False
