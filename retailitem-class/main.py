#
# Christian Espinoza Celis 
# 2/9/2025
# RetailItem Class Programming Project
# SDEV 1200
#
# Use comments liberally throughout the program. 

#import the retail Item 
#import 

from RetailItem import RetailItem 
from cash_register import CashRegister


def displayOptions():
    print(f'Item \t\t Stock \t\t Price')
    item_one.displayItemInfo()
    item_two.displayItemInfo()
    item_three.displayItemInfo()
    item_four.displayItemInfo()
    item_five.displayItemInfo()
    item_six.displayItemInfo()

def cleanString(givenString):
        givenString = givenString.casefold()
        for i in givenString:
            if i.isspace() == True:
                givenString = givenString.replace(" ", "")
        return givenString

def decidingPurchase(given):
    if given == 'one':
        firstRegister.purchase_item(item_one)
    elif given == 'two':
        firstRegister.purchase_item(item_two)
    elif given == 'three': 
        firstRegister.purchase_item(item_three)
    elif given == 'four':
         firstRegister.purchase_item(item_four)
    elif given == 'five':
         firstRegister.purchase_item(item_five)
    elif given =="six":
         firstRegister.purchase_item(item_six)
    elif given == "seven":
         firstRegister.purchase_item(item_seven)
    else:
         print("Not a valid Option")

#Program starts here
selected = ''

item_one = RetailItem("One: Jacket", 12, 59.95)

item_two = RetailItem("Two: Designer Jeans", 40, 34.95)

item_three = RetailItem("Three: Shirt", 20, 24.95)

item_four = RetailItem("Four: Necklace", 34, 20.99)

item_five = RetailItem("Five: Gloves", 100, 35.78)

item_six = RetailItem("Six: Bracelet", 75, 12.93)

item_seven = RetailItem("Seven: Eagles Hat", 356, 129.47)

#Displays the data in each item object.
displayOptions()
print('\n')

#THE cash-register part of the assignment for WEEK/MODULE 5 starts here
#create the object that's based off the cashregister class. Containing all its properties and methods.
firstRegister = CashRegister()
#Create a while loop that ask for the user to select a product.
while selected != "exit":
    selected = input("Hello! Please type the number (as a letter)\nOR enter 'exit' to end shopping: ")
    selected = cleanString(selected)
    if selected == 'exit':
            break
    else:
        decidingPurchase(selected)

#integrate all the item objects into the cash Register

#Retrieves all the item descriptions from the list containing the item objects. Superior to the first
firstRegister.checkout()
