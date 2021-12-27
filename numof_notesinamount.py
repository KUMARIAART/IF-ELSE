amt=int(input("Enter the amount:"))
if amt>=500:
    notes_500=amt//500
    print("Minimum number of 500 notes is",notes_500)
elif amt>=100:
    notes_100=amt//100
    print("Minimum number of 100 notes is",notes_100)
elif amt>=50:
    notes_50=amt//50
    print("minimum number of 50 notes is",notes_50) 
elif amt>=10:
    notes_10=amt//10
    print("minimum number of 10 notes is",notes_10)  
else:
    print("invalid amount")         