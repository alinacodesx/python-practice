# topic: average of 3 numbers
# to find the average of 3 numbers
# average = (a+b+c)/3
a = 10
b = 19
c = 14
avg = (a+b+c)/3
print("average=",avg)
# to find the average of 3 numbers using input function
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
avg = (a+b+c)/3
print("average=",avg)
# to find the average of 3 numbers using function
def average(num1, num2, num3):
    avg = (num1 + num2 + num3) / 3
    return avg
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))
result = average(num1, num2, num3)
print("average =", result)
# to find the average of 3 numbers using function and return statement
def average(num1, num2, num3):
    avg = (num1 + num2 + num3) / 3
    return avg
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))
result = average(num1, num2, num3)
print("average =", result)
