# # Create a sample matrix
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9],
#           [0, 2, 6]]
#
# rows = len(matrix)
# cols = len(matrix[0])
#
#
# # Function to get the diagonals
# def get_diagonals(matrix):
#     diagonals = []
#
#     # Loop over columns for the first half
#     for col in range(cols):
#         # row, col = 0, col
#         row =  0
#         diagonal = []
#         while row < rows and col >= 0:
#             diagonal.append(matrix[row][col])
#             row += 1
#             col -= 1
#         diagonals.append(diagonal)
#
#     print("First half")
#     print(diagonals)
#     # Loop over rows for the second half
#     for row in range(1, rows):
#         col =  cols - 1
#         diagonal = []
#         while row < rows and col >= 0:
#             diagonal.append(matrix[row][col])
#             row += 1
#             col -= 1
#         diagonals.append(diagonal)
#
#     print("Second half")
#     print(diagonals)
#     return diagonals
#
#
# # Get and print the diagonals
# diagonals = get_diagonals(matrix)
# for diagonal in diagonals:
#     print(" ".join(map(str, diagonal)))

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [0, 2, 6]]

cols = len(matrix[0])

rows = len(matrix)

print(f" rows {rows}   cols {cols}")



def get_diagonals(matrix):

    diagonals = []

    for col in range(cols):
        row = 0
        diagonal = []
        while row < rows and col >= 0:
            diagonal.append(matrix[row][col])
            row += 1
            col -= 1
        diagonals.append(diagonal)

    print(f"first half " , diagonals)

    for row in range(1, rows):
        col = cols-1
        diagonal = []

        while row <  rows and col >= 0:
            diagonal.append(matrix[row][col])
            row += 1
            col -= 1
        diagonals.append(diagonal)

        # print("Second half")
        # print(diagonals)
    return diagonals


# Get and print the diagonals
diagonals = get_diagonals(matrix)
for diagonal in diagonals:
    print(" ".join(map(str, diagonal)))