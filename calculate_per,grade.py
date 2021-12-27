phy=int(input("enter marks for phy:"))
chem=int(input("enter marks for chem:"))
bio=int(input("enter marks for bio:"))
math=int(input("enter marks for bio:"))
comp=int(input("enter marks for comp:"))
per=(phy+chem+bio+math+comp)/5
print(per)
if (per>=90):
    print("grade A")
elif (per>=80):
    print("grade B")  
elif (per>=70):
    print("grade C")  
elif (per>=60) :
    print("grade D") 
elif (per>=40) :
    print("grade E") 
else:
    print("grade F")          