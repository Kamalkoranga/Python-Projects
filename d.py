#name = input('Enter your name: ')
#age = input('Enter your age: ')
#print('Hello ' + name + '!')
#print('Hello ' + name + '!' + ' You are  ' + age)

# ----------Basic  Calculator

#num1 = float(input('Enter 1st Number: '))
#num2 = float(input('Enter 2nd Number: '))
#result = num1 + num2
#print(result)

# ---------- Calculator
num1 = float(input('Enter 1st Number: '))
num2 = float(input('Enter 2nd Number: '))
operator = input('Select an Operator :-  \nAdd (+) \nSubract (-) \nDivision (/) \nMultiply (*)')
if operator == '+' :
    print (num1 + num2)
elif operator == '-' :
    print(num1 - num2)
elif operator == '/' :
    print(num1 / num2)
elif operator == '*' :
    print(num1 * num2)
else :
    print('Opps! you had not entered correct operator....')