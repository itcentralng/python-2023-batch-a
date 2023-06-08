# dictionaries are contained within
# curly braces
person = {"name":"Abdulwahab Hassan", "age":15, "hobbies":["Swimming", 'Eating']}

print(person)

person.clear()
print(person)

person2 = person.copy()

print(person2)

person3 = {"name":"Aisha Auwal", "age":35, "friend":"Shamsudeen Abdullahi"}
print(person3.get("name"))
print(person3.get("age"))
print(person3.get("friend"))

person4 = {"name":"Khauthar Yusuf", "age":3}
print(person4.get("name"))
print(person4.get("age"))

print(person4.items())
print(person4.keys())

person4.pop("name")
person4.pop("age")

print(person4)

person5={"name":"Aisha Auwal", "complexion":"brown"}
print(person5.get("complexion"))
print(person5.get("name"))

print(person5.popitem())
print(person5)

person5.setdefault("age", 35)

print(person5)

person5.setdefault("friend", "Shamsuddeen")

print(person5)

person5.setdefault("dob", "01-01-2005")
print(person5)
person5.setdefault("dob", "01-01-2009")
print(person5)

person5.update({"dob":"01-01-2009"})

print(person5)

person5.update({"name":"Abubakar Hassan"})

print(person5)

person5.update({"age":14})

print(person5)

person5.update({"friend":"Jamil Salis"})

print(person5)

print(person5.get("age"))
print(person5.get("dob"))
print(person5.get("name"))

person5.pop("age")

print(person5)

# QUICK RECAP
{"name":"Shamsu"}