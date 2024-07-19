# sets
cs_courses = {"software engineering", "logic design", "java", "python", "unix"}
bca_courses = {"software engineering", "logic design", "accounts", "electronics", "unix"}

print(cs_courses.union(bca_courses))
print(cs_courses.intersection(bca_courses))
print(cs_courses.difference(bca_courses))


# create empty set

my_set = set()

fruits = {"banana", "apple", "cherry"}
nums = set([1, 12, 3, 34, 5])
mixed_set = {24, "raghav", "Shivamogga"}

print(fruits)

for num in nums:
    print(f"*** : {num}")

print(mixed_set)

set1 = {1, 2, 3}
set2 = {4, 5, 3}

union_set = set1.union(set2)
print(union_set)

intersection_set = set1.intersection(set2)
print(intersection_set)


difference_set1 = set1.difference(set2)
print(difference_set1)


difference_set2 = set2.difference(set1)
print(difference_set2)