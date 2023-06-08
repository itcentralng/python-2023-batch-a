# Assignment

"""
Write a state and capital game
Users are prompted with a name of
a state for which to provide the
capital.
The games runs on an endless loop
until all the states have been used
or the user chooses to 'quit'

The whole game should start when a function
is called. For example stateAndCapital() ==> game starts
"""


def stateAndCapital():
    states = [
        {"state": "Abia", "capital": "Umuahia"},
        {"state": "Adamawa", "capital": "Yola"},
        {"state": "Akwa Ibom", "capital": "Uyo"},
        {"state": "Anambra", "capital": "Awka"},
        {"state": "Bauchi", "capital": "Bauchi"},
        {"state": "Bayelsa", "capital": "Yenagoa"},
        {"state": "Benue", "capital": "Makurdi"},
        {"state": "Borno", "capital": "Maiduguri"},
    ]

    while True:
        print("Welcome to the state and capital game\n")
        ran_state = random.choice(states)

        state_name = ran_state.get("state")
        capital = input("Enter the capital of {}: ".format(state_name))

        if capital.lower() == ran_state.get("capital").lower():
            print("Correct! Well done\n")
        else:
            print("Opps! Wrong answer. The correct answer is {}\n".format(
                ran_state.get("capital")))


stateAndCapital()
