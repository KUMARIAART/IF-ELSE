year=int(input("enter the year:"))
if year%100==0:
    if year%400==0:
        print("leap year ",year)
    else:
        print("not a leap year")
elif year%4==0:
    print("leap year",year)
else:
    print("not a leap year")


