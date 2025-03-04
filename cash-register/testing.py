#Testing ground for the retailItem and cashregister assignments. Not intended for grading.
# Christian Espinoza Celis 
# 02/12/2024
# Cash Register Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 

#Gets the RetailItem class from the retailitem-class program 
#It is important to note that the file had to be renamed due to the use of a hyphen conflicting.




class RetailItem:

    def __init__(object, description, units_in_inventory, price):
        object.description = description
        object.units_in_inventory = units_in_inventory
        object.price = price

    def displayItemInfo(self):
        print(f'{self.description} \t {self.units_in_inventory} \t ${self.price}')



class CashRegister:
    #Basically when the class is called to create the object, the object will have the data and following methods automatically.
    def __init__(self):
        self.holdObjects = []
        self.holdDescriptions = []
        self.total = 0.0 

    #FOLLOWING METHODS FOR THE OBJECT TO USE:

    #A method named `purchase_item` that accepts a `RetailItem` object as an argument
    #Each time the `purchase_item` method is called, the `RetailItem` object that is passed as an argument should be added to the list.
    def purchase_item(self, givenObject):
        self.holdObjects.append(givenObject)
        self.holdDescriptions.append(givenObject.description)
        self.total += givenObject.price

    #Prints the objects, just a way to show that all the entered objects are present. 
    def get_objectList(self):
        print(self.holdObjects)

    #Prints the descriptions only. 
    def get_descriptions(self):
        print(f'Currently in Cart: ')
        for i in self.holdDescriptions:
            print(i)

    #Prints the total but doesn't return it. 
    def get_total(self):
        print(f'Total: ${self.total:.2f}')

    #Clears all the properties in the object. 
    def clear(self):
        self.holdObjects = []
        self.holdDescriptions = []
        self.total = 0.0 

#Gets the descriptions through the property holding all retail item objects. 
    def get_descriptions2(self):
        print(f'Current Items in the Cart: ')
        #Uses a for loop, each loop the object in the array will change and 
        #we have to specify that we want to retreive only the description property from each object within.
        for i in self.holdObjects:
            print(i.description)

#Gets the total from the property holding all the retail item objects. Returns a value at the end.
    def get_total2(self):
        #Make an accumulator 
        acc = 0 
        #Specify that we want to loop over the property (array) holding the retail objects. 
        for i in self.holdObjects:
            #specify that in each object we want to the price property of it.
            acc += i.price
        #Once it has recieved all prices, round from 2 decimal places. 
        acc = round(acc, 2)
        #return the variable.
        return acc
#A special function that utilizes two other methods. 
    def checkout(self):
        self.get_descriptions2()
        print(f'Total: ${self.get_total2()}')
        
            
#Program Starts Here 
#Creat the retail items as objects.
itemOne = RetailItem("Jacket", 12, 59.95)

itemTwo = RetailItem("Designer Jeans", 40, 34.95)

itemThree = RetailItem("Shirt", 20, 24.95)

#Create an object that utilizes the CashRegister class. Now contains all its properties and methods.
selected = CashRegister()
#Enter the objects into the other object that utilizes the cash register class. 
selected.purchase_item(itemOne)
selected.purchase_item(itemTwo)
selected.purchase_item(itemThree)
#Calling and testing functions 
selected.get_total()
selected.get_objectList()
selected.get_descriptions()
selected.get_descriptions2()
#selected.clear()
print('\n')
selected.checkout()
