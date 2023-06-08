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

import random

def playGame():

    states = [
        {"name":"Abia", "capital":"Umuahia"},
        {"name":"Adamawa", "capital":"Yola"},
        {"name":"Akwa Ibom", "capital":"Uyo"},
    ]

    playing = True

    used_states = []

    while playing:
        state = random.choice(states)
        if state not in used_states:
            used_states.append(state)
        response = input("What is the capital of {}? ".format(state.get('name')))
        if response == 'quit':
            playing = False
        else:
            if state.get('capital') == response:
                print("That's correct!")
            else:
                print("Oops! wrong, the capital of {} is {}".format(state.get('name'), state.get('capital')))
        if len(used_states) == len(states):
            playing = False 

playGame()