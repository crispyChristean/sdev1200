#Christian Espinoza Celis 

import sqlite3
#   - ___ Add a new student
#   - ___ Search for an existing student 
#   - ___ Update an existing student 
#   - ___ Delete an existing student 
#   - ___ Show a list of all students
def display():
    print("1: Add new Student \
       \n2: Search for an Existing Student \
       \n3: Update an existing Student \
       \n4: Delete an existing Student \
       \n5: Show a list of all Student \
")


def get_choice():
    display()
    given_comm = int(input('Choice: '))
    while given_comm > 5 or given_comm < 1:
        given_comm = int(input("Please enter a valid input: "))
    return given_comm

def new_dep(cursor, input_one, major_id, dept_id):
    cursor.execute('''INSERT INTO Students (Name, MajorID, DeptID)
                   Values (?)''', (input_one, major_id, dept_id))

def view_dep(cursor, input_one):
    cursor.execute('''SELECT *
                   FROM Students
                   WHERE name = ?''', (input_one,))
    row = cursor.fetchall()
    print('\n',row,'\n')

def set_dep(cursor, one, two):
    cursor.execute('''UPDATE Students
                   SET Name = ?
                   WHERE Name = ?''', (two, one,))
def del_dep(cursor, one):
    cursor.execute('''DELETE FROM Students
                   WHERE Name = ?''', (one,))

def view_all(cursor):
    cursor.execute('''SELECT *
                   FROM Students''')
    rows = cursor.fetchall()
    print('\n',rows,'\n')
    
def execute_choice(cursor, choice):
    if choice == 1:
        input_one = input("Please give the name of the new Student: ")
        input_two = input("Please Enter the Major ID: ")
        input_three = input("Please Enter the DeptID: ")
        new_dep(cursor, input_one, input_two, input_three)
        
    elif choice == 2:
        input_one = input("Please enter the name of the Student to view: ")
        view_dep(cursor, input_one)
    elif choice == 3:
        input_one = input("Please enter the name of the Student: ")
        input_two = input("Please enter the new name for the Student: ")
        set_dep(cursor, input_one, input_two)

    elif choice == 4:
        input_one = input("Please enter the name of the Student you want to delete")
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





