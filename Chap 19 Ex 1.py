
user_dict = {'apple': "red",
             'lettuce': 'green',
             'lemon': 'yellow',
             'orange': 'orange'}
intruder = False
username = input("Please enter your name: ")
password = input("Please enter your password: ")

for user, pass_word in user_dict.items():
    if user == username and pass_word == password:
        intruder = True
        break
if intruder == True:
    print("Welcome Master")
else:
    print("INTRUDER ALERT")