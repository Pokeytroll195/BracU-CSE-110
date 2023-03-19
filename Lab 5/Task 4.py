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

f_list = []

for i in range(len(a_list)):
    f_list.append(int(a_list[i]) ** 2)

print(f_list)