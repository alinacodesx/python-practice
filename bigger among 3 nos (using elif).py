# bigger among 3 nos (using elif)
a = int(input("enter first no:"))
b = int(input("enter second no:"))
c = int(input("enter third no:"))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b) 
else:
    print(c)       