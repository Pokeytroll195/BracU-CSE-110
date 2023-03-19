n = input("Enter your list: ")
new_text = ''
add = ''
a_list = []

for i in n:
    if i != ',':
        new_text += i
    else:
        pass
for i in new_text:
    if i != ' ':
        add += i
    else:
        a_list.append(add)
        add = ''
a_list.append(add)

for i in range(len(a_list)):
    if int(a_list[i]) == int(a_list[0]):
        max_number = int(a_list[0])
        max_cap = i
    else:
        if int(a_list[i]) > max_number:
            max_number = int(a_list[i])
            max_cap = i
print(f"My list: {a_list}")
print(f"Largest number in the list is {max_number} which was found at index {max_cap}")