print('-------------------Password Manager---------------------')

data = []

while len(data) <= 5  :
    start = input("Add password ? \n(y) or (n) : ")
    if start == 'y' :
        name = input('Name: ')
        user_name = input('Username: ')
        user_password = input("Password: ")
        print("-----------Saved!")
        name_password = (user_name, user_password)
        data.append(name_password)
    else :
        break

check = input("Type 'show' to check saved passwords: ")
if check == 'show':
    print(data)