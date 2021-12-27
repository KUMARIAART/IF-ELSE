# speed=input("gadi ki kya speed hai?")
# time=speed
# speed=int(speed)
# if speed<=70:
#     print("gadi speed limit me hai")
# else:
#     print("gadi speed limit ke bahar thi.") 

speed=int(input("please enter speed:-"))
time=int(input("enter any number for time:-"))-70*50
if speed<time:
    print("please pay your fine",time)
else:
    print("stay home and be safe",time)    



