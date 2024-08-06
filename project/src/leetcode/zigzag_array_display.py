# def string_to_2d_array(s, num_cols):
#     # Calculate the number of rows needed
#     num_rows = (len(s) + num_cols - 1) // num_cols
#
#     # Create the 2D array
#     array_2d = [list(s[i * num_cols:(i + 1) * num_cols]) for i in range(num_rows)]
#
#     return array_2d
#
# # def string_to_2d_array(s, num_rows):
# #     # Calculate the number of columns needed
# #     num_cols = (len(s) + num_rows - 1) // num_rows
# #
# #     # Create the 2D array
# #     array_2d = [list(s[i * num_cols:(i + 1) * num_cols]) for i in range(num_rows)]
# #
# #     return array_2d
#
# def transpose(matrix):
#     return [list(row) for row in zip(*matrix)]
#
# # Example usage
# s = "PAYPALISHIRING"
# num_rows = 3
# array_2d = string_to_2d_array(s, num_rows)
# print(array_2d)
#
#
# def display_2d_array(array_2d):
#     for row in array_2d:
#         print(' '.join(row))
#
# display_2d_array(array_2d)
#
# transposed = transpose(array_2d)
# print(transposed)
#
# # # Example usage
# # s = "abcdefghij"
# # num_cols = 3
# # array_2d = string_to_2d_array(s, num_cols)
# # print(array_2d)
#
#
#
str1 = "PAYPALISHIRINGMENOW"
num_rows = 3
d = {}
for index_i, char in enumerate(str1):
    print(f"Index {index_i}: {char}")
    d.update({index_i:char})

    # for j in range( index_i , len(str)):
    #     print(f"i -> {index_i} , j -> {j}")
#first_row = for i in range(0, len(str), 4)
row_number = 3
increment_value = 0
# for i in range(3):
#     if i%2 == 0:
#         increment_value = row_number+1
#     else:
#         increment_value = row_number  1
#     first_row = [d[x] for x in range(i, len(str), row_number + 1)]
#     print(first_row)
#second_row = [d[x] for x in range(1, len(str), row_number - 1)]
#print(second_row)
#third_row = [d[x] for x in range(2, len(str), row_number + 1)]
#print(third_row)
# for i in range(row_number):
#     if i ==
i = 0
d = {}
pntr = 0
incrementFlag = True
while i < len(str1):
    print("&&&&&       i value : ", i)
    print("Pointer before assignment ", pntr)


    if pntr in d:
        d[pntr].append(str1[i])
    else:
        d[pntr] = [str1[i]]


    if pntr == row_number-1:
        incrementFlag = False
    if pntr == 0:
        incrementFlag = True
    i += 1
    if incrementFlag:
        pntr += 1
    else:
        pntr -= 1

    print("Pointer after assignment ", pntr)
    result = ''
    for key in sorted(d.keys()):
        result += ''.join(d[key])
    return result


# Function to concatenate dictionary values
def concatenate_dict_values(d):
    result = ''
    for key in sorted(d.keys()):
        result += ''.join(d[key])
    return result






