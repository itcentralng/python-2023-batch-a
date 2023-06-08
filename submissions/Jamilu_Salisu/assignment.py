
# Q1: Using comments, list all the data types you know with examples

# String
name = "Jamilu Salisu"

# Integer
age = 24

# Float
sallary = 99.99

# Boolean
isHealthy = True

# List
skills_learning = ["Python", "Flask", "Dart", "Flutter", "Clound Computing"]

# Dictionary
intern_profile = {"name": "Jamilu Salisu",
                  "institution": "BUK", "department": "SWE", "level": 300, "duration": "6 months"}

# Tuple
skills = ("PHP", "Javascript", "HTML", "CSS", "Angurlar", "Flutter")

# Set
hobbies = {"Coding", "Watching Anime", "Reading Comics", "Networking"}


# Q2: Read about variable naming convention in python and create examples of each

# (i) variable name must start with a letter or the underscore character
firstname = "Jamilu"
_othername = "Mohammed"

# (ii) variable name cannot start with a number
# 2lastname = "Salisu" # an error will occur

# (iii) variable name can only contain alpha-numeric characters and underscores(A-z, 0-9, and _)
full_name1 = "Jamilu Salisu"

# (iv) variable names are case-sensitive
height = 1.50
Height = 1.60
HEIGHT = 1.75


# Q3: List 5 String methods with an example using print() in each case to print your result

# split the string into a list
print(name.split())

# convert the string to uppercase
print(firstname.upper())

# replace a word in the string
print(name.replace("Jamilu", "Mohammed"))

# format the string
print("I am {} years old and I earn {}$ per month.".format(
    age, sallary))

# count the number of times a word appears in the list
print("I am learning Flutter and Python.".count("am"))

# Q4: List 5 List methods with an example using print() in each case to print your result


# Q5: Create an a list with dictionaries with the following information
#      Name, Age, Class, Subjects
#      each subject should have CA and Exam score

interns_scores = [
    {"name": "Jamila", "age": 20, "class": "SS One",
     "subjects": [
         {"course": "Dart", "CA": 25, "Exam": 55},
         {"course": "Flutter", "CA": 19, "Exam": 39},
         {"course": "Python", "CA": 27, "Exam": 40},
         {"course": "Flask", "CA": 30, "Exam": 52},
         {"course": "Cloud Computing", "CA": 22, "Exam": 53}
     ]},
    {"name": "Abdulaziz", "age": 24, "class": "Jss Two",
     "subjects": [
         {"course": "Dart", "CA": 21, "Exam": 44},
         {"course": "Flutter", "CA": 8, "Exam": 33},
         {"course": "Python", "CA": 25, "Exam": 58},
         {"course": "Flask", "CA": 17, "Exam": 47},
         {"course": "Cloud Computing", "CA": 22, "Exam": 53}
     ]},
    {"name": "Hauwa'u", "age": 19, "class": "SS Three",
     "subjects": [
         {"course": "Dart", "CA": 19, "Exam": 44},
         {"course": "Flutter", "CA": 22, "Exam": 53},
         {"course": "Python", "CA": 27, "Exam": 38},
         {"course": "Flask", "CA": 26, "Exam": 49},
         {"course": "Cloud Computing", "CA": 29, "Exam": 58}
     ]}
]

#      Calculate the total score for each student and print the result
#      use console to print the following statement for at least two of the students.
#      NAME -----  AGE  ------  CLASS  ------ TOTAL

#      James ----- 10 --------  Jss One ----- 150.5

#      NOTE: there should be atleast 3 students and atleast 5 subjects each student.
