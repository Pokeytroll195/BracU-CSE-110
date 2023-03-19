user_list = []
for i in range(5):
    x = input()
    user_list.append(x)
user_list = user_list[::-1]

for i in range(5):
    print(user_list[i])
