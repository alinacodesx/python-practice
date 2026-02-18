# Check whether a number is Armstrong or not using function

def is_armstrong(n):
    temp = n
    power = len(str(n))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10

    return total == n


num = int(input("Enter a number: "))

if is_armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
