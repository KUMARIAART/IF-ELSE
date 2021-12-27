"write a python programe to reverse the number"  

num=int(input("enter any number:-"))
a=num%10
num//=10
b=num%10
c=num//10
d=(a*100+b*10+c*1)
if d<1000:
    print(d,"is a reverse number")
else:
    print("invalid")    




