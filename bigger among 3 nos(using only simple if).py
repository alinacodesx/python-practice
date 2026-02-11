a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
big = a
if b>big:
    big=b
if c>big:
    big=c
print("biggest number=",big)