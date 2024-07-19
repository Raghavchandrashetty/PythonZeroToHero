print("how you doing")
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print(squares)

# simple for loop
str = "india"
for x in numbers:
    print(x)

for x in str:
    print(x)

    # for loop with range
    for i in range(0,10,2):
        print(i)

# for loop with enumerate()
list1 = ["Work", "Hard", "Party", "Harder"]

for count, element in enumerate(list1):
    print(count+50 , element)

# nested for loops in python
for i in range(1,4):
    for j in range(1,4):
        print(i, j)

# loop over list
for word in list1:
    print(word)

# python for loop in one line
Numbers = [x for x in range(11)]
print(Numbers)

#Python for loop with dictionaries

dictionary = dict()
dictionary['master'] = 1
dictionary['qa'] = 2
dictionary['dev'] = 3

for ele in dictionary:
    print(ele, dictionary[ele])


# python for loop with tuples
tup = ((1, 2), (3, 4), (5,6))
for a,b in tup:
    print(a, b)