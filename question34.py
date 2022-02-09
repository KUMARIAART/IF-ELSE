"Write a Python program to display the current date and time."

import datetime   
dt = datetime.datetime.now() # use now() method in datetime  
print( "Display the current date of the system: ") # current date   
print (str (dt) ) # call the dt variable to print the system date. 


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
