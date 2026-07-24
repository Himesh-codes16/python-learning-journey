"""
Project: Personal Expense Tracker
Author: Himesh
Language: Python

Description:
A menu-driven console application that allows users to add,
search, and analyze expenses using dictionaries, functions,
loops, and conditional statements.
"""
def total_expense(expenses):#total price
    return sum(expenses.values())
def highest(expenses):#highest price
    highest_category, highest_price = next(iter(expenses.items()))
    for category,expense in expenses.items():
        if(expense > highest_price):
            highest_price = expense
            highest_category = category
    return "You have spent highest amount on",highest_category,"and that is",highest_price
def lowest(expenses):#lowest price
    lowest_category, lowest_price = next(iter(expenses.items()))
    for category,expense in expenses.items():
        if(expense < lowest_price):
            lowest_price = expense
            lowest_category = category
    return "You have spent lowest amount on",lowest_category,"and that is",lowest_price
def average(expenses):#for average
    total=0
    for price in expenses.values():
        total+=price
    return "Average amount spent is ",total/len(expenses)
expenses = {}
while True:#main menu
    print("===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expense")
    print("4. Show Total Expense")
    print("5. Show Highest Expense")
    print("6. Show Lowest Expense")
    print("7. Show Average Expense")
    print("8. Exit")
    print("---------------------------")
    choice = int(input("Please enter your choice "))#choice cases
    if (choice == 1):
        key = input("Enter Expense category ")
        value = int(input("Enter the amount spent "))
        expenses[key] = value         
    elif (choice == 2):
        if(len(expenses) > 0):
            for key,value in expenses.items():
                print(f"{key}:{value}")
        else:
            print("No expense added yet")
    elif (choice == 3):
        search=input("Enter expense category to search:")
        if search in expenses:
            print("Category of expense is:",search)
            print("Amount spent is:",expenses[search])
        else:
            print("Expense does not exist")
    elif (choice == 4):
        print("Total expenses is:",total_expense(expenses))
    elif (choice == 5):
        if(len(expenses) > 0):
            print(highest(expenses))
        else:
            print("No data entered")
    elif (choice == 6):
        if(len(expenses) > 0 ):
            print(lowest(expenses))
        else:
            print("No data entered")
    elif (choice == 7):
        if(len(expenses) > 0):
            print(average(expenses))
        else:
            print("No items in the cart")
    elif(choice == 8):
        break
    else:
        print("Incorrect Choice Number entered")
print("Thank you")#End of program