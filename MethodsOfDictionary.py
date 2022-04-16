student = {
  "last_name": "Kujo",
  "name": "Jotaro",
  "year": 1970
}

student.clear()

print(student)

#--------------------------------------------------------------------#

student = {
  "last_name": "Kujo",
  "name": "Jotaro",
  "year": 1970
}
x = student.copy()

print(x)

#--------------------------------------------------------------------#

x = ('marks', 'roll_no', 'attendence')
y = 0

dictionary = dict.fromkeys(x, y)

print(dictionary)

#--------------------------------------------------------------------#

student = {
  "last_name": "Kujo",
  "name": "Jotaro",
  "year": 1970
}

x = student.get("name")

print(x)

#--------------------------------------------------------------------#

student = {
  "last_name": "Kujo",
  "name": "Jotaro",
  "year": 1970
}

x = student.items()

print(x)

#--------------------------------------------------------------------#

student = {
  "last_name": "Kujo",
  "name": "Jotaro",
  "year": 1970
}

x = student.keys()

print(x)

#--------------------------------------------------------------------#

student = {
  "last_name": "Kujo",
  "name": "Jotaro",
  "year": 1970
}

student.pop("last_name")

print(student)

#--------------------------------------------------------------------#

student = {
  "last_name": "Kujo",
  "name": "Jotaro",
  "year": 1970
}

student.popitem()

print(student)

#--------------------------------------------------------------------#

student = {
  "last_name": "Kujo",
  "name": "Jotaro",
  "year": 1970
}

x = student.setdefault("last_name", "Joestar")

print(x)

#--------------------------------------------------------------------#

student = {
  "last_name": "Kujo",
  "name": "Jotaro",
  "year": 1970
}

student.update({"Stand": "Star Platinum"})

print(student)

#--------------------------------------------------------------------#

student = {
  "last_name": "Kujo",
  "name": "Jotaro",
  "year": 1970
}
x = student.values()

print(x)
