
class RetailItem:

    def __init__(object, description, units_in_inventory, price):
        object.description = description
        object.units_in_inventory = units_in_inventory
        object.price = price

    def displayItemInfo(self):
        print(f'{self.description} \t\t {self.units_in_inventory} \t\t ${self.price}')


itemOne = RetailItem("Jacket", 34, 56.89)