alist = ["Coke", "Jam", "Ice"]

alist.append("Sprite")

print(alist)

# alist.clear()

# print(alist)

blist = alist.copy()

print(blist)

alist.append("Fried Rice")

print(alist)
print(blist)

clist = alist

alist.append("Beans")

print(alist)
print(clist)

print(alist.count("Sprite"))

alist.extend(blist)
print(alist)
alist.extend("abdul")
print(alist)

print(alist.insert(0, "Jama"))

print(alist)

alist.pop(0)
print(alist)
alist.pop()
alist.pop()
alist.pop()
alist.pop()
alist.pop()
print(alist)

alist.remove("Coke")
print(alist)

# QUICK RECAP
people = ["Halima", "Shamsu"]
