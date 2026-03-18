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


""" print(items[0]["name"])
for index, item in enumerate(items):
    print(index, ":", item["name"]) """
purchase =(int(input("Do you want add of items to your cart?")))
def shop(cart):
    purchase =(int(input("Do you want add of items to your cart?")))
    cart = []
    print(items)
