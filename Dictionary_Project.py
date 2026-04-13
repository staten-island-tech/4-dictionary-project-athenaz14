items = [
{
    "name": "Pencil",
    "price": 2.00,
    "department": "Stationery",
    "description": "Writing/Drawing instrument with graphite."
    
},
{
    "name": "Eraser",
    "price": 1.00,
    "department": "Stationery",
    "description": "A tool to remove graphite."
},
{
"name": "Paper",
    "price": 2.00,
    "department": "Stationery",
    "description": "150 sheets of printer paper."
},
{
"name": "Marker",
    "price": 5.00,
    "department": "Stationery",
    "description": "Felt tip pen."

},
{
"name": "Pen",
    "price": 1.50,
    "department": "Stationery",
    "description": "Writing/Drawing Instrument with ink."
},
{
"name": "Looseleaf",
    "price": 1.50,
    "department": "Stationery",
    "description": "A sheet with three holes punched"
}
]
prices = []
cart = []
total_cost = 0
shop = True
for index, item in enumerate(items): 
    print(index, ":", item["name"],item["price"])

while shop: 
    purchase = int(input("Do you want add of items to your cart?")) 
    cart.append(items[purchase]["name"]) 
    prices.append(items[purchase]["price"]) 
    continue_shopping = input("Do you want to continue to shop? Enter y or n") 
    if continue_shopping == "n": 
        shop = False
for item in cart: 
    print(f"{cart}")
for price in prices: 
    total_cost += price
    print(f"{cart, total_cost}")
    
""" while True: purchase =(input("Do you want add of items to your cart? Enter s to quit")) if purchase == "s": break elif item == purchase: cart.append(items["name"]) prices.append(items["price"]) for item in cart: print(f"{item["name"]}") total+=item["price"] print(total) """
""" def cart(items):
    purchase =(input("Do you want add of items to your cart? Enter s to quit"))
    prices = []
    cart = []
    total = 0
    while True:
        if purchase == "s":
            break
        else:
            cart.append(item["name"])
            prices.append(item["price"])
 """


        


""" while purchase == item:
        print(f"You added {purchase} to cart!")
        purchase.append(item)
        purchase =(input("Any additional items?"))
        if purchase == item:
      print("Finished with shopping")
 """

