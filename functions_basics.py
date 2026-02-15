"""
Topic: Python Functions
This file demonstrates:
- defining and calling functions
- print vs return
- parameters and default values
- *args and **kwargs
"""


# --------------------------------------------------
# Basic Function
# --------------------------------------------------

def hello_func():
    """Return a simple greeting."""
    return "Hello function."


# calling the function
print(hello_func())

# using returned value
print(hello_func().upper())
print(hello_func().lower())


# --------------------------------------------------
# Function with Parameters
# --------------------------------------------------

def greet(greeting, name="You"):
    """
    Return a formatted greeting message.

    greeting -> required argument
    name -> default argument
    """
    return "{}, {}".format(greeting, name)


print(greet("Hi", name="Alina"))
print(greet("Hello"))   # default name will be used


# --------------------------------------------------
# *args and **kwargs
# --------------------------------------------------

def student_info(*args, **kwargs):
    """
    *args   -> multiple positional arguments (tuple)
    **kwargs -> multiple keyword arguments (dictionary)
    """
    print("Courses:", args)
    print("Details:", kwargs)


# data
courses = ["Math", "Art"]
info = {"name": "Alina", "age": 18}

# unpacking while calling function
student_info(*courses, **info)
