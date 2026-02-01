#Exercise 4 - Bakery Menu and Stock
#Restarted to polish coding and do comparison

#Step 1 - create menu; price and stock

menu = {
  'bread': {'price': 3, 'stock': 10},
  'muffin': {'price': 4, 'stock': 5},
  'cookie': {'price': 2, 'stock': 20}
}

#Step 2 - initial total price
price_total = 0

#Welcome message
#\n is make print in a row
print("Welcome! Type 'done' when finished.\n")

#Step 3 - start order loop

while True:
  order = input("What do you want to order? Type 'done if finished': ").lower()

  #Exit
  if order == 'done':
    break #Stop order loop if condition is met

  #Check item is on menu
  #use 'not in' instead of 'in' this time
  if order not in menu:
    print(f"Sorry {order} is not in menu. Try again.")
    continue #Ask again

  #Ask for order amount
  while True:
    try: #might be wrong input, don't crash
      order_amount = int(input(f"How many {order} do you want?: ")) 
    except ValueError: #if convert int fails, dont crash and ask again
      print("Try again using numbers")
      continue

    #Check stock and calculate price
    if order_amount <= menu[order]['stock']:
      
    #deduct stock and add total to price
      menu[order]['stock'] -= order_amount
      price_total += order_amount * menu[order]['price']

      print(f"Added {order_amount} {order} to your cart.")
      print(f"{order} left in stock: {menu[order]['stock']}\n")

      break #exit order amount loop

    else: #if the order goes more than current stock available
      print(f"Sorry, only {menu[order]['stock']} {order}(s) available.")

#step 4 - print final total
print(f"\nYour final total is RM{price_total}")
print("Thank you for your order!")
