file1 = open("/Users/hadoop/Downloads/Cover_letter.txt", "w")
L = ["this is Bengaluru \n", "This is Chennai \n", "This is London \n", "This is NYC \n"]

file1.write("Hello \n")
file1.writelines(L)
file1.close()

file1 = open("/Users/hadoop/Downloads/Cover_letter.txt", "r+")

print("Output of Read function is ")
print(file1.read())
print()

# seek(n) takes the file handle to the nth
# byte from the beginning.
file1.seek(0)

print("Output of Readline function is ")
print(file1.readline())
print()

# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(99))
print()

file1.seek(0)
print("Output of Readline(9) function is ")
print(file1.readline(99))
print()

dir()