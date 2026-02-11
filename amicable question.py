#Amicable numbers are a pair of numbers where:
#the sum of proper divisors of the first number = the second number
#and the sum of proper divisors of the second number = the first number.
#Exampe- 220 and 284.

n1 = int(input("enter first no: "))
n2 = int(input("enter second no: "))
s1 = 0
s2 = 0
for i in range(1,n1//2+1):
    if n1 % i == 0:
        s1 += i
for i in range(1,n2//2+1):
    if n2 % i == 0:
        s2 += i
if s1==n2 and s2==n1:
    print("Numbers are amicable")
else:

    print("Numbers are not amicable")
