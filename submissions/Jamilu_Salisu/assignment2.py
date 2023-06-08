# Create a folder with your name in the root of this project
# Create a new file within this folder and name it assignment2.js
# Answer the follwoing questions:

# Q1:
# Declare a variable called "str" and assign it a string value.
str = "I am learning Python"

# Use the toLowerCase() method to convert "str" to lowercase, then use the split() method to
# create a list of characters from "str" and use the reverse() method to reverse the order
# of the characters in the list.
str = str.lower()
str = str.split()
str = str.reverse()

# Finally, join the characters in the list back together into a string and store the result in
# a new variable called "reverseStr". Compare "str"
# to "reverseStr" using conditional statement and output
# "The string is a palindrome" if they are the same or
# "The string is not a palindrome" if they are different.

# Q2:
# Declare a list called "numbers" and initialize
#  it with a list of integers. Use the list index
# to access each element and multiply it by 2.
# Output the modified list.

num = [2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in num:
    num *= 2
    print(i)

# Q3:
# Declare a dictionary called "person" with properties "name",
#  "age" and "gender". Use a conditional statement to
# check if the age property is greater than 30, then
# output the key-value pairs of the dictionary using the
# dictionary properties.
