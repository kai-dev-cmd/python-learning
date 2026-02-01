# Exercise 4 - Bakery Menu and Stock (Version 1)

# Step 1 - create menu; price and stock
menu = {
    "bread": {"price": 3, "stock": 10},
    "muffin": {"price": 4, "stock": 5},
    "cookie": {"price": 2, "stock": 20}
}

# Step 2 - initial total price
price_total = 0

print("Welcome to the bakery!\n")

# Step 3 - ask for a valid order item
while True:
    order = input("What do you want?: ").lower()
    
    if order in menu:
        print(f"{order} is available!")
        break #use this if condition is met
      
    else: #if not in menu, print this
        print(f"{order} is not available. Please try again.")

# Step 4 - ask for amount and check stock
while True:
    try: #learned to use this so the program asks again instead of crashing if input is wrong
      #because if it is wrong, it will stop
        order_qty = int(input(f"How many {order} do you want?: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if order_qty <= menu[order]["stock"]:
        print(f"Your order for {order} is added to your cart.")
        break
    else:
        print(f"For {order}, we only have {menu[order]['stock']} left. Please try again.")

# Step 5 - order loop for additional orders
# while order != 'done' is needed for add on order
# but i can just use 'while True' next time and handle 'done' inside
while order != 'done':
    if order in menu:
        # Deduct stock and calculate total
        menu[order]["stock"] -= order_qty
        price_total += order_qty * menu[order]["price"]

        # Print
        print(f"Added {order_qty} {order}(s) to your cart.")
        print(f"{order} left in stock: {menu[order]['stock']}\n")
    else:
        print("Invalid item. Please choose from the menu.")

    # Ask for next order here
    order = input("Add on? (type 'done' to finish): ").lower()
    if order == 'done':
        break #stop if 'done'

    # Ask for amount again
    while True:
        try:
            order_qty = int(input(f"How many {order} do you want?: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if order_qty <= menu[order]["stock"]:
            break
        else:
            print(f"For {order}, we only have {menu[order]['stock']} left. Please try again.")

# Step 6 - print final total
print(f"\nYour final total is RM{price_total}")
print("Thank you for your order!")
