"Write a program to accept the cost price of a bike and display the road tax"
"to be paid according to the following criteria :" 
"Cost price (in Rs)                                       Tax"
"> 100000                                                  15 %"
" > 50000 and <= 100000                                    10%"
" <= 50000                                                  5%"

cost=int(input("enter the price:-"))
if cost>100000 :
    print("total amount",cost,"remainig amount",cost*15/100-cost,"","totat tax",cost*15/100)
elif cost>50000 and cost <=100000: 
    print("total amount",cost,"remainig amount",cost*10/100-cost,"","totat tax",cost*10/100)
elif cost <=50000:
    print("total amount",cost,"remainig amount",cost*5/100-cost,"","totat tax",cost*5/100) 
else:
    print("not at all")          

       
