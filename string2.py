# Reverse a string without using built-in reverse helpers

input_text = str(input('Enter a text: '))
reverse_text = input_text[::-1]
print(reverse_text)


# without using built_in reverse helpers

def text_reverse(r): # function takes parameter r
  reverse_text = ""  # to store reversed text while loop iterates through 
  for char in r:
    reverse_text = char + reverse_text # Adds the current charecter to the fron of the reversed text
  return reverse_text # returns the value back to where it was called 
input_text = str(input('Enter a text: '))
print(text_reverse(input_text)) # calls and prints



# Count the number of vowels in a string

text = str(input('Enter the text: '))
vowels = {'a', 'e', 'i', 'o', 'u'}
count = 0

for char in text.lower():
  if char in vowels:
    count +=1
  
print('Vowels: ',count, 'times')


# Check whether two words are anagrams - words or pharse formed by using char eactly once from other word or phrase
# 1. count the length of both words
# 2. count the frequency of the characters present
# sort the both words to know 1 and 2


def is_anagram(a, b):
      return sorted(a.lower()) == sorted(b.lower())

text1= str(input('Enter a word: '))
text2 = str(input('Enter anagram text: '))

print(is_anagram(text1, text2))




