#N O T E: THIS IS NOT THE OFFICAL ASSIGNMENT BUT A TEST UNRELATED ENTIRELY, DO NOT GRADE THIS FILE
import sqlite3

    # cursor.execute('DROP TABLE IF EXISTS Entries')
    # cursor.execute('''CREATE TABLE Entries (
    #                name VarChar(50),
    #                phone_num INT(10))''')

class student_experiment:

    def __init__(self):
       self.given_choice = 0


    def add_tables(self, cursor): 
        cursor.execute('''CREATE TABLE Majors (
                    MajorID INTEGER PRIMARY KEY,
                    Name TEXT)''')


        cursor.execute('''CREATE TABLE Departments (
                    Department INTEGER PRIMARY KEY,
                    Name TEXT)''')
        
        cursor.execute('''CREATE TABLE Students (
                    StudentID INTERGER PRUMARY KEY,
                    Name TEXT,
                    MajorID INTEGER,
                    DeptID INTEGER)''')
        
    def create_db_copy(self):
        given = input("Enter the name of the database that will contain student info tables: ")
        connection = sqlite3.connect(given)
        cursor = connection.cursor()
        self.add_tables(cursor)

    def add_new_major(self, cursor, input_one):

        cursor.execute('''INSERT INTO Majors (Name)
                       VALUES (?)''', (input_one))

    def add_new_department(self, cursor, input_one)
        cursor.execute('''INSERT INTO Departments (Name)
                       VALUES (?)''', (input_one))
        
    
    def decide_command_major(self, cursor, given, s_t):
        if  s_t == 1 and given == 1:
            input_one = input("Please enter the name of the Major: ")
            add_new_major(cursor, input_one)
        elif  s_t == 1 and given == 2: 

        elif  s_t == 1 and given ==3: 

        elif  s_t == 1 and given == 4:

        elif  s_t == 1 and given == 5:

        elif s_t == 2 and given == 1:
            input_one = input("Please enter the name of the Department: ")
            add_new_department(cursor, input_one)
        elif  s_t == 2 and given == 2:

        elif s_t == 2 and given == 3: 

        elif s_t == 2 and given == 4:

        elif s_t == 2 and given == 5: 

        elif s_t == 3 and given == 1:
            input_one = input("Please enter the name of the Student: )
            key_one = input()
        elif s_t == 3 and given == 2:
        
        elif s_t == 3 and given== 3:

        elif s_t == 3 and given == 4:

        elif s_t == 3 and given == 5:

        else:
            pass
    def edit_major(self, cursor, selected_tab):
        print("1: Add new Major \
              \n2: Search for an Existing Major \
              \n3: Update an existing Major \
              \n4: Delete an existing Major \
              \n5: Show a list of all majors \
            ")
        while given > 1 and given < 5:
            given = input("Please select a command for the Majors Table")
            self.decide_command_major(cursor, given, selected_tab)

    def edit_departments(self, cursor, selected_tab):
        print("1: Add new Department \
              \n2: Search for an Existing Department \
              \n3: Update an existing Department \
              \n4: Delete an existing Department \
              \n5: Show a list of all Department \
            ")
        while given > 1 and given < 5:
            given = input("Please select a command for the department")
            self.decide_command_major(cursor, given, selected_tab)

    def edit_students(self, cursor, selected_tab):
        print("1: Add a new Student \
              \n2: Search for an Existing student \
              \n3: Update an existing student \
              \n4: Delete an existing student \
              \n5: Show a list of all student \
            ")
        while given > 1 and given < 5:
            given = input("Please select a command for the students table")
            self.decide_command_major(cursor, given, selected_tab)

    def choose_table(self):
        enter_db = input("please enter the database file name: ")
        connect = sqlite3.connect(enter_db)
        cursor = connect.cursor()
        print('1: Majors Table \
              \n2: Departments Table \
              \n3: Students Table\n\n')
        while selected_table == int:
            selected_table = input("Please choose the table to edit, view, or manipulated: ")

            if selected_table == 1:
                self.edit_major(cursor, selected_table)
            elif selected_table ==2:
                self.edit_departments(cursor, selected_table)
            elif selected_table == 3:
                self.edit_students(cursor, selected_table)

