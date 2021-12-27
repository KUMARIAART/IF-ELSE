"Accept the age, sex (‘M’, ‘F’), number of days and display the wages accordingly"
"If age does not fall in any range then display the following message: “Enter appropriate age"

age=int(input("enter the age:-"))
gender=input("enter the gender:-")
wages=int(input("enter the wages:-"))
if age>=18 and age<30:
    print(age,gender,wages,"yes")
elif age>=30 and age<=40:
    print(age,gender,wages,"no") 
else:
    print("Enter appropriate age")  


    
# M
# 700
# F
# 750
# M
# 800
# F
# 850

     


