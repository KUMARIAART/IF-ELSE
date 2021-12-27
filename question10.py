"Take the age of 3 people by user and determine oldest and youngest among them."
from typing import SupportsRound


AARTI=int(input("enter first age:-"))
SONU=int(input("enter second age:-"))
PAWAN=int(input("enter third age:-"))
if AARTI<SONU and AARTI<PAWAN:
    if SONU>AARTI and SONU<PAWAN:
        print("aarti is youngest")
        print("sonu is oldest")
    else:
        print("aarti is youngest") 
        print("pawan is oldest")
elif SONU<AARTI and SONU<PAWAN:
    if AARTI>SONU and AARTI>PAWAN:
        print("sonu is youngest")   
        print("aarti is oldest")  
    else:
        print("sonu is youngest") 
        print("mohit is oldest") 
elif PAWAN<AARTI and PAWAN<SONU:
    if AARTI>PAWAN and AARTI>SONU:
        print("pawan is youngest") 
        print("aarti is oldest")   
    else:
        print("pawan is youngest") 
        print("sonu is oldest")        
        
      