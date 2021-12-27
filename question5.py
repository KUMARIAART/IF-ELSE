"Write a Python program to add 'ing' at the end of a given string (length should be at least"
"3). If the given string already ends with 'ing' then add 'ly' instead. If the string length"
"given string is less than 3, leave it unchanged. Go to the editor"
"Sample String : 'abc'"
"Expected Result : 'abcing'"
"Sample String : 'string'"
"Expected Result : 'stringly'"


n=input("enter the word:-")
a="ly"
b="ing"
if a in n:
    if len(n)==3:
        print(n+b)
if n in b:  
    print(n+a)
else:
    print(n+b)