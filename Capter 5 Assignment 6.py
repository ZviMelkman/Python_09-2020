
firstNum = int(input("Please enter an integer. "))
difference = int(input("Please enter the difference. "))
sequence = int(input("Please enter the sequence. "))
sum = firstNum

for x in range(0, sequence):
    sum = sum + difference
    print(sum)
