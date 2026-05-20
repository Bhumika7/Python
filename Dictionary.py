
# character frequency count
word = 'Bhumika' # create a variable called 'word' which contains string 'Bhumika'
freq = {} # create a empty dictionary called freq

for char in word: # loop through each character in the word 
  if char in freq: # if the selected char exist already in the empty dictionary called freq, 
    freq[char] += 1 # add frequency of the character to 1 to the existing freq 
  else:
    freq[char] = 1 # else add 1 to the empty dict

print(freq) # print freq of all the character in the string called Bhumika 


# word frequency count

words = 'Apple Ball Cat Dog Dog'
word_list = words.split() # splits the string into a list of word
word_freq = {} # empty dict to count freq

for word in word_list:
  if word in word_freq:
    word_freq[word] += 1 #increases he count for specific word(key) by 1 
  
  else:
    word_freq[word] = 1 # adds one

print(word_freq)

# count numbers in a list
# problem statement : Count how many time number appears in a list basically frequency of a number
count = int(input('Enter the count: '))
num_freq = {}
for i in range(count):
    number = int(input('Enter the list of numbers: '))
    if number in num_freq:
      num_freq[number] +=1
    else:
       num_freq[number] = 1
print(num_freq)


# Word counter: Ask the user for a string and print the number of words and the
# frequency of each character

text = str(input('Enter a string: '))
freq = {}

for char in text:
  if char in freq:
    freq[char] +=1

  else:
    freq[char] = 1
print('Count word: ', len(text.split())) #.split() breaks the string in spaces and turns it into list of words with comma
print(freq)

# Count how many times each word appears in a sentence

sentence = str(input('Enter a sentence: '))
freq_word = {}

for word in sentence.split():
  if word in freq_word:
    freq_word[word] +=1
  else:
    freq_word[word] = 1

print(freq_word)


# Count how many times each number appears in a list

count = int(input('Enter the count: '))
num_freq = {}

for i in range(count):
  num = int(input('Enter a number: '))
  if num in num_freq:
    num_freq[num] +=1
  else:
    num_freq[num] = 1

print(num_freq)


# Return the first duplicate value in a list if one exists
the_list = [1, 3, 1, 4, 5] # creates a list
seen = set() # empty set to store seen value, no need for duplicate set as we are only looking for first duplicate


for num in the_list: 
  if num in seen:
    print('duplicate:', num)
    break
  else:
    seen.add(num)

  





