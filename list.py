# find the largest number in a list
# Enter the count
# get a list of multiple numbers
# sort list in ascending order
# the last number in the list is the largest number

num = int(input('Enter count on the list: '))
num_list = [] 

for i in range(num):
    user_input = int(input('Enter the number: '))
    num_list.append(user_input)
num_list.sort()
print('The largest number is: ',num_list[-1])


# count how many times a value appears in a list

# enter the count on the list
# create an empty list
# enter the target value
# set count = 0
# iterate though each number on the list
# for that range, if the target value appers on the list, increase the count

list_count = int(input('Enter the numbers of count on the list: '))
target_value = int(input('What is your target value you are looking for in a list? '))
count = 0
for i in range(list_count):
    user_input = int(input('Enter the number: '))
    if target_value == user_input:
       count +=1
print('The target value appears: ', count, 'times')


# find duplicates in a list

# enter the user count on the list
# set initial count to 0 
# use set to eliminate duplicate on list
# iterate through each element in the list, starting at i if i appears any where in the list, increase the count

list_count = int(input('Enter the count on the list: ')) # ask user how many times they want to enter number in list
num_seen = set() # set to store the number seen in each iteration
duplicates = set() # set to store the duplicate value

for i in range(list_count):
    user_input = int(input('Enter the number: '))
    if user_input in num_seen: # checks if the number already exists before
       duplicates.add(user_input) # add to the duplicate set
    else:
      num_seen.add(user_input) # stores in seen set
print('The duplicate list is: ', list(duplicates) )


# Return the largest number in a list

count = int(input("How many numbers? "))
numbers = [] # empty list 

for i in range(count):
    value = int(input("Enter a number: "))
    numbers.append(value)

print("Largest number is:", max(numbers)) # max function