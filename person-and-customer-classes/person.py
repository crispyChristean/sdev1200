#
# Christian Espinoza Celis 2/26/2025
# Date
# Person and Customer Classes Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.

class Person:
    def __init__(self, name, address, number):
        self.__name = name
        self.__address = address
        self.__number = number
    
    def set_name(self, name):
        self.__name = name 

    def set_address(self, address):
        self.__address = address
    
    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address
    
    def get_number(self):
        return self.__number
    

class Customer(Person):
    def __init__(self, name, address, number, customer_number, mailing_list):

        Person.__init__(self, name, address, number)

        self.__customer_number = customer_number
        self.__mailing_list = mailing_list 

    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number

    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list

    
    def get_customer_number(self):
        return self.__customer_number

    def get_mailing_list(self):
        return self.__mailing_list 