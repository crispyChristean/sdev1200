#
# Christian Espinoza Abraham Espinoza Espinoza Celis Christian 
# 011111/34/t8ie59yjiosklgnsokdfgko;n;dfklgnkldsnfgnd
# Rock, Paper, Scissors Game Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 
import random 
from tkinter import *


#Funtion decides what to assign the computer.
def decideChoice(given):
    if given == 1:
        given = "paper"
    if given == 2:
        given = "rock"
    if given == 3:
        given = "scissors"
    return given

#Function makes the string match the computer's wording.
def cleanString(given):
    given = given.casefold()
    for i in given:
        if i.isspace() == True:
            given = given.replace(" ", "")
    if given.isalpha == False:
        print("Sorry, input is invalid, please en-enter")
    else:
        return given
#Function decides winner via matching arrays.
def decideWinner(comp, user):

    place = [comp, user]
    checker = [
            #Index 0
            [ 
                ["rock", "rock"], 
                ["paper", "paper"],
                ["scissors", "scissors"] 
            ],
            #Index 1
            [ 
                ["rock", "scissors"], 
                ["paper","rock"], 
                ["scissors", "paper"] 
            ],
            #index 2
            [ 
                ["rock", "paper"], 
                ["paper", "scissors"], 
                ["scissors", "rock"]
            ]
        
        ]
    print(f'The computer chose: {comp}\nThe player chose: {user}') #Show choices

    # print(place) - Working correctly
    # print(checker)- Working correctly.

    #Checks if it's a draw, does so by checking array pairs to see if one matches. Checking 2D arrays for matches.
    for i in checker[0]:
        if place == i:
            print("It's a Draw!")

    #Checks to see if there's a computer win. Every Scenario in this 2D array is the computer winning.
    for i in checker[1]:
        if place == i:
            print("Alas, you've been bested by the computer! Computer Wins!")
    #Checks to see if there is a user win. Every Scenario is for that of the user.
    for i in checker[2]:
        if place == i:
            print("Congratulations! You've won over the computer!")

#Program starts here.
computersSelection = random.randint(1,3)
# print(computersSelection) -Working correctly

#Once the number is generated, the number is then changed into text.
computersSelection = decideChoice(computersSelection)
# print(computersSelection) - working correctly 

#User then decides what to pick.
usersChoice = input("Welcome to Rock-Paper-Scissors, please enter one: ")

#the program then checks if there is any spaces and changes lettering. Also checks if its valid.
usersChoice = cleanString(usersChoice)

# print(usersChoice) - working correctly.
#Then the program calls the funtion that'll determine a winner.
decideWinner(computersSelection, usersChoice)
