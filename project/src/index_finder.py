print("imported index finder module")

test_str = "Test String"

def find_index(to_search, target):
    for i, element in to_search:
        if element == target:
            return i
        return -1
