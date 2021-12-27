"Write a python program to input electricity unit charges and calculate total "
"electricity bill according to the given condition:"
"For first 50 units Rs. 0.50/unit"
"For next 100 units Rs. 0.75/unit"
"For next 100 units Rs. 1.20/unit"
"For unit above 250 Rs. 1.50/unit"
"An additional surcharge of 20% is added to the bill"

# charges=int(input("enter:-"))
# per_unit=int(input("enter:-"))
# total=charges*per_unit*20/100
# if charges<50:
#     print("low")
# elif charges>50 and charges<100:
#     print("medium")
# elif charges>100 and charges<200:
#     print("little")  
# elif charges<250:
#     print("higher") 
# else:
#     print("not valid")             


# u = int(input('Enter The Amount Of Units Consumed:'))
# if u <= 50:
#     amt = u*0.5 
#     print('Amount To Be Paid Is:',amt)  
# elif u <= 150 and u > 50:
#     amt = (50*0.5) + ((u-50)*0.75)
#     print('Amount To Be Paid Is:',amt)
# elif u <= 250 and u > 150:
#     amt = (50*0.5) + (100*0.75) + ((u-150)*1.2)
#     print('Amount To Be Paid Is:',amt)
# else:
#     amt = (50*0.5) + (100*0.75) + (100*1.2) + ((u-250)*1.5)
#     print('Amount To Be Paid Is:',amt)
# print('Process Completed')


"Write a program to calculate the electricity bill (accept number of unit from user) "
"according to the following criteria :"
"Unit                                                     Price " 
"First 100 units                                               no charge"
"Next 100 units                                              Rs 5 per unit"
"After 200 units                                             Rs 10 per unit"
"(For example if input unit is 350 than total bill amount is Rs2000)"

num=int(input("enter the value:-"))
if num<100:
    print("no charge")
elif 5*100>100:
    print("yes")  
elif 10*200>200:
    print("no")
else:
    print("invalid")   
    
           




