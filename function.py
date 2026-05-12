# a function that adds two numbers

def add(a, b):
  return a + b

result = add(2, 3)
print(result)

# a function that checks whether a number is even

def is_even(n):
  return n % 2 == 0
print(is_even(5))


# a function that returns the larger of two values

def large_value(a, b):
  
    if a > b:
      return a
    else:
      return b

num1 = int(input('enter a number a: '))
num2 = int(input('enter a number b: '))

result = large_value(num1, num2)

print('The large number is:',result)


# A function that takes a number and returns whether it is even

def is_even(n):

    if n % 2 == 0:
      return 'even'
    else:
      return 'odd'

num = int(input('Enter a number: '))

even_num = is_even(num)

print('The num is even: ', even_num)


# A function that takes a string and returns its length

def string_length(s):
      return len(s)
   
string = str(input('Enter string: '))
print('The length of the string is: ',string_length(string))



# A function that takes a number and returns whether it is even

def is_even(n):
  return n % 2 == 0
num = int(input('Enter a number:' ))
print(is_even(num))


#Calculator: Ask the user for two numbers and an operation (+, -, *, /) and print the result
#using functions

def operations(a, b, op):
    if op == '+':
      return(a + b)
    elif op == '-':
      return(a - b)
    elif op == '*':
      return(a * b)
    elif op == '/':
      if b!= 0:
        return(a / b)
      else:
        return "divided by 0 is infinite"
    else:
      "Invalid operation"
num1 = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))
operation = input('Enter operation: ')
print(operations(num1, num2, operation))

