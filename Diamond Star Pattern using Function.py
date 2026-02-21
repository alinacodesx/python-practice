# Diamond Star Pattern using Function

def diamond_pattern(n):
    # Upper half
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

    # Lower half
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)


# Taking input from user
num = int(input("Enter number of rows: "))
diamond_pattern(num)