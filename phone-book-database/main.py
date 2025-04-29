#
# Christian 
# 4/28/2025
# Phone Book Database Programming Project
# SDEV 1200
#
import sqlite3
#Function to create the table, if it exist, drop the table in the database first.
def add_entries_table(cursor):

    cursor.execute('DROP TABLE IF EXISTS Entries')
    cursor.execute('''CREATE TABLE Entries (
                   name VarChar(50),
                   phone_num INT(10))''')
#Create the Display Options
def display():
    print('Please Select what to do in the Database.')
    print('1: Add Name and Phone Number')
    print('2: View a persons phone number')
    print('3: Change the Phone Number of a person ')
    print('4: Delete a Row ')
    print('5: Exit')
#Gets input from the user.
def get_choice():
    display()
    given_command = int(input('Choice: '))
    while given_command > 5 or given_command < 1:
        given_command = int(input("Please enter a Valid Input: "))
    return given_command

#Execute the command given
def execute_choice(cursor, given_choice):
    if given_choice == 1:
        input_one = input("Please enter the name of the Person: ")
        input_two = input("Please enter the Phone Number: ")
        add_name_phone(cursor, input_one, input_two)
    elif given_choice == 2:
        input_one = input("Please enter the Name of the Person: ")
        view_phone(cursor, input_one)
    elif given_choice == 3:
        input_one = input("Please enter the desired person's name: ")
        input_two = input("Please enter the new Phone Number: ")
        change_phone(cursor, input_one, input_two)
    elif given_choice == 4:
        input_one = input("Please enter the name of the desired person to delete: ")
        delete_row(cursor, input_one)
#Commands to do one of the following: Update, Read, or Delete
def add_name_phone(cursor, one, two):
    cursor.execute('''INSERT INTO Entries (name, phone_num)
                   VALUES (?, ?)''', (one, two))

def view_phone(cursor, input_one):
    cursor.execute('''SELECT phone_num
                   FROM Entries
                   WHERE name = ?''', (input_one,))
    results = cursor.fetchall()
    print(f'The Phone Number of the Person: {results}')
def change_phone(cursor, input_one, input_two):
    cursor.execute('''UPDATE Entries
                   SET phone_num = ?
                   WHERE name = ?''', (input_two, input_one))

def delete_row(cursor, input_one):
    cursor.execute('''DELETE FROM Entries
                   WHERE name = ?''', (input_one,))
    
#Connections are used to connect to a database.
#If you are referencing a database that doesn't exist, a new one will exist.
connection = sqlite3.connect('phone_book.db')
#Cursor interacts with the database with SQL statements
cursor =  connection.cursor()

choice = 0

add_entries_table(cursor)

while choice != 5:
    choice = get_choice()
    execute_choice(cursor, choice)
#Committ and close the connection to the database.
connection.commit()
connection.close()