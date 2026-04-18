# Example of try-except with else block

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
else:
    print("You entered:", number)
    print("Square of number:", number * number)
