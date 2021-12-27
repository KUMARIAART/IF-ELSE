 
"Write a Python program that reads two integers representing a month"
"and day and prints the season for that month and day." 
"Expected Output:"
"Input the month (e.g. January, February etc.): july "                    
"Input the day: 31 "                                                      
"Season is autumn "

month=(input("enter the month:-"))
day=int(input("enter the day:-"))
if month=="jan" or "feb" or "march" or "apr":
   day=="29"
   print("Season is winter")
elif month=="may" or "june" or "july" or "aug":
     day=="30"
     print(" season is summer")
elif month=="sep" or "oct" or "nav" or "dec":
     day=="31"
     print(" season is raining")   
else:
    print("wrong")
        


