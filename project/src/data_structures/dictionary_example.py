# dictionaries

student = {"name" : "Raghav", "age": 37, "courses" : ["Java", "Python"] }

for ele in student:
    print(ele)

student['phone'] = 9986796686
student['name'] = "Shetty"
print(student['courses'])
print(student.get('phone', "Not found"))
print(student.get('name'))

# update the values
student.update({'name': 'Jagath', 'age':38, 'courses' : ["Python", "QA"], 'address' :  'Swiss'})
print(student)

# delete a key
del student['age']
print(student)

# remove an element
name = student.pop('name')
print(name)

print(len(student))

print(student.items())
print(student['courses'][0])

for key, value in student.items():
    print(key, value)

    #help(student)

