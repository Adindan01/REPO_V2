# Rock, Paper, Scissors game
import random
import sys

actions = {
    1 : "rock",
    2 : "paper",
    3 : "scissors"
}
computer_action = random.choice(actions)

# Outline for what the user can choose, and how the computer's choices are randomized
user_action = input("Enter a choice (rock, paper, scissors): ")
while user_action == len[1-3](actions):
    continue
else:
    print("I didnt quite catch that. Please type rock, paper, or scissors, and don't forget to use lowercase!")
    sys.end()

# Initial prompt for the user input and the computer's resulting choice
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

while user_action == ("rock", "paper", "scissors") == True: 
    
    while True:

        # Tie result
        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        
        # Rock win condition
        if user_action == "rock" and computer_action == "scissors":
            print("Rock smashes scissors! You win!!!")
    
        # Paper win condition
        if user_action == "paper" and computer_action == "rock":
            print("Paper covers rock! You win!!!")
        
        # Scissors win condition
        elif user_action == "scissors" and computer_action == "rock":
            print("Rock smashes scissors! You lose.")


        
        #while user_action == ("rock", "paper", "scissors"):
#    continue
#if user_action != ("rock", "paper", "scissors"):
 #   quit
  #  input("I didnt quite catch that. Please type ""rock,"" paper,"" or ""scissors,"" and don't forget to use lowercase!")