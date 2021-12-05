# ------------------------------- Python lists----------------------- (they are changeable)

#friends = ['Kamal', 'Neha', 'Prince'] # list
# index =  0               1              2
#print(friends[-1]) # index
#print(friends[1]) # index
#print(friends[0:1]) # range
 
#friends[0] = 'Papa' # to modify value in list
#print(friends)

#-----------------------List Function-----------------------

#lucky_numbers = [34, 4, 8, 15, 16, 23, 42]
#friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 'Kamal', 'Kamal']
#friends.extend(lucky_numbers) # combine list at the end of one another
#friends.append('Kamal') # add another element in the end of the list
#friends.insert(1, 'Neha') # insert elements in any index position
#friends.remove('Kevin') # to remove an element
#friends.clear() # to remove every element of list
#friends.pop() # remove last element of list

#friends.sort() # sort the elements in alphabet order
#lucky_numbers.sort() #sort in ascending order

#print(friends.index('Karen')) # to find index position of element
#print(friends.count('Kamal')) # count the no of times of an element in
#lucky_numbers.reverse() # write in reverse format

#friends2 = friends.copy() #to copy the elemnts 
#print(friends2)
#print(friends)

#--------------Tuples -----------------

#coordinates = (34, 45) # __they are not changeable
#print(coordinates[1])

# ----------Functions-------------

#def say_hello() :
    #print("Hello Buddy!")  # def is a keyword , say_hello is a name
#print('HI')
#say_hello () # to execute function we have to call it
#print('How are you?')

#def friends(*name):    # name is parameter
  #  print('Hello ' + name[1])
    
#friends('kamal', 'nakul', 'rajat', 'raahul')    #kamal is argument
  
#def friends(name, age):   
#    print('Hello ' + name + ' , you are ' + str(age))
    
#friends('kamal',  45)

# ---------- Return Statement--------------

#def cube(num):
  #  return num*num*num # return is used to get information back and after this no code accepted

#result = cube(5)
#print(result)
  
  # -------if statement---------------------
  
#is_male = True
#is_tall = False
#if is_male and is_tall :  # or /and
  #    print('You are male or tall or both')
#elif is_male and not (is_tall):  # not is used to use negative of is-tall
#    print ('You are short male')
#elif not(is_male) and is_tall:
  #  print('You are not a male butyou\re tall')
#else :
  #  print('You are  not  a male and not  tall')

#-------------------if statement comparision

#def max_number(num1, num2, num3):
#   if num1 >= num2 and num1 >= num3 :
#    return num1
#  elif num2 >= num3 and num2 >= num1:
#    return num2
#  else:
#    return num3

#print(max_number(3, 4, 5))


#-------------------Advanced calculator

#num1 = float(input("Enter 1st number: "))
#num2 = float(input("Enter 2nd number: "))
#operator = input("Choose: \n (+) \n (-) \n (/) \n (*)")
#if operator == '+':
 #   print(num1 + num2)
#elif operator == '-':
#    print (num1 - num2)
#elif operator == '/':
 #   print(num1 / num2)
#elif operator == '*':
#    print(num1 * num2)
#else:
 #   print("You had choosen anything else!")

 #-----------Dictonaries

#data = {
#  "Kamal Singh" : "Mahesh Koranga, Asha Koranga, Jawhar Nagar", 
#  "Rahul" : "Kamala,  Harish"
#}

#print(data['Kamal Singh'])
#print(data['Rahul'])

#----------------While loop(guessing game)

secret_word = 'kamal'
limit = 0
guess =''
while limit < 3 and guess != secret_word:
  guess = input('Guess the word: ')
  if guess == secret_word :
    print("You got it")
  else :
    limit += 1
    if limit == 3 :
      print('You loose it')
    else :
      print('Try Again')
    

if guess != secret_word :
  print('You loose the game!')
else :
  print('You win the game!')