empty_dict = {}
person = {"name" : "Raghav", "age": 38, "address" : "Farmington, MI"}
grades = dict(alice=95, bob=82, charlie =  92)

for name, score in grades.items():
    print(f" name -> {name} : score -> {score} ")
    print(grades[name], "Shiva")

print(grades.get("raju", "Unknown user"))

grades["Raju"] = 100
grades.update({"sampada" : 96})

print(grades.pop("bob"))

print(grades)

print(grades.keys())

print(grades.values())

print(grades.items())

print(grades.get("jagath", "Palya"))

more_grades = {"a" : 37, "b": 93}

grades.update(more_grades)
print(grades)
grades.update()

fruits = {"apple": 5, "banana" : 3, "apricot": 4}
print(fruits)
keys_view = fruits.keys()
print(keys_view)

fruits["orange"] = 7
print(fruits)


dict1 = {"a":1, "b":2, "d":4}
dict2 = {"d":4, "e":5, "f":6}

keys_dict1 = dict1.keys()
keys_dict2 = dict2.keys()

print(keys_dict1 & keys_dict2)
print(keys_dict1 | keys_dict2)
print(keys_dict1 - keys_dict2)

print("banana" in keys_view)

print(len(dict1))

print(f" before sorting :   {fruits}")
sorted_fruits = sorted(fruits)
print(f" after sorting :   {sorted_fruits}")

reverse_sorted_fruits =  sorted(fruits, reverse=True)
print(f"TTTTTTT    {reverse_sorted_fruits}")

#sort based on values

# print(f" !!!!!!!!!!! {fruits.get}")
#reverse_based_on_values = sorted(fruits, keys=fruits.get, reverse=True)
print(f" UUUUUU   {grades}")
sorted_by_grades = sorted(grades, key=grades.get, reverse=True)
print(f"******** {sorted_by_grades}")


myList = list[("delhi", "india"), ("washignton DC", "USA"), ("London", "UK")]

print(list)
myDict = dict(myList)
print(myDict)
