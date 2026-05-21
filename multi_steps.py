# 1. Rock, paper, scissors: Ask the user to choose rock, paper, or scissors, generate a
# random choice for the computer, and print the winner

# computer creates a random choice from three options and compares it with the user choice

import random

# ask the user for the choice

user_choice = str(input('rock, paper or scissors: '))

# list of choices 
choices = ['rock', 'paper', 'scissors']

computer_choice = random.choice(choices) # computer random choice

print('Computer choice is: ', computer_choice)

if computer_choice == user_choice:
    print("It's a tie!")

elif (
    (user_choice == "rock" and computer_choice == "scissors") or
    (user_choice == "paper" and computer_choice == "rock") or
    (user_choice == "scissors" and computer_choice == "paper")
):
    print("You win!")

elif user_choice in choices:
    print("Computer wins!")

else:
    print("Invalid choice, please choose rock, paper, or scissors.")