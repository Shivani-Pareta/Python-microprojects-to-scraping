##The following code is good to understand how to access items in a dictionary and play around with that
# print("-"*30)

# grocery_list={
#     "Apple": 150,
#     "Banana" : 40,
#     "Potato" : 30,
#     "Tomato" : 60,
#     "Bread" : 40,
#     "Eggs" : 200,
#     "Onion" : 50
# }

# total_bill = 0

# print(f"\n-----Generating the receipt-----")

# for item_name,price in grocery_list.items():
#     print(f"\n {item_name} : ₹{price}* input(quantity)")
#     total_bill +=price

# print("-"*30)
# print(f"total amount to be paid:{total_bill}")
# print("-"*30)





## Let's take it up a nothc and try to incorporate the actual factor of quantity like in a grocery list
#this will take taking inputs on the quantity that is required
#printing the quantity item and price in the final receipt after taking the input
#producing the final number/amount to be paid 


print("-"*30)

grocery_list={
    "Apple": 150,
    "Banana" : 40,
    "Potato" : 30,
    "Tomato" : 60,
    "Bread" : 40,
    "Eggs" : 200,
    "Onion" : 50
}

total_bill = 0

receipt_lines = []

print(f"\n-----Taking your order-----")

for item_name,price in grocery_list.items():

    quantity_input= input(f"\nHow many items of {item_name} would you like ?: ")
    quantity = int(quantity_input)

    item_total = price * quantity
    total_bill +=item_total
    receipt_lines.append(f"-> {quantity} * {item_name} : ₹{item_total}")

#for presentation purposes
print("\n" + "=" * 30)
print("          FINAL RECEIPT")
print("=" * 30)

for lines in receipt_lines:
    print(lines)

# print(f"\n -> {quantity} * {item_name} : ₹{item_total}")

print("-"*30)
print(f"total amount to be paid:{total_bill}")
print("-"*30)
