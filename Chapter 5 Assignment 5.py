

firstNum = int(input("Please enter an integer. "))
secondNum = int(input("Please enter another integer. "))
thirdNum = int(input("Please enter the last integer. "))

if(firstNum >= secondNum and firstNum >= thirdNum):
    print("The biggest number is: " + str(firstNum))
elif(secondNum >= thirdNum):
    print("The biggest number is: " + str(secondNum))
else:
    print("The biggest number is: " + str(thirdNum))

