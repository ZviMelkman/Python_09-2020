# Chapter 11 Exercise 3:
text_list = []
empty = True
while empty:
    user_text = input("Please enter your text: ")
    if user_text == "":
        empty = False
    else:
        text_list.append(user_text)
print(text_list[::-1])
