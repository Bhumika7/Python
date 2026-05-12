

#1. Print numbers 1 through 20
for number in range(1, 21):
  print('Number is:',number)

#2. Print all even numbers from 1 to 20

for number in range(2, 21, 2): # without if statement, jumps by 2 each time with last argument. 
  print(number)


#3. Ask the user for a word and print each character on its own line

character_String = input('Enter a word:' )
for char in character_String:
    print(char)



#4. Coin flip simulator: Ask the user how many times to flip a coin, simulate the flips, and
#print the total heads and tails

import random # random module, choice comes with random

def flip_coin():  # defines a function 
  return random.choice(['heads', 'tails']) # picks one of each and return it to a function

# Get user input
num_flips = int(input("Enter the number of flips:")) 

total_heads = 0 # these are the scoreboard and starts at 0 before we begin flipping
total_tails = 0

# Run the simulation 
for i in range(num_flips): # this is a loop, this runs untill the intended number of flips "num_flips"
  if (flip_coin() == 'heads'): # if it is a head, condition is true we add 1 to the scoreboard else we add 1 to the tails
    total_heads += 1
  else:
    total_tails += 1

print("Total no of heads:",total_heads)
print("Total no of tails:",total_tails)


import random #to generate random data 

#5. Simple number guessing game: Randomly choose a number and ask the user to
#guess until they get it right

secret_num = random.randint(1, 10) # picks one random number from 1 to 10 
while True:
  user_choice = int(input('Choose a number from 1 to 10:')) # displays the message to the user to choose a number


  if user_choice > secret_num:
    print ('Guess lower')

  elif user_choice < secret_num:
    print ('Guess higher')

  else:
    print('Your guess is correct, it was',secret_num)

    break

   











