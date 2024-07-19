"""
List = mutable
Remove,pop,insert,append,extend,join,split,max,min,sum,sorted,sort
Tuple= immutable
Sets= used as membership checker
Doesn't allow duplicate data
Union, difference, intersection
"""

print("inside lists, tuples, sets examples")

courses = ["History", "Math", "Physics", "Computer_Science"]

print(len(courses))
print(courses)
print(courses[0])
# last element
print(courses[3])

# last element by negative index
print(courses[-1])

# display range of values
print(" display range of values")
print(courses[:2])
print(courses[0:2])

print(courses[2:])

# add an element to the end of the list
print("add an element to the end of the list")

#courses.append("Art")

print(courses)
courses.insert(0, "Art")
print(courses)

courses2 = ["Art", "Education"]
courses3 = ["Business", "Sports"]

courses2.append(courses)
courses3.extend(courses)
print(courses2)
print(courses2[0])
print(courses2[2][0])
print(courses3)

# removing values from a list
courses.remove('Math')
print(courses)
courses.pop()
popped = courses.pop()
print(popped)

# reverse the list
courses.reverse()
print(courses)

friends = ["Raghav", "Shivu", "Abhijith", "Deepthi", "samapda", "sushmitha", "Jagath", "Shabarish"]
print(friends)
friends.reverse()
print(friends)

friends.sort()
print(friends)

nums = [1, 20, 13, 4, 5, 7,17 ]
print(nums)
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

courses = ["History", "Math", "Physics", "Computer_Science"]
sorted_courses = sorted(courses)
print(courses)
# min , max, sum on the list

print(max(nums))
print(min(nums))
print(sum(nums))

#print(help(nums))

print(courses.index('Physics'))
print(courses.index('Physics'))
print('Math' in courses )

# print the elements in the list
for course in courses:
    print(course)

# using enumerate for index and element
for index, course in enumerate(courses, start=1):
    print(index, course)

# joining the list elements by a delimiter

courses_string = '$$$'.join(courses)
print(courses_string)

new_list = courses_string.split("$$$")
print(new_list)


#creating empty list
empty_tuple = []
empty_tuple = list()


