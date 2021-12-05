print ('----------Sign Up Page -----------')
name = input('Name : ')
email = input('Email : ')

password1 = ''
while len(password1)  < 6 :
    password1 = input('Password: ')
    if len(password1) < 6 :
        print('----------Enter password bigger than 6 digits!----------')
    else :
        password2 = ''
        while password2 != password1:
            password2 = input('Confirm Password: ')
            if  password1 == password2 :
                print('----------Congrats! You have successfully signed up ...----------')
            else :
                print('----------Password didn\'t match!----------')

