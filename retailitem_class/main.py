#
# Christian Espinoza Celis 
# 2/9/2025
# RetailItem Class Programming Project
# SDEV 1200
#
# Use comments liberally throughout the program. 


class RetailItem:

    def __init__(object, description, units_in_inventory, price):
        object.description = description
        object.units_in_inventory = units_in_inventory
        object.price = price

    def displayItemInfo(self):
        print(f'{self.description} \t {self.units_in_inventory} \t ${self.price}')

itemOne = RetailItem("Jacket", 12, 59.95)

itemTwo = RetailItem("Designer Jeans", 40, 34.95)

itemThree = RetailItem("Shirt", 20, 24.95)

itemOne.displayItemInfo()
itemTwo.displayItemInfo()
itemThree.displayItemInfo()
