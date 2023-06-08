# Write a shopping game where a player will start by
# setting how much they want to spend in our shop with
# maximum spend limit of 5000 naira.
# Players will then be presented with a list of items one
# by one for them to choose from.
# They must not buy more than 5 items.
# If a player spends all their money by the end of the game
# they win, otherwise they can choose to play again or
# its game over.


# pseudocode
"""
Welcome players to the game
print("Welcome")
we need the name of the player
name = input("Enter name")
We need player spend limit
playerlimit = input("How to spend?")
we need to max spend limit to 5000
maximumspendlimit = 5000
we need the list of items
items = [{'name':'A', 'price':2}]
we need a way to keep track of what players are buying
tracker = 0
spent = 0
we need a way to show items one by one
for item in items:
    players must not buy more than 5 items
    if tracker < 5:
        # we meed a way to let plauers select items
        response = input("Wanna buy {} for {}".format(
            item.get('name'), item.get('price')))
        if response == 'y':
            tracker +=1
            spent +=item.get('price')
We need a way to check if the spendlimit is the same as what the player spent
if playerlimit == spent:
    print("You won)
else:
    print("Game over")
if they are the same the player wins otherwise they loose
"""


# pseudocode
"""
I need a player
there is a spend limit of 5000
there will be player limit
the game depends on the spend limit
I need a list of products
i need name and price for a product
I need to iterate through my products
then show the player
the player needs a way to select a product
I need to keep track of their purchases
I need to check their total spendings
over their chosen spend limit
"""

# psuedocode with implementation embeded
"""
I need a player
player = input("Hey player whats your name? ")
there is a spend limit of 5000
spendlimit = 5000
there will be player limit
playerlimit = input("Hey player how much are you spending?")
the game depends on the spend limit
if spendlimit <= playerlimit:
    player the game here
    =====================
    I need to keep track of their purchases
    purchases = []
    I need a list of products
    i need name and price for a product
    products = [{'Coke':10},'Fanta':5,'IceCream':90]
    I need to iterate through my products
    then show the player
    for product in products:
        they player must not buy more than 5 products
        if len(purchased) < 5:
            the player needs a way to select a product
            selection = input("Are you interested in buying {} at {} | yes or no?".format(
                product.get('name'), product.get('price')))
            purchases.append(product)
    I need to check their total spendings
    spent = 0
    for item in purchased:
        spent+=item.get('price')
    over their chosen spend limit
    if spent == playerlimt:
        print('Good')
otherwise the game ends here
    else:
        print("game over")
"""


import random
print("--------- SHOPPING GAME ---------")
print("\nInstructions:\nSpend Limit: 5000\nTo select a product when displayed type 'yes'\nTo skip a product when displayed type 'no'\n")
spend_limit = 5000
name = input("Please enter your name to start: ")
player_spend_limit = input(
    "Alright {}, how much do you want to spend? ".format(name))

shop = [
    {"name": "Coke", "price": 250},
    {"name": "Pepsi", "price": 150},
    {"name": "Sprite", "price": 100},
    {"name": "Lacasera", "price": 200},
    {"name": "Bread", "price": 650},
    {"name": "Laptop", "price": 2450},
    {"name": "Fanta", "price": 200},
    {"name": "Cake", "price": 1500},
    {"name": "Water", "price": 100},
    {"name": "Yoghurt", "price": 750},
]

if spend_limit >= int(player_spend_limit):
    print("Great, your spend limit is set to {}".format(player_spend_limit))
    purchased = []
    spent = 0

    game_state = True
    while game_state:
        for product in shop:
            product = random.choice(shop)
            if len(purchased) < 2:
                response = input("\nProduct: {}\nPrice: {}\nDo you want this product? ".format(
                    product.get('name'), product.get('price')))
                if response == 'yes':
                    purchased.append(product)

        for item in purchased:
            spent += item.get('price')

            if spent == int(player_spend_limit):
                print("Congrats {}, you won!!!\nSpend Limit: {}\nAmount Spent: {}".format(
                    name, player_spend_limit, spent))

                # play_again = input("\nDo you want to play again? Yes or No? ")
                # if play_again.lower == 'no':
                #     game_state = False
            else:
                print("Better luck next time {}!!!\nSpend Limit: {}\nAmount Spent: {}".format(
                    name, player_spend_limit, spent))

                # play_again = input("\nDo you want to restart? Yes or No? ")
                # if play_again.lower == 'no':
                #     game_state = False
        else:
            print("Sorry you have to spend 5000 or less")
