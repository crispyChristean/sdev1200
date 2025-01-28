#
# Christian Espinoza
# 1/20/2025
# Pennies for Pay Programming Project
# SDEV 1200 
#

# Use comments liberally throughout the program.

#User input that will be used when creating the table. 
amountOfDay = int(input("Please Enter the Number of Days being payed for in pennies: "))

#Starting value of the float, represents current amount of pennies.
amountOfPennies = .02

#Create the arrays. 
#Array that will be used to hold the amount of days.
creatingDays = []
#Array that will be used to hold the amount of pennies.
creatingAmounts = []
#An array that will be temporary hold single values from the previous two arrays.


#For the first loop, we take the given input, add one (becuase of how iterations work in python), set that as our condition for the amount of times. 
#Within the loop, we append the current value we are sitting at, starting from 0, to the array holding the days. 
#NEXT, we add the current value of pennies to the array holding its total. 
#AFTER, we add then double the amount of pennies. Then the loop repeats. This has to be done at the end otherwise the values are messeed up.
for iteration in range(amountOfDay+1): 
    creatingDays.append(iteration)
    creatingAmounts.append(amountOfPennies)
    amountOfPennies *= 2

#Uses another loop that represents each day indicated by a new line. Prints to console!
for i in range(len(creatingDays)):
    print('\n')
    print(f'Day: {creatingDays[i]} \t {creatingAmounts[i]}')
