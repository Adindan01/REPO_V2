# showing basically nothing

import sys
import random

while True:
    user_action = input("Pick one (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, and the computer chose {computer_action}!\n")

    if user_action == computer_action:
        print(f"Both players picked {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! LETS GO!!! YOU WIN!!!")
        else:
            print("Paper covers rock! GET REKT NERD!!!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! YOU WIN!!!")
        else:
            print("Scissors cuts paper! I'd probably stop if I lost like that.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! YOU GOT EM'!")
        else:
            print("Rock smashes scissors! Better luck next time, loser.")

    play_again = input("Play again? (y/n): ")
    if  play_again.lower() != "y":
            sys.exit()
    

# ROCK, PAPER, SCISSORS!


