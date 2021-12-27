"Write a Python program to test whether a number is within 100 of 1000 or 2000"
a=int(input("enter the value:-"))
b=int(input("enter the value:-"))
n=100
if (n-1000)<=100:
    print("correct")
elif (n-2000)<=100:
    print("yes")  
else:
    print("incorrect")      



