"Write a Python program to accept a filename from the user and print the extension of that." 
"Sample filename : abc.java"
"Output : java"

# name=input("enter the name:-")
# a="abc.java"
# b="script"
# if a and b:
#     print(b)
# else:
#     print("wrong") 

filename=input("input the filename:-")  
f_extns=filename.split(".") 
print("the extension of the file is : "+repr(f_extns[-1]))

