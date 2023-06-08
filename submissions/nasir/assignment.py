# Q5: Create an a list with dictionaries with the following information
#      Name, Age, Class, Subjects
#      each subject should have CA and Exam score
#      use console to print the following statement for at least two of the students.
#      NAME -----  AGE  ------  CLASS  ------ TOTAL
#      James ----- 10 --------  Jss One ----- 150.5
#      NOTE: there should be atleast 3 students and atleast 5 subjects each student.

# students = [
#     {
#         "name":"Nasir Mustapha", 
#         "age":16, 
#         "class":"Jss One A", 
#         "subjects":[
#         {"name":"Inter Science", "ca":20, "exam":46},
#         {"name":"Agric Science", "ca":15, "exam":56},
#         {"name":"PHE", "ca":25, "exam":26},
#         {"name":"Music", "ca":25, "exam":35},
#         {"name":"Civic Education", "ca":15, "exam":16}
#         ]
#         },
#     {
#         "name":"Bashir Haruna", 
#         "age":16, 
#         "class":"Jss One A", 
#         "subjects":[
#         {"name":"Inter Science", "ca":20, "exam":46},
#         {"name":"Agric Science", "ca":15, "exam":56},
#         {"name":"PHE", "ca":25, "exam":26},
#         {"name":"Music", "ca":25, "exam":35},
#         {"name":"Civic Education", "ca":15, "exam":16}
#         ]
#         },
#     {
#         "name":"Hattuna Dabo", 
#         "age":16, 
#         "class":"Jss One A", 
#         "subjects":[
#         {"name":"Inter Science", "ca":20, "exam":46},
#         {"name":"Agric Science", "ca":15, "exam":56},
#         {"name":"PHE", "ca":25, "exam":26},
#         {"name":"Music", "ca":25, "exam":35},
#         {"name":"Civic Education", "ca":15, "exam":16}
#         ]
#         }
# ]

# # print("NAME -----  AGE  ------  CLASS  ------ TOTAL")
# # total1 = students[0].get("subjects")[0].get("ca")+students[0].get("subjects")[0].get("exam")
# # total2 = students[0].get("subjects")[1].get("ca")+students[0].get("subjects")[1].get("exam")
# # total3 = students[0].get("subjects")[2].get("ca")+students[0].get("subjects")[2].get("exam")
# # total4 = students[0].get("subjects")[3].get("ca")+students[0].get("subjects")[3].get("exam")
# # total5 = students[0].get("subjects")[4].get("ca")+students[0].get("subjects")[4].get("exam")
# # finaltotal = total1+total2+total3+total4+total5
# # print("{} ----- {} --------  {} ----- {}".format(students[0].get("name"), students[0].get("age"), students[0].get("class"), finaltotal))

student = [
    {
        "name":"Aisha Auwal",
        "age":14,
        "class":"Primary 3",
        "subjects":[
            {"ca":25.4, "exam":45.5},
            {"ca":23.4, "exam":44.5},
            {"ca":22.4, "exam":43.5},
            {"ca":21.4, "exam":42.5},
            {"ca":24.4, "exam":41.5},
        ],
    },
    {
        "name":"Faisal Auwal",
        "age":14,
        "class":"Primary 3",
        "subjects":[
            {"ca":25.4, "exam":45.5},
            {"ca":23.4, "exam":44.5},
            {"ca":22.4, "exam":43.5},
            {"ca":21.4, "exam":42.5},
            {"ca":24.4, "exam":41.5},
        ],
    },
    {
        "name":"Abduwahab Auwal",
        "age":14,
        "class":"Primary 3",
        "subjects":[
            {"name":"Basic Science", "ca":25.4, "exam":45.5},
            {"name":"Inter Science","ca":23.4, "exam":44.5},
            {"name":"Agric Science","ca":22.4, "exam":43.5},
            {"name":"Primary Science","ca":21.4, "exam":42.5},
            {"name":"Home Economics","ca":24.4, "exam":41.5},
        ],
    },
]
print("NAME -----  AGE  ------  CLASS  ------ TOTAL")

name = student[0].get("name")
age = (student[0].get("age"))
Class = (student[0].get("class"))
ca = (student[0].get("subjects")[0].get("ca"))
exam = (student[0].get("subjects")[0].get("exam"))

print("{} ----- {} --------  {} ----- {}".format(name, age, Class, ca+exam))

name2 = student[1].get("name")
print(name2)
exam2 = student[1].get("subjects")[1].get("exam")
print(exam2)
age2 = student[1].get("age")
print(age2)
ca2 = student[1].get("subjects")[0].get("ca")
print(ca2)