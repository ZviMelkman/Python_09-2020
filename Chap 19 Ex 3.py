
comp_dict = {}
with open('hosts.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        (key, val) = line.split("=")
        comp_dict[key] = val
# print(comp_dict)
user_name = input("Please enter name: ")
user_id = False
i = 0
for k in comp_dict.keys():
    # print(k, comp_dict[k])
    if user_name == k:
        # print(f"User name: {k}; IP: {comp_dict[k]}")
        user_id = True
        i = k
        break
if i != 0:
    print(f"User name: {i}; IP: {comp_dict[i]}")
else:
    print("Sorry, no such user.")
