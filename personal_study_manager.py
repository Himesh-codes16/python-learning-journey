import os

print(os.getcwd())
subjects = {}
def total_hours(subjects):
    return sum(subjects.values())
def most_studied(subjects):
    highest_subject,highest_hour = next(iter(subjects.items()))
    for subject,hour in subjects.items():
        if hour > highest_hour:
            highest_hour = hour
            highest_subject = subject
    return "You have studies highest",highest_hour,"hours on",highest_subject
while True:#Main Menu
    print("\n=====Study Manager=====")
    print("1. Add Subject")
    print("2. View Subjects")
    print("3. Search Subject")
    print("4. Add Study Hours")
    print("5. Show Total Study Hours")
    print("6. Show Most Studied Subject")
    print("7. Save Data")
    print("8. Load Data")
    print("9. Exit")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        key=input("Enter name of the subject: ").lower()
        value = int(input("Enter the number of hours spent on the subject: "))
        subjects[key] = value
    elif choice == 2:
        if(len(subjects) > 0):
            for key,value in subjects.items():
                print(f"{key}:{value} hours")
        else:
            print("No Data Entered yet")
    elif choice == 3:
        search = input("Enter the Subject you want to search: ").lower()
        if search in subjects:
            print("The Subject",search,"is found in database")
            print("Time spent on the subject is",subjects[search])
        else:
            print("Subject not found please make sure the subject is added in the database")
    elif choice == 4:
        key = input("Enter the subject in which you have to add study hours:").lower()
        value = int(input("Enter hours studies in that subject: "))
        if key in subjects:
            subjects[key]+=value
            print("Study hours updated successfully")
        else:
            print("Subject Not Found")
    elif choice == 5:
        print("Total hours spent on studies is",total_hours(subjects))
    elif choice == 6:
        if len(subjects) > 0:
            print( most_studied(subjects))
    elif choice == 7:
        print("Current Subjects: ",subjects)
        file = open("subjects.txt","w")
        for key,value in subjects.items():
            file.write(f"{key}:{value}\n")
        file.close()
        print("Data saved successfully")
    elif choice == 8:
        file = open("subjects.txt","r")
        subjects={}
        for line in file:
            line = line.strip()
            parts = line.split(":")
            subjects[parts[0]] = int(parts[1])
        file.close()
        print("Data loaded Successfully")
    elif choice == 9:
        break
    else:
        print("Incorrect choice number entered" )
print("Thankyou")              