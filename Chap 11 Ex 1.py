# Chapter 11 Exercise 1:
big_num = 0
for x in range(10):
    user_num = int(input("Please enter an integer. "))
    if user_num > big_num:
        big_num = user_num
print("The biggest number is: " + str(big_num))