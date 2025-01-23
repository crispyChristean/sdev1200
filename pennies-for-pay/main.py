#
# Christian Espinoza
# 1/20/2025
# Pennies for Pay Programming Project
# SDEV 1200 
#

# Use comments liberally throughout the program.

#Import a module that allow for creating tables. 

#As a note, I had to install the tabulate module by going to the powershell in windows, this involved opening the terminal and entering "pip install tabulate" 

#Mistake I made: Trying to make a 2-D array but just placing only the first and second array,didn't work and only really "combined" both arrays. 
from tabulate import tabulate

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
roughDraft = []
#An array that will be 2-Dimensional and the final array.
finalDraft = []

#For the first loop, we take the given input, add one (becuase of how iterations work in python), set that as our condition for the amount of times. 
#Within the loop, we append the current value we are sitting at, starting from 0, to the array holding the days. 
#NEXT, we add the current value of pennies to the array holding its total. 
#AFTER, we add then double the amount of pennies. Then the loop repeats. This has to be done at the end otherwise the values are messeed up.
for iteration in range(amountOfDay+1): 
    creatingDays.append(iteration)
    creatingAmounts.append(amountOfPennies)
    amountOfPennies *= 2

#In this loop, we are setting up the 2-D array. I decided on this approach cause I didn't want to erase my old code.
#Starting the range by using either  array holding the days or total pennies, since both lengths are the same
#FIRST, we add the the value of day and what value it calls from the iteration (retreiving values by index and iteration manipulation) into the empty array.
#SECOND, we do the same again, however in this case we are converting a float to a string and calling the index by iteration in a f string, this allows us to format how it looks.
#LASTLY, we then add the new array holding the two values, and add that to the final array, which after doing so we declare the other array as empty and repeat the process.
for iteration2 in range(len(creatingDays)):
    roughDraft.append(creatingDays[iteration2])
    roughDraft.append(f'${creatingAmounts[iteration2]:.2f}')
    finalDraft.append(roughDraft)
    roughDraft = []


#Heading for the table.
head = ["Number of Days", "Penny Amount"]

#Checking Arrays 

#print(creatingDays)
#print(creatingAmounts)
#print("\n")
#print(finalDraft)

#Gives the Table Format that is desired, as specified in the instructions. 
print(tabulate(finalDraft, headers=head, tablefmt="grid"))
