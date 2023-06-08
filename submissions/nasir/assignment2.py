#Q1:
# Declare a variable called "string" and assign it a string
#  value. Use the lower() method to convert "string"
#  to lowercase, then use the split() method to create
#  a list of characters from "string" and use the reverse()
#  method to reverse the order of the characters in 
# the list. Finally, join the characters in the list 
# back together into a string and store the result in 
# a new variable called "reverse_string". Compare "string" 
# to "reverse_string" using conditional statement and output 
# "The string is a palindrome" if they are the same or 
# "The string is not a palindrome" if they are different.

str = "I AM AN INTERN AT IT CENTRAL"
str = str.lower()
li = str.split()
print(li)
li.reverse()
print(li)
reverseStr = ' '.join(li)
print(reverseStr)

if str == reverseStr:
    print('The string is palindrome')
if str != reverseStr:
    print('The string is not palindrome')

# Q2:
# Declare a list called "numbers" and initialize
#  it with a list of integers. Use the list index 
# to access each element and multiply it by 2. 
# Output the modified list.

numbers = [2, -7, 5]
numbers[0] = numbers[0]*2
numbers[1] = numbers[1]*2
numbers[2] = numbers[2]*2
print(numbers)

# Q3:
# Declare a dictionary called "person" with properties "name",
#  "age" and "gender". Use a conditional statement to 
# check if the age property is greater than 30, then 
# output the key-value pairs of the dictionary using the 
# dictionary properties.

person = {
    "name":"Abubakar Salis",
    "age":35,
    "gender":"Male"
}

if person.get("age") > 30:
    print(person.items())