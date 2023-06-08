# # # ForLoop

# # numbers = [1, 2, 3]

# # # for "a variable" in "what your are iterating over":
# #     # what happens every time it loops

# # for number in numbers:
# #     if number % 2 != 0:
# #         print(number)

# # for alphabet in "ZAINAB":
# #     if alphabet in 'AIOEU':
# #         print(alphabet)

# # for name in ("Jamil", "Halima", "Late Commer"):
# #     if 'Late' not in name:
# #         print(name)

# # person = {'name':'James Aurthur', 'age':25}

# # for item in person:
# #     print(person.get(item))

# # Class Exercise

# # Write a program that helps a customer pick cheap products
# # from a certain shop. The shop has a list of items each
# # with its name, price and brand. The customer only has
# # 50 naira to spend and is looking to buy up to 5 products.

# shop = [
#     {"name": "Butter", "price": 200, "brand": "Blueband"},
#     {"name": "Cake", "price": 10, "brand": "Rahma Stores"},
#     {"name": "Bread", "price": 5, "brand": "Rahma Stores"},
#     {"name": "Banana", "price": 10, "brand": "Rahma Stores"},
#     {"name": "Pepsi", "price": 150, "brand": "Pepsi"},
#     {"name": "Coke", "price": 5, "brand": "Coca Cola"},
#     {"name": "Pure Water", "price": 20, "brand": "Coca Cola"},
#     {"name": "Ice Cream", "price": 200, "brand": "Kanti Plus"},
# ]

# money = 50

# purchased = []

# for item in shop:
#     if item.get('price') <= money:
#         purchased.append(item.get('name'))
#         money -= item.get('price')
# items = "\n".join(purchased)
# thanks = "Thank you for shopping with us\n"
# reciept = thanks+"Here are your items:\n"+items
# print(reciept)

# # Write a shopping game where a player will start by
# # setting how much they want to spend in our shop with
# # maximum spend limit of 5000 naira.
# # Players will then be presented with a list of items one
# # by one for them to choose from.
# # They must not buy more than 5 items.
# # If a player spends all their money buy the end of the game
# # they win, otherwise they can choose to play again or
# # its game over.

# WHILE LOOP

# one = 1
# zero = 0

# while one>zero:
#     one -= 1
#     print(1, 0)

# numbers = [1, 2]

# while len(numbers) < 5:
#     print(numbers)
#     numbers.append(numbers[-1]+1)

# Exercise

# Using while loop recreate the shopping game
# And allow the player to quit or restart the game at any time

# Correction
import random
print("--------- SHOPPING GAME ---------")
print("\nInstructions:\nSpend Limit: 5000\nTo select a product when displayed type 'yes'\nTo skip a product when displayed type 'no'")
spend_limit = 5000
name = input("Please enter your name to start: ")
player_spend_limit = input("Alright {}, how much do you want to spend?".format(name))

shop = [
    {"name":"Coke", "price":250},
    {"name":"Pepsi", "price":150},
    {"name":"Sprite", "price":100},
    {"name":"Lacasera", "price":200},
    {"name":"Bread", "price":650},
    {"name":"Laptop", "price":2450},
    {"name":"Fanta", "price":200},
    {"name":"Cake", "price":1500},
    {"name":"Water", "price":100},
    {"name":"Yoghurt", "price":750},
]

if spend_limit >= int(player_spend_limit):
    print("Great, your spend limit is set to {}".format(player_spend_limit))
    purchased = []
    spent = 0

    playing = True

    while playing:
        product = random.choice(shop)
        if len(purchased) < 5:
            response = input("\nProduct: {}\nPrice: {}\nDo you want this product? ".format(product.get('name'), product.get('price')))
            if response == 'yes':
                purchased.append(product)
            elif response == 'quit':
                playing = False
                print("Good bye {}".format(name))
            elif response == 'restart':
                purchased = []
                player_spend_limit = input("Alright {}, how much do you want to spend now?".format(name))
        else:
            
            for item in purchased:
                spent += item.get('price')
            
            if spent == int(player_spend_limit):
                print("Congrats {}, you won!!!\nSpend Limit: {}\nAmount Spent: {}".format(name, player_spend_limit, spent))
            else:
                print("Better luck next time {}!!!\nSpend Limit: {}\nAmount Spent: {}".format(name, player_spend_limit, spent))
            
            response = input("Want to play again? ")
            if response == 'no':
                playing = False
            else:
                purchased = []
                player_spend_limit = input("Alright {}, how much do you want to spend now?".format(name))
else:
    print("Sorry you have to spend 5000 or less")

# QUICK RECAP
