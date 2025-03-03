#
# Christian Epsinoza Celis 
# 3/2/2025
# ShiftSupervisor Class Programming Project
# SDEV 1200
#
#Use comments liberally throughout the program.


from shiftsupervis import Employee 
from shiftsupervis import shiftSupervisor


firstEmployee = Employee("Luke Skywalker", 47899, "Training", "Jedi Master")
secondEmployee = Employee("The Hulk", 39119, "Construction", "Demolition Worker")

shift_manager = shiftSupervisor("Albert Einstein", 96712, "Education", "Scientist", "$123,000", "$12,000")

print(shift_manager.get_name())
#Not sure why the attributes don't print, even though when doing the return method it does show that it is passing the attributes properly.
shift_manager.display_supervisor()