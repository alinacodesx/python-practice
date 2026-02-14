m = int(input("Enter month no: "))
y = int(input("Enter year: "))
match m:
    case 1|3|5|7|8|10|12:
         print("31 days")
    case 4|6|9|11:
         print("30 days")
    case 2:
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
         print("29 days")
        else:
         print("28 days")
    case _:
         print("Invalid month no")