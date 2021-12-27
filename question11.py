"A student will not be allowed to sit in an exam if his/her attendance "
"is less than 75%.Take following input from the user. Number of classes held."
"Number of classes attended. And print, percentage of class attended. "
"Is the student is allowed to sit in the exam or not."

class_held=int(input("please enter the number:-"))
class_attended=int(input("please enter the number:-"))
percentage=class_attended/class_held*100
if percentage>=75:
    print("allowed")
else:
    print("not allowed")

