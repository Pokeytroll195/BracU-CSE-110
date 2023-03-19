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

if len(a_list) < 4:
    print("Not possible")
else:
    print(a_list[2:-2:])

