"Write a program to accept two numbers and mathematical operators"
"and perform operation accordingly."
"Like:"
"Enter First Number: 7"
"Enter Second Number : 9"
"Enter operator : +"
"Your Answer is : 16"

num1=int(input("enter first number:-"))
num2=int(input("enter second number:-"))
symbol=(input("enter the symbol:-"))
if symbol=="+":
    print(num1+num2)
elif symbol=="-":
    print(num1+num2)  
elif symbol=="*":
    print(num1+num2)
elif symbol=="**":
    print(num1+num2) 
elif symbol=="/":
    print(num1+num2) 
elif symbol=="%":
    print(num1+num2)
elif symbol=="//":
    print(num1+num2)                    
else:
    print("no")    
