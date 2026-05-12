# reverse a string

Slicing in str class

obj[start:]: Everything from start to the end.

obj[:stop]: Everything from the beginning up to (but not including) stop.

obj[1:4]: Elements at index 1, 2, and 3.

obj[::2]: Every second element (stepping by 2).

obj[1::-1]: Starts at index 1 and goes backward (returns the first two elements reversed).


# reverse a string
string = 'World'
reversed_string = string[: : -1] # starts at from start to end, and reversed by 1 each time
print(reversed_string)


# count vowels in a string
string = str(input('Enter a string: '))
vowel = {'a', 'e', 'i', 'o', 'u'}
i = 0
for char in (string): #iterate over each char in string
  if char.lower() in vowel: # lower cased the input 
    i +=1 # increment by 1 each time 

print('Total Vowels: ',i)


#count how many times a character appears

word = str(input('Enter a word:', ))
character = str(input('Enter a charecter:', ))
count = 0

for char in word:
  if char == character:
    count +=1

print("The charecter appers: ", count )


# Palindrome checker: Ask the user for a word or phrase and return whether it is a palindrome

input_text = input("Enter a word or phrase: ")

clean_text = input_text.replace(" ", "").lower() # Removes space and makes lowercase
reverse_text = clean_text[::-1] # Reverse the text
if clean_text == reverse_text:  # Check if palindrome
    print("It is a palindrome")
else:
    print("It is not a palindrome")