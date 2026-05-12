# checking if a number is positive / negative / zero

x = float(input('Enter a number:'))
if x > 0:
  print('positive')
elif x<0:
  print('negative')
elif x==0:
  print('Zero')

#checking if a number is even or odd

y = int(input('Check even or odd:'))

if y%2 == 0:
  print('even')

else:
  print('odd')

#comparing two values
name = 'Bhumika'
print ('B' in name)


#Print your name, age, and favorite food
name = 'Bhumika Basnet'
Age = 25
favFood = "momo"
print('My name is: ',name, 'My fav food is:',favFood, 'My age is:',Age)


#Ask the user for two numbers and print their sum
x = float(input("Enter a number:"))
y = float(input("Enter another number:"))

print(x + y)

#Ask the user for a name and print a greeting
name = str(input('Write your name:'))
print("Hello", name)

