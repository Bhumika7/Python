#Ask the user for their age and print whether they are allowed to vote

Age = float(input('What is your Age?'))

if Age >= 18:
  print('You are allowed to vote')
else:
  print('')

#Tip calculator: Ask the user for the bill amount and tip percentage, then print the tip
#amount and total bill

bill_amount = float(input('Please enter the bill amount'))
tip_percentage = float(input('Please enter the tip percentage'))

tip_amount = ((tip_percentage / 100) * bill_amount)
total_bill = (bill_amount + tip_amount)

print('The total tip amount is', tip_amount)
print('The total bill amount is', total_bill)


#Bill splitter: Ask the user for the total bill, tip percentage, and number of people, then 
#print how much each person should pay

bill_amount = float(input('Please enter the bill amount'))
tip_percentage = float(input('Please enter the tip percentage'))
total_people = int(input('Enter total number of people'))

tip_amount = ((tip_percentage / 100) * bill_amount)
total_bill =  (bill_amount + tip_amount)
each_person = total_bill / total_people
print('Each person pays', each_person)
"""
