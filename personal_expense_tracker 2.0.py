"""
Project: Personal Expense Tracker
Author: Himesh
Language: Python

Description:
A menu-driven console application that allows users to add,
search, and analyze expenses using dictionaries, functions,
loops, and conditional statements.
"""
import json
def total_expense(expenses):#total price
    return sum(transaction['amount'] for transaction in expenses)
def highest(expenses):#highest price
    first_transaction = expenses[0]
    highest_category = first_transaction['category']
    highest_price = first_transaction['amount']
    for transaction in expenses:
        if(transaction['amount'] > highest_price):
            highest_price = transaction['amount']
            highest_category = transaction['category']
    return f"You have spent highest amount on {highest_category} and that is {highest_price}"
def lowest(expenses):#lowest price
    first_transaction = expenses[0]
    lowest_category = first_transaction['category']
    lowest_price = first_transaction['amount']
    for transaction in expenses:
        if(transaction['amount'] < lowest_price):
            lowest_price = transaction['amount']
            lowest_category = transaction['category']
    return f"You have spent lowest amount on {lowest_category} and that is {lowest_price}"
def average(expenses):#for average
    if not expenses:
        return 0
    total=0
    for transaction in expenses:
        total+=transaction['amount']
    return total / len(expenses)
def high_expenses(expenses):
    avg = average(expenses)
    high=[transaction for transaction in expenses if transaction['amount'] > avg]
    return high
def save_expenses(expenses):
    try:
        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)
    except OSError as e:
        print(f"Error saving expenses: {e}")
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: The expenses.json file is not in a valid JSON format.")
        return []
expenses = load_expenses()
while True:#main menu
    print("===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expense")
    print("4. Show Total Expense")
    print("5. Show Highest Expense")
    print("6. Show Lowest Expense")
    print("7. Show Average Expense")
    print("8. Show Expenses Above Average")
    print("9. Exit")
    print("---------------------------")
    try:
        choice = int(input("Please enter your choice "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if (choice == 1):
        key = input("Enter Expense category ")
        key = key.strip()  # Remove leading and trailing whitespace
        if key.isdigit():
            print("Category cannot be a number. Please enter a valid category.")
            continue
        if not key.strip():
            print("Category cannot be empty. Please enter a valid category.")
            continue
        try:
            value = int(input("Enter the amount spent "))
            if value <= 0:
                print("Amount cannot be negative or zero. Please enter a valid amount.")
                continue
            transaction = {"category": key, "amount": value}
            expenses.append(transaction)
            save_expenses(expenses)
            print("Expense added successfully.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif (choice == 2):
        if(len(expenses) > 0):
            for number, transaction in enumerate(expenses, start=1):
                print(f"{number}. Category: {transaction['category']}, Amount: {transaction['amount']}")
        else:
            print("No expense added yet")
    elif (choice == 3):
        search=input("Enter expense category to search:")
        search = search.strip()  # Remove leading and trailing whitespace
        match = filter(lambda item: search.lower() in item['category'].lower(), expenses)
        match_list = list(match)
        if match_list:
            for transaction in match_list:
                print(f"Category: {transaction['category']}, Amount: {transaction['amount']}")
        else:
            print("No matching expenses found.")
    elif (choice == 4):
        print(f"Total expenses is: {total_expense(expenses)}")
    elif (choice == 5):
        if(len(expenses) > 0):
            print(f"Highest expense is: {highest(expenses)}")
        else:
            print("No data entered")
    elif (choice == 6):
        if(len(expenses) > 0 ):
            print(f"Lowest expense is: {lowest(expenses)}")
        else:
            print("No data entered")
    elif (choice == 7):
        if(len(expenses) > 0):
            print(f"Average expense is: {average(expenses)}")
        else:
            print("No items in the cart")
    elif(choice == 8):
        print("Expenses above average:")
        high_expenses_dict = high_expenses(expenses)
        if high_expenses_dict:
            for transaction in high_expenses_dict:
                print(f"Category: {transaction['category']}, Amount: {transaction['amount']}")
        else:
            print("No expenses above average.")
    elif(choice == 9):
        break
    else:
        print("Incorrect Choice Number entered")
print("Thank you")#End of program