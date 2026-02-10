# topic: area of circle
# question -to find the area of circle
# area of circle = 3.14*r**2
r = float(input("enter radius:"))
area = 3.14*r**2
print("area of circle=",area)
# area of circle using function
def area_of_circle(radius):
    area = 3.14 * radius ** 2
    return area
r = float(input("enter radius:"))
result = area_of_circle(r)
print("area of circle =", result)
# area of circle using function and error handling
def area_of_circle(radius):
    try:
        area = 3.14 * radius ** 2
        return area
    except TypeError:
        return "Invalid input. Please enter a number."
r = input("enter radius:")
result = area_of_circle(r)
print("area of circle =", result)

