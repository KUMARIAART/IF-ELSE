print("welcome to STATE BANK OF INDIA please insert your card")
print("hi,please do not remove your card leave your card inserted during the entire transaction")
card=input("select your card 1.debit card:")
if card=="1":
    language=input(" please select your language 1.english 2.हिन्दी:")
    print()
    if language=="1":
        pin=int(input("enter your pin:"))
        if pin==6789:
            account_type=(input("enter your account type:"))
            if account_type=="current"or "saving":
                print("please select transection:deposit,pin change,withdraw,balance enquary")
                trangection=(input("cheque your trangection:"))
                if trangection=="withdraw":
                    amount=int(input("enter total amount in the form of 100,200,500,2000:"))
                    balance=50000
                    if amount>=0 or amount<=50000:
                        if amount%100==0:
                            print("your current balance is",balance-amount)
                            receipt=input("do you want receipt 1.yes,2.no:" )
                            if receipt=="1":
                                print("your trangection is completed please collect your card")
                            else:
                                print("trangection fail")  
                        else:
                            print("try again")  
                    else:
                        print("enter valid amount")
                else:
                    print("trangection fail")
            else:
                print("invalid account")
        else:
            print("please correct pin")
    else:
        print("invalid")
else:
    print("not access") 
print("thank you")           





                                
                  
                    
                


    

