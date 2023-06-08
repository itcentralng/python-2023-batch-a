def countToFive():
    print(1, 2, 3, 4, 5)

countToFive()

def isEven(number):
    print(number%2 == 0)

isEven(3)
isEven(4)

def sum(num1, num2):
    print(num1+num2)

sum(2, 12)
sum(12, 12)
sum(42, 12)

b = sum(1, 2)

print("B: ", b)

def greet(name="Halima"):
    print("Hello ", name)

greet()
greet("Aisha")


def sum(num1, num2):
    return num1+num2

a = sum(5, 4)

print(a+5)


def sayHello(person):
    print("Hello ", person)


people = ["Abdullahi", "Galadima", "Abduwahab", "Halima", "Aisha", "Jamil"]

for person in people:
    sayHello(person)

def sayHi():
    print("Hi")

sayHi()

def getFirstAndLast(listofnumbers):
    return [listofnumbers[0], listofnumbers[-1]]

firstlast = getFirstAndLast(people)

print(firstlast)

def register(name, age):
    if age < 18:
        return "You are too young register"
    if age > 30:
        return "You are too old register"
    return "Hi {} your registration was successful".format(name)

registration = register("Abubakar Galadima", 28)

print(registration)


# Quick Exercise
"""
Using the built in range function, 
Write a function that will print out
all even numbers within a certain range.
"""

def getEvenNumbersBetween(num1, num2):
    for num in range(num1, num2):
        if num % 2 == 0:
            print(num)

getEvenNumbersBetween(10, 16)
getEvenNumbersBetween(1, 10)

# Q2:
"""
Write a function that takes a string and returns
the string with every other character removed except
the english alphabets.
For example: cleanString('28DADA*1 <,MUSA') => DADAMUSA 
"""

def cleanString(chars):
    cleaned = ""
    alphabets = 'abcdefghijklmopqrstuvwxyz'
    for char in chars:
        if char.lower() in alphabets:
            cleaned += char
    return cleaned

def cleanString(chars):
    cleaned = ""
    for char in chars:
        if char.isalpha():
            cleaned += char
    return cleaned


print(cleanString('28DADA*1 <,MUSA'))

# Q3:
"""
Write a function that prints your name
"""

def mynameis():
    print("Nasir Mustapa")

mynameis()

def mynameis(name):
    print(name)

mynameis("Nasir Mustapha")

# Assignment

"""
Write a state and capital game
Users are prompted with a name of 
a state for which to provide the 
capital.
The games runs on an endless loop
until all the states have been used
or the user chooses to 'quit'

The whole game should start when a function 
is called. For example stateAndCapital() ==> game starts
"""

# More functions

def sumup(num1, num2):
    num3 = num1+num2
    print(num3)

def prints5():
    print(5)

def printNum(num=6):
    print(num)

def myname(name):
    print("I am ", name)

# QUICK RECAP
