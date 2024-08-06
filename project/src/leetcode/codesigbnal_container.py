from bisect import bisect_right

queries = [["ADD","0"],
 ["ADD","1"],
 ["ADD","1"],
 ["ADD","11"],
 ["ADD","22"],
 ["ADD","3"],
 ["ADD","5"],
 ["GET_NEXT","0"],
 ["GET_NEXT","1"],
 ["REMOVE","1"],
 ["GET_NEXT","1"],
 ["ADD","0"],
 ["ADD","1"],
 ["ADD","2"],
 ["ADD","1"],
 ["GET_NEXT","1"],
 ["GET_NEXT","2"],
 ["GET_NEXT","3"],
 ["GET_NEXT","5"]]

def solution(queries):
    # print(queries)
    new_elements = []
    result = []

    def get_next(value):
        index = bisect_right(new_elements, value)
        return str(new_elements[index]) if index < len(new_elements) else ""


    for i in range(len(queries)):
        # print(f" i : {i}  element : {queries[i][0]} : {queries[i][1]}" )
        if queries[i][0] == "ADD":
            new_elements.append(queries[i][1])
            sorted(new_elements)
            result.append("")
        elif queries[i][0] == "EXISTS":
            if queries[i][1] in new_elements:
                result.append("true")
            else:
                result.append("false")
        elif queries[i][0] == "REMOVE":
            if queries[i][1] in new_elements:
                new_elements.remove(queries[i][1])
                result.append("true")
            else:
                result.append("false")
        elif queries[i][0] == "GET_NEXT":
            #sorted_list = new_elements)
            #print(f" new_elements {new_elements}")
            result.append(get_next(queries[i][1]))
    return result


#
res = solution(queries)

print(res)
#     list = [1,2, 4]
#
#     get_next(1)