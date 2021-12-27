print("create your new facebook account")
first_name=(input("enter first name:"))
if first_name>="A" and first_name<="Z" or first_name>="a" and first_name<="z":
    print("first name")
    last_name=(input("enter last name:"))
    if last_name>="A" and first_name<="Z" or first_name>="a" and last_name<="z":
        print("last name")
        date=int(input("enter the date:"))
        if date>=1 or date<=31:
            month=int(input("enter the month:"))
            if month>=1 or month<=12:
                year=int(input("enter the  year:"))
                if year>=1800 and year<2021:
                    print(date,month,year)
                    gender=(input("enter the gender:"))
                    if gender=="female":
                        print("female")
                        gmail=(input("add your mail:"))
                        if gmail=="arti39612@gmail.com":
                            print("gmail")
                            mobile_no=int(input("enter moble no:"))
                            if mobile_no>=0 or mobile_no<=9:
                                print("mobile no")
                                otp=int(input("enter the otp:"))
                                if otp>=0 or otp<=9:
                                    print("suggest strong password")
                                    upper_case=(input("enter the upper case:"))
                                    if upper_case>="A "and upper_case<="Z":
                                        print("it is upper case letter")
                                        lower_case=(input("enter the lower case:"))
                                        if lower_case>="a" and lower_case<="z":
                                            print("it is lower case")
                                            special_char=(input("enter the special char:"))
                                            if special_char=="@" or special_char=="$" or special_char=="#":
                                                print("it is special char")
                                                numeric=(input("enter the number:"))
                                                if numeric>="0" and numeric<="9":
                                                    print("it is number")
                                                    a=(upper_case+lower_case+str(numeric)+special_char)
                                                    if len(a)==8:
                                                        print("it is strong password")
                                                        print("finish singning up")
                                                    else:
                                                        print("it is not strong password")
                                                else:
                                                    print("it is not numeric")  
                                            else:
                                                print("it is not special_char")
                                        else:
                                            print("it is not lower case")  
                                    else:
                                        print("it is not upper case charector")
                                else:
                                    print("invalid otp")
                            else:
                                print("inccorect no.")  
                        else:
                            print("invalid account")
                    else:
                        print("invalid gender")
            else:
                print("incorrect date")
    else:
        print("invalid last name")
else:
    print("invalid first name")
print("save password and remember your phone number and password")
