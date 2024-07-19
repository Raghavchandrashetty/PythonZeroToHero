def my_decorator(func):
    def wrapper():
        print("something happening before the fucntion")
        func()
        print("something happening after the function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()