menu = {
    'Panneer Butter masala': 140,
    'Butter roti': 20,
    'Burger': 60,
    'Sandwich': 70,
    'Veg noodles': 80
}

print("Welcome to the restaurant")
print("Panneer Butter masala: Rs140\nButter roti: Rs20\nBurger: Rs60\nSandwich: Rs70\nVeg noodles: Rs80\n")
Order_total = 0

FOODITEM_1 = input("Enter the Food item name here: ")
if FOODITEM_1 in menu:
    Order_total += menu[FOODITEM_1]
    print(f"Your item {FOODITEM_1} has been added to the order")
else:
    print(f"Ordered item {FOODITEM_1} is not available in our restaurant")

NEXT_ORDER = input("Do you want to add another item? (YES/NO): ").upper()
if NEXT_ORDER == 'YES':
    FOODITEM_2 = input("Enter the Food item here: ")
    if FOODITEM_2 in menu:
        Order_total += menu[FOODITEM_2]
        print(f"Your item {FOODITEM_2} has been added to the order")
    else:
        print(f"Ordered item {FOODITEM_2} is not available in our restaurant")

print(f"The total bill of the order is Rs{Order_total}")
