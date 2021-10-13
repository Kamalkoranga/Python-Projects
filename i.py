student_mail = ["kamal@school.com", "nakul@school.com", "rohit@school.com", "rajat@school.com", "rahul@school.com"]
print("-------------ST Lamart School------------")
email = input("Enter your school email id :- ")
if email == student_mail[0] :
    print(" Math           20\n Physics        15\n Chemistry      17\n English        14\n Computer       18")

elif email == student_mail[1] :
    print(" Math           18\n Physics        13\n Chemistry      19\n English        16\n Computer       16 ")

elif email == student_mail[2] :
    print(" Math           16\n Physics        15\n Chemistry      20\n English        18\n Computer       14 ")

elif email == student_mail[3] :
    print(" Math           17\n Physics        16\n Chemistry      15\n English        18\n Computer       14 ")

elif email == student_mail[4] :
    print(" Math           10\n Physics        16\n Chemistry      18\n English        16\n Computer       19 ")
    
else :
    print('Not Found !')