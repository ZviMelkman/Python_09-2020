# assignment 3:
Unum = int(input("Please enter an integer. "))
if (Unum % 7 == 0):
    print("Boom")
else:
    print("You number is not dividable by 7.")

# assignment 4:
Unum = int(input("Please enter an integer. "))
Vnum = Unum
if (Unum % 7 == 0):
    print("Boom")
while (Vnum >= 0):
    if(Vnum % 10 == 7):
        print("Boom")
        break
    else:
        b = Vnum / 10
else:
    print("You number is not dividable by 7 or contains the digit 7.")