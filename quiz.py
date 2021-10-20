#-------------------------------Quiz App

score = 0

def quiz(guess, answer):

    chance = 0
    global score
    
    while chance < 3:
        
        if guess == answer:
            print("Yes, It's correct!")
            score += 1
            chance += 4
        
        else:
            if chance < 2:
                print("No, It's not correct")
                guess = input('Try Again: ')
                chance += 1
        
            else:
                print(f"The correct answer is {answer}")
                break
        
#---------------------------------------------Questions

q1 = input("Q1:- How many days in a week? ")
quiz(q1, '7')

q2 = input('Q2:- What is capital of India? ')
quiz(q2, 'Delhi')

q3 = input("Q3:- What is the height of Mt. Everest (in meter)? ")
quiz(q3, '8,848.86')

q4 = input("Q4:- How many countries in the world? ")
quiz(q4, '195')

q5 = input("Q5:- Who is the prime minister of India? ")
quiz(q5, 'Narendra Modi')

q6 = input('Q6:- Where is the headquater of Google situated? ')
quiz(q6, 'California')

q7 = input("Q7:- How many satellites in space? ")
quiz(q7, '1300')

q8 = input("Q8:- Which team won the cricket world cup in the year 2019? ")
quiz(q8, 'England')

q9 = input('Q9:- What does SWAN stand for? ')
quiz(q9, 'State Wide Area Network')

q10 = input("Q10:- The Noble Prize was started by which country? ")
quiz(q10, 'Sweden')

#----------------------------------------------result

print(f"Your result is {score} / 10 ")

if score <= 5:
    print(" You need to work hard :( ")
    
elif score < 10:
    print("Great, keep going!!")
else :
    print(' Excellent :) ')