
#Question 1

str = "I AM AN INTERN AT IT CENTRAL"
print(str.lower())
li = str.split()
print(li)
li.reverse()
print(li)
reverseStr = ' '.join(li)
print(reverseStr)

if str == reverseStr:
    print('The string is palindrome')
else:
    print('The string is not palindrome')



#Question 2


numbers = [1,3,2,7,9,10,4,7,8,1,6,5]
number=[]
for i in numbers:
    number.append(i*2)
print(number)


#Question 3

person = {'name':'Aminu', 'age':12, 'gender':'male'}
if person['age'] > 30:
    print(person.items())
else:
    print ("age not greater than 30")


