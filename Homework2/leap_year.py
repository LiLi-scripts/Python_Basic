year = int(input("year: "))

leap = 366
usual = 365

if year % 4 !=0:
    print("Quantity of days: ", usual)
elif year % 4 == 0:
    print("leap year:", leap)
elif year % 100 !=0:
    print("leap year:", leap)
elif year % 400 != 0:
    print("leap year:", leap)
else:
    pass