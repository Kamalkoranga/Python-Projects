a = 55
guess = int()
while guess != a :
    guess = int(input('Guess the number : '))
    if guess > a :
        print('You had choosen a little bit large number!')
    elif guess == a :
        print ("You got it ! That's a number ")
    else  :
        print ("You had choosen a small number ! ")

