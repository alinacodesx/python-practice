# topic area of triangle
# question - to find the area of triangle
# area of triangle = 0.5*base*height
base = float(input("enter base of triangle:"))
height = float(input("enter height of triangle:"))
area = 0.5 * base * height
print("area of triangle =", area)
# area of triangle using heron's formula
# heron's formula = sqrt(s*(s-a)*(s-b)*(s-c))
import math
a = float(input("enter side a of triangle:"))
b = float(input("enter side b of triangle:"))
c = float(input("enter side c of triangle:"))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (
s - c))
print("area of triangle =", area)
# area of triangle using function
def area_of_triangle(base, height):
    area = 0.5 * base * height
    return area
base = float(input("enter base of triangle:"))
height = float(input("enter height of triangle:"))
result = area_of_triangle(base, height)
print("area of triangle =", result)
# area of triangle using function and heron's formula
def area_of_triangle(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
a = float(input("enter side a of triangle:"))
b = float(input("enter side b of triangle:"))
c = float(input("enter side c of triangle:"))
result = area_of_triangle(a, b, c)
print("area of triangle =", result)
# area of triangle using function and heron's formula and error handling
def area_of_triangle(a, b, c):
    try:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    except ValueError:
        return "Invalid input. Please enter valid sides of triangle."
a = float(input("enter side a of triangle:"))
b = float(input("enter side b of triangle:"))
c = float(input("enter side c of triangle:"))
result = area_of_triangle(a, b, c)
print("area of triangle =", result)
# area of triangle using function and heron's formula and error handling and loop
def area_of_triangle(a, b, c):
    try:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    except ValueError:
        return "Invalid input. Please enter valid sides of triangle."
while True:
    a = float(input("enter side a of triangle:"))
    b = float(input("enter side b of triangle:"))
    c = float(input("enter side c of triangle:"))
    result = area_of_triangle(a, b, c)
    print("area of triangle =", result)
    