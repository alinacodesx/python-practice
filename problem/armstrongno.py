n = int(input("Enter number: "))
digits = str(n)
power = len(digits)
total = sum(int(d) ** power for d in digits)
if total == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is NOT an Armstrong number")
