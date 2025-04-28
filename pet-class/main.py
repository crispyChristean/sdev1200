#
# Christian Epsinoza Celis 
# 2/9/2025
# Pet Class Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 

import pet

name = input("What is your pets name: ")
animal_type = input ("what type of animal is your pet: ")
age = input("How old is your pet: ")

my_pet = pet.pet(name, animal_type, age)

print("The myPet Object is createdd, let me show you each part: ")
print("Pet Name:", my_pet.get_name())
print("Animal Type:", my_pet.get_animal_type())
print("Pet's Age:", my_pet.get_age())