# Customer pick cheap products, shop has a list of items each with its name, price and brand.
# The customer only has 50 naira to spent and is looking to buy up to 5 products.

stocks = [
    {"name": "Milk", "price": 20, "brand": "Peak"},
    {"name": "Bread", "price": 50, "brand": "Dangote"},
    {"name": "Eggs", "price": 2, "brand": "Golden Penny"},
    {"name": "Sugar", "price": 10, "brand": "Dangote"},
    {"name": "Salt", "price": 5, "brand": "Dangote"},
    {"name": "Rice", "price": 3, "brand": "Royal Stallion"},
    {"name": "Beans", "price": 8, "brand": "Golden Penny"},
]

# sort the list of items by price
#  stocks.sort(key=lambda x: x.get("price"))
spent_limit = 50

for i in stocks:
    if i.get("price") <= spent_limit:
        spent_limit -= i.get("price")
        if spent_limit >= 0:
            print(i.get("name"), "\tCost\t", i.get("price"))
        else:
            print("Sorry, you cannot afford any of the products")

print("####################\n")

# Write a shopping game where a player will start by
# setting how much they want to spend in our shop
spend_limit = int(input("How much do you want to spend? "))

# with maximum spend limit of 5000 naira.
if spend_limit > 5000:
    print("Sorry, you cannot spend more than 5000 naira")
    exit()

# Players will then be presented with a list of items one by one for them to choose from.

purchasable_items = [
    {"name": "Milk", "price": 1200},
    {"name": "Bread", "price": 600},
    {"name": "Eggs", "price": 1500},
    {"name": "Sugar", "price": 700},
    {"name": "Salt", "price": 200},
    {"name": "Rice", "price": 700},
    {"name": "Beans", "price": 950},
]

print(purchasable_items)

# They must not buy more than 5 items. If a player spends all their money buy the end of the game
# they win, otherwise they can choose to play again or its game over.

purchased_items = []
for item in purchasable_items:
    print("Do you want to buy", item.get("name"), "?")
    answer = input("Yes or No: ")

    if answer.lower() == "yes":
        if item.get("price") <= spend_limit:
            purchased_items.append(item)
            spend_limit -= item.get("price")

print(purchased_items)
