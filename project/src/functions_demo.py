def hello_func():
    return 'Hello Function'
    #print("Inside Hello Function!")
    #pass

def hello_func(greeting = "Hello", name = "India"):
    return '{} {} Function.'.format(greeting, name)
    #print("Inside Hello Function!")
    #pass

#DRY - dont repeat yourselves

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

print(hello_func().upper())


print(hello_func("Hi", "Raghav"))

print(student_info("Math", "Art", name="John", age=22))

print("***********")
courses = ["math", "Art"]
info = {"name":"Raghav", "age": 37}

student_info( *courses, **info)


month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap_year(year):
        return 29

    return month_days[month]

print(is_leap_year(2017))
print(is_leap_year(2024))

print(days_in_month(2017, 2))
print(days_in_month(2024, 2))
print(days_in_month(2024, 10))
print(days_in_month(2024, 14))






