#The menu of resturant
menu  = {
    "Pizza" : 30,
    "Dal Baati": 60,
    "Pasta":35,
    "Burger" : 45,
    "Coffee" : 70,
}

print("welcome to YM resturant")
print("Pizza:30\nDalBaati :60\nPasta :35\nBuger :45\nCoffee :70")

order_total = 0
#80 + 70 = 150

item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1] #0 + 50
    print(f"Your item {item_1} has been added to your order")
    
else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No) ") 
if another_order == "Yes":
    item_2 = input("Enter the name of second item =") 
    if item_2 in menu:
        order_total += menu[item_2]
        print("Item {item_2} has been added to order")
    else:
        print("Ordered item {item_2} is not available!")          

print(f"The total amount of items to pay is {order_total}")        
        