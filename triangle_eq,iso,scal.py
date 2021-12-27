side1=int(input("enter  the number:"))
side2=int(input("enter the number:"))
side3=int(input("enter the number:"))
if (side1==side2 and side2==side3):
    print("the triangle is equilateral")
elif(side1==side2 or side1==side3 or side2==side3) :
    print("the triangle is isosceles")
else:
    print(" the triangle is scalene")    


