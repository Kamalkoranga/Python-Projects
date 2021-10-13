import random
number = random.randrange(0, 100)
guess = int()
while guess != number :
    guess = int(input('Guess any number between 0 and 100: '))
    if guess == number :
        print ( 'Congratulation! You got it')
    elif guess > 100:
        print("You had choosen a bigger number than 100!")
    elif guess < number:
        print("You guessed a bit small number!")
    elif guess > number :
        print("You guessed a bit large number!")
    
    