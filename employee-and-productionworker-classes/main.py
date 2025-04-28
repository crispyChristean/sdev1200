#
# Chjristian Espinoza 2/27/2025
# 
# Employee And ProductionWorker Classes Programming Project
# SDEV 1200
#
import Employee

# Use comments liberally through the program.
def main():

    givenName = input("Employee Name: ")
    givenEmployee_number = input("Employee Number: ")
    givenShift = int(input("Shift Number: "))
    givenRate = input("Pay Rate: ")

    if givenShift == 1:
        givenShift = "Day Shift"
    elif givenShift == 2:
        givenShift = "Night Shift"
    elif givenShift == 3:
        givenShift = "Double Shift"
    else:
        print("Not a valid shift number!")
        exit()
    my_employee = Employee.productionWorker(givenName, givenEmployee_number, givenShift, givenRate)

    print("Employee Information")
    print("-------------------------")
    print("Employee Name: ", my_employee.get_employeeName())
    print("Employee Number: ", my_employee.get_employeeNumber())
    print("Employee's Shift: ",my_employee.get_shiftNumber())
    print("Payrate: ", my_employee.get_payRate())
#Program Start
main()
