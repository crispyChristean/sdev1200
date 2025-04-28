#
# Christian Espinoza Celis 2/26/2025
# Person and Customer Classes Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.

from person import Person
from person import Customer

def main():
    givenName = input("Name: ")
    givenAddress = input("Address: ")
    givenNumber = input("Number: ")
    givenCustomer = input("Customer Number: ")
    givenMail = input("Do you want to be added to a mailing List?: ")

    givenMail.casefold()
    if givenMail == 'yes' or givenMail == 'y':
        givenMail = True
    else:
        givenMail = False

    my_customer = Customer(givenName, givenAddress, givenNumber, givenCustomer, givenMail)

    # Display information.
    print("Customer Information")
    print("-------------------------")
    print("Name ", my_customer.get_name())
    print("Address: ", my_customer.get_address())
    print("Phone Number: ", my_customer.get_number())
    print("Customer Number: ", my_customer.get_customer_number())
    print("On the Mailing List: ", my_customer.get_mailing_list())
# Call the main function.
main()