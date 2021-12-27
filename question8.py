"A company decided to give a bonus of 5% to an employee if his/her year of service is"
"more than 5 years. Ask users for their salary and year of service and print the net bonus amount."

salary=int(input("enter salary:"))
year=int(input("enter year:-"))
total=salary*5/100
if year >=5:
    print(total,"gives bonus")
else:
    print("not gives bonus")    