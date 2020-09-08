# assignment 4:

user_num = int(input("Please enter an integer. "))

if user_num / 7 == 0:
    print("Boom")
else:
    while user_num >= 1:
        if user_num % 10 == 7:
            print("Boom")
            break
        user_num /= 10
    print("You number is not dividable by 7 or contains the digit 7.")
