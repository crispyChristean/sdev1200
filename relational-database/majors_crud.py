#Christian Espinoza Celis 

import sqlite3

def display():
    print("1: Add new Major \
       \n2: Search for an Existing Major \
       \n3: Update an existing Major \
       \n4: Delete an existing Major \
       \n5: Show a list of all Major \
")


def get_choice():
    display()
    given_comm = int(input('Choice: '))
    while given_comm > 5 or given_comm < 1:
        given_comm = int(input("Please enter a valid input: "))
    return given_comm

def new_dep(cursor, input_one):
    cursor.execute('''INSERT INTO Majors (Name)
                   Values (?)''', (input_one,))

def view_dep(cursor, input_one):
    cursor.execute('''SELECT *
                   FROM Majors
                   WHERE name = ?''', (input_one,))
    row = cursor.fetchall()
    print('\n',row,'\n')
def set_dep(cursor, one, two):
    cursor.execute('''UPDATE Majors
                   SET Name = ?
                   WHERE Name = ?''', (two, one,))
def del_dep(cursor, one):
    cursor.execute('''DELETE FROM Majors
                   WHERE Name = ?''', (one,))

def view_all(cursor):
    cursor.execute('''SELECT *
                   FROM Majors''')
    rows = cursor.fetchall()
    print('\n',rows,'\n')
    
def execute_choice(cursor, choice):
    if choice == 1:
        input_one = input("Please give the name of the new Major: ")
        new_dep(cursor, input_one)
        
    elif choice == 2:
        input_one = input("Please enter the name of the Major to view: ")
        view_dep(cursor, input_one)
    elif choice == 3:
        input_one = input("Please enter the name of the Major: ")
        input_two = input("Please enter the new name for the Major: ")
        set_dep(cursor, input_one, input_two)

    elif choice == 4:
        input_one = input("Please enter the name of the Major you want to delete")
        del_dep(cursor, input_one)

    elif choice == 5:
        view_all(cursor)

#Program starts here
connection = sqlite3.connect('student_info.db')
cursor = connection.cursor()
choice = 0
while choice != 6:
    choice = get_choice()
    execute_choice(cursor, choice)





