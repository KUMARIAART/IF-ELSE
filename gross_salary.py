basic_salary=int(input(" enter basic salary of employee:"))
if (basic_salary<=10000 ):
    da=basic_salary*(80/100)
    hra=basic_salary*(20/100)

elif (basic_salary <=20000)  :
    da=basic_salary*(90/100) 
    hra=basic_salary*(25/100)
else:
    da=basic_salary*(95/100)  
    hra=basic_salary*(30/100) 

print(basic_salary+hra+da)

     

