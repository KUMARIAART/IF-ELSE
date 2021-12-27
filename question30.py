"the number is of one digit or two digit or three digit or more than three digit "


num=int(input("enter the value:-"))
if num<=1 and num>=9:
    print(num,"is a one digit number")
elif num>=10 and num<=99:
    print(num,"is two digit number")
elif num>=100 and num<=999:
    print(num,"is a thre digit number") 
elif num>1000 and num<=9999:
    print(num,"is a four digit number") 
else:
    print("invalid")          
