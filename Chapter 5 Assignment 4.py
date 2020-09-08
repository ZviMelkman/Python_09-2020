# assignment 4:

user_num = int(input("Please enter an integer. "))
check = False
if user_num % 7 == 0:
    check = True
else:
    while user_num >= 1:
        if user_num % 10 == 7:
            check = True
            break
        user_num /= 10

if check:
    print("Boom")
else:
    print("Your number is not dividable by 7 or contains the digit 7.")
