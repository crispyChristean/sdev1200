#Christian Espinoza Celis 

import sqlite3

def display():
    print("1: Add new Department \
       \n2: Search for an Existing Department \
       \n3: Update an existing Department \
       \n4: Delete an existing Department \
       \n5: Show a list of all Department \
")


def get_choice():
    display()
    given_comm = int(input('Choice: '))
    while given_comm > 5 or given_comm < 1:
        given_comm = int(input("Please enter a valid input: "))
    return given_comm

def new_dep(cursor, input_one):
    cursor.execute('''INSERT INTO Departments (Name)
                   Values (?)''', (input_one,))

def view_dep(cursor, input_one):
    cursor.execute('''SELECT *
                   FROM Departments
                   WHERE name = ?''', (input_one,))
    row = cursor.fetchall()
    print('\n',row,'\n')
def set_dep(cursor, one, two):
    cursor.execute('''UPDATE Departments
                   SET Name = ?
                   WHERE Name = ?''', (two, one,))
def del_dep(cursor, one):
    cursor.execute('''DELETE FROM Departments
                   WHERE Name = ?''', (one,))

def view_all(cursor):
    cursor.execute('''SELECT *
                   FROM Departments''')
    rows = cursor.fetchall()
    print('\n',rows,'\n')

def execute_choice(cursor, choice):
    if choice == 1:
        input_one = input("Please give the name of the new department: ")
        new_dep(cursor, input_one)
        
    elif choice == 2:
        input_one = input("Please enter the name of the department to view: ")
        view_dep(cursor, input_one)
    elif choice == 3:
        input_one = input("Please enter the name of the Department: ")
        input_two = input("Please enter the new name for the Department: ")
        set_dep(cursor, input_one, input_two)

    elif choice == 4:
        input_one = input("Please enter the name of the Department you want to delete")
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





