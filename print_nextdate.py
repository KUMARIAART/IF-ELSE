date=int(input("enter the date"))
if date>=1 or date<=31:
    month=int(input("enter the month:"))
    if month>=1 or month<=12:
        year=int(input("enter the year:"))
        if year>=0 and year<=2021:
            print(date+1,"/",month,"/",year)
        else:
            print("invalid")
    else:
        print("invalid")
else:
    print("invalid")        
