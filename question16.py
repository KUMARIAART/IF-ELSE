"Accept any city from the user and display the monument of that city."
"City                                 Monument"
"Delhi                               Red Fort"
"Agra                                Taj Mahal"
" Jaipur                              Jal Mahal"

city=input("enter the city name:-")
if city=="delhi":
    print("red fort")
elif city=="agra":
    print("Taj Mahal")
elif city=="jaipur":
    print("Jal Mahal")    
else:
    print("invalid")    
