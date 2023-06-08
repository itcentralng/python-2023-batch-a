"""
Question1:List all the data types you know with examples 

String :- Any type of text within a "" or ''. Examples are; '100','Fatima',"13.44","18ift" and so on.

Integer :- Positive and negative whole numbers. Examples are; 10,-4,100,77 and so on.

Floats :- Numbers with decimal points. Examples are; 15.3,4.00,-5.55,0.23 and so on.

Boolean :- A datatype that can only result to either True or False.Examples are; True or False,True and True,
False or False,True and False.

List :-  A datatype that takes other datatypes in a [] seperated by comma.Examples are; [],[1,2,13.55,10.50,'a','b'],
['mango','apple','banana'],['jamilu','aisha'['zainab','rashida']] and so on.

tuple :- A datatype similar to list but functionally different(does not allow modification).Takes other datatypes in
a () seperated by comma.

Dictionary :- A datatype that carries a key with it's corresponding value in {}.Examples are; {1:'one',2:'two',3:'three'},
{'a':10,'b':12,'c':14,'d':16,'e':18,'f':20},{'fruit':'apple','carb':'rice','veg':'cabbage'}.




Question2: Read about variable naming convention in python and create examples of each


-A variable should start with a letter or an underscore. Examples are; num1, _shoppinglist, Age, name and so on.

-A variable name cannot start with a number. Examples are 1num, 90days, 7courses, 25thjanuary.

-A variable can only contan alpha-numeric characters and underscore. Examples are; subject1, _profile_, section7, no1_series.

-A variable can only be name cannot be a reserved name in python. Examples are; Type, print, class, and so on.

-Variables are case sensitive so Age is different from age.

-Variable cannot have whitespace in between them. Examples are; num 1, january 21st, first class, and so on
"""


#Question3: List 5 string methods with an example using print() in each case to print your result


form_method = "Hi, my name is {} and I'm an intern at {} and I'm learning {} ".format('Halima Abubakar','iT Central','Python')

print(form_method)

cent_method = 'HaLimA AbUbaKaR MauDe'

print(cent_method.casefold())

join_method = ' '.join(['This', 'is','a','python','assignment']) 

print(join_method)

up_method = 'we have a python class tomorrow in the morning and a meeting in the evening'

print(up_method.upper())

count_method = 'we have a python class tomorrow in the morning and a meeting in the evening'

print(count_method.count('a'))
print(count_method.count('e'))
print(count_method.count('i'))



#Question4: List 5 list methods with an example using print() in each case to print your result

grocery= ['sugar','tea','oil','milk','bread','tomatoes','spices','water','juice','pasta']
print(grocery)
grocery.reverse()
print(grocery)
grocery.append('meat')
grocery.append('eggs')
grocery.append('bread')
print(grocery)
grocery.sort()
print(grocery)
print(grocery.count('bread'))
grocery.clear()
print(grocery)

'''
Question5: Create a list with dictionaries with the following information;
Name, Age, Class, Subjects
each subject should have a CA and Exam score
use console to print the following statement for at least two of the students.
NAME -----  AGE ----- CLASS -----  TOTAL
NOTE: There should be atleast 3 students and atleast 5 subjects each student.
'''

Students_record = {'Name': ['Aminu','Fatima','Abdul'], 'Age': [16,14,15],'Class': ['Jss2','Jss1','Jss2'],
                   'Subjects': [{'English':[{'C.A':[24,15,20],'Exam':[65,40,53],'Total':[89,55,73]}],'Maths':[{'C.A':[24,15,20],'Exam':[65,40,53],'Total':[89,55,73]}],'Biology':[{'C.A':[24,15,20],'Exam':[65,40,53],'Total':[89,55,73]}],'chemistry':[{'C.A':[24,15,20],'Exam':[65,40,53],'Total':[89,55,73]}],'physics':[{'C.A':[24,15,20],'Exam':[65,40,53],'Total':[89,55,73]}]}]}
print (Students_record())
 











