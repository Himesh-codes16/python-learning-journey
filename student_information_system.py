name = input("Enter your name ")
age = int(input("Enter your age "))
marks = float(input("Enter your marks out of 100 "))
city = input("Enter the name of the city you live in ")
email = input("Enter you active email id ")
print("--------Student Report--------")
print("Name of the Student :",name)
print("Age of the Student :",age)
print("City in which the Student lives :",city)
print("Email id of the Student :",email)
print("Marks of the Student :",marks)
print("Length of the Student's name is :",len(name),"characters (including space)")
print("First letter of the Student's name is :",name[0])
print("Last letter of the Student's name is :",name[-1])
if(marks >= 90):
    print("A+ Grade")
elif(marks >=80 and marks < 90):
    print("A Grade") 
elif(marks >=70 and marks < 80):
    print("B Grade")
elif(marks >=60 and marks < 70):
    print("C Grade")
else:
    print("Needs Improvement")
if(age >= 18):       
    print("Student is eligible to vote")
else:
    print("Student is not eligible to vote")
if(email.endswith("@gmail.com")):
    print("Student has a Gmail Account")
else:
    print("Student uses other service provider for Email Account")
yes=int(input("Do you want to continue ? \n If yes then type 1 "))
if(yes==1):
    print("Thank You ! for submitting your details")
else:
    print("Program Closed")