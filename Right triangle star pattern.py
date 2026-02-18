# Right triangle star pattern

def pattern(n):
    for i in range(1, n + 1):
        print("*" * i)

num = int(input("Enter number of rows: "))
pattern(num)
