#
# Christian Espinoza Celis 
# 02/9/2025
# Pet Class Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 


class pet:
#REMEMBER: the word "self" is just a placeholder for the object. 
    def __init__(self, name, animal_type, age):
        self.__name = name 
        self.__animal_type = animal_type 
        self.__age = age

#Function to set the name of the pet, when used it will need two parameters, the object and the name that will be integrated as a attribute.
    def set_name(self, name):
        self.__name = name
#Function to set the type of the pet used it will need two parameters, the object and the name that will be integrated as a attribute.
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type 
#Function to set the age the pet, when used it will need two parameters, the object and the name that will be integrated as a attribute.
    def set_age(self, age):
        self.__age = age


    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age