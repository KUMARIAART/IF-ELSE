"Accept the number of days from the user and calculate the charge for library according to following :"
"First five days : Rs 2/day."
"Six to ten days  : Rs 3/day."
"Ten to 15 days  : Rs 4/day"
"After 15 days    : Rs 5/day"

user=int(input("enter num of days:-"))
if user<=5:
    print("2rs")
elif user>=6 and user<=10:
    print("3rs") 
elif user>=10 and user<=15:
    print("4rs") 
else:
    print("5rs")          





