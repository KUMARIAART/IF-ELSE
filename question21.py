"Accept three numbers from the user and display the second largest number."


a=int(input("enter first number:-"))
b=int(input("enter second number:-"))
c=int(input("enter third number:-"))
if a<b and b<c or a>b and b>c:
    print(b,"is second largest number")
else:
    print("wrong") 

  
