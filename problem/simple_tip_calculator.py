# simple tip calculator
bill = float(input("Enter bill amount: "))
tip_percent = float(input("Enter tip percentage: "))

tip = bill * (tip_percent / 100)
total = bill + tip

print("Tip:", round(tip,2))
print("Total bill:", round(total,2))

