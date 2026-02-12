#to check number is prime or not using for loop
n = int(input('Enter your number'))
count = 0
for i in range(1,n+1): 
    if n % i == 0:
        count += 1    #move to next number
if count == 2:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")

    


