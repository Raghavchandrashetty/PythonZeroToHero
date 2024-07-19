

if True:
    print("condition was true")
else:
    print("False")

language = "python"

if language == "python":
    print("PYTHON")
else:
    print("NON PYTHON")

"""
Equals:                     ==
NOt Equals:                 !=
Greater than                >
Less than                   <
Greater or Equal            >=
Lesser or Equal             <=
Object identity :           is
"""

five = 5
six = 6
aaru = 6
if five == six:
    print("Equal")
else:
    print("Not equal")

if six == aaru:
    print("SIXER")
else:
    print("NOT a 6")

language = "scala"
if language == "python":
    print("PYTHON")
elif language == "java":
    print("Java")
elif(language == "scala"):
    print("Scala")
else:
    print("OLD language")


# and / or / not

user = "admin"
logged_in= False

if user == "admin" and logged_in :
    print("Admin page")
else:
    print("bad creds")

if user == "admin" or logged_in :
    print("Admin page")
else:
    print("bad creds")

logged_in= True
if  not logged_in :
    print("PLEASE LOG IN ")
else:
    print("WELCOME")

# comparing lists
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)

print(a is b)
print(id(a))
print(id(b))

print(c is b)
print(id(c))
print(id(a))

print(id(a) == id(c))


"""
False values:
    False
    None
    Zero of any numeric type
    An empty sequence, for example, '', (), []
    Any empty mapping, for example , {}.
    
"""

condition = False

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

condition = None

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

condition = 0

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

condition = {}

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

condition = ()

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

condition = []

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

condition = ''

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

condition = 0.0

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")