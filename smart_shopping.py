print("====== SMART SHOPPING CART ======")
name = input("Please enter your name: ")#Customer details
print("Name of customer:",name)
print("Customer name in uppercase:",name.upper())
print("Customer name in lowercase:",name.lower())
cart=[]
print("Enter 5 Items into your shopping cart")
cart.append(input("Enter 1st item "))# Add item
cart.append(input("Enter 2nd item "))
cart.append(input("Enter 3rd item "))
cart.append(input("Enter 4th item "))
cart.append(input("Enter 5th item "))
print("Your Shopping cart is ",cart)
print("Total Items in the cart is ",len(cart))
print("1st Item in the cart is:",cart[0])
print("Last Item in the cart is:",cart[-1])
choice=input("Do you want to remove an item from the cart? (yes/no) ")#Asking for removal of item
if(choice.lower() == "yes"):
    item=input("Name the item you want to remove ")
    if(item in cart):
        cart.remove(item)
        print("Here is the updated cart:",cart)
    else:
        print("Item not found in cart")
else:
    print("No changes in the original cart")
choice=input("Do you want to add an item in the cart? (yes/no) ")#Asking for addition of item
if(choice.lower() == "yes"):
    item=input("Name the item you want to add ")
    cart.append(item)
    print("Here is the final updated cart:",cart)   
else:
    print("This is your final cart:",cart)
print("Here is your shopping list arranged in alphabetical order:",sorted(cart))
print("Here is your shopping list arranged in reverse alphabetical order:",sorted(cart, reverse=True))
final=tuple(cart)#Final Cart that now cannot be modified
print("Final Shopping Record:", final)
print("\n====== SHOPPING SUMMARY ======")
print("Customer Name:", name)
print("Total Items Purchased:", len(cart))
print("Final Shopping Record:", final)
print("Thank you for shopping!")
print("Visit Again!")