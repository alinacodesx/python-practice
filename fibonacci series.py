a = int(input("enter first term"))
b = int(input("enter second term"))
t = int(input("enter total terms"))
print(a, end=" ")
print(b, end=" ")

for i in range(3,t+1):
    c = a + b
    print(c, end=" ")
    a = b
    b = c 