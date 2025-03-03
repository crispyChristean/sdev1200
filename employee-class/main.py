#
# Christian Espinoza Celis 
# 02/09/2025
# Employee Class Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.


class Employee:

    def __init__(objectPlaceHolder, name, identification, department, job_title):
        objectPlaceHolder.name = name
        objectPlaceHolder.identificaiton = identification
        objectPlaceHolder.department = department
        objectPlaceHolder.job_title = job_title 

    def displayEmployees(self):
        print(f'{self.name} \t {self.identificaiton} \t {self.department} \t {self.job_title}')

#Not sure what to name the objects



firstEmployee = Employee("Luke Skywalker", 47899, "Training", "Jedi Master")
secondEmployee = Employee("The Hulk", 39119, "Construction", "Demolition Worker")
thridEmployee = Employee("Bullwinkle Moose", 81774, "Animation", "Cartoon Character")

firstEmployee.displayEmployees()
secondEmployee.displayEmployees()
thridEmployee.displayEmployees()


