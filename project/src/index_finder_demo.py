
#import index_finder


def find_index(to_search, target):
    for i, element in enumerate(to_search, 1):
        if element == target:
            return i
    return -1


courses = ["Math" ,"Art", "Physics", "CS"]

index = find_index(courses, "CS")
print(index)

