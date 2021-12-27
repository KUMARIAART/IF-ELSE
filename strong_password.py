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
              else:
                    print("it is not strong password")  
           else:
                print("it is not special_char") 
        else:
            print("it is not a number")  
    else:
        print("it is not lower case charector")  
else:
    print("it is not upper case charector")                             



