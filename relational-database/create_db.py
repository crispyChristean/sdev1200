
import sqlite3

    # cursor.execute('DROP TABLE IF EXISTS Entries')
    # cursor.execute('''CREATE TABLE Entries (
    #                name VarChar(50),
    #                phone_num INT(10))''')

def add_tables(cursor):


    cursor.execute('DROP TABLE IF EXISTS Students')
    cursor.execute('DROP TABLE IF EXISTS Majors')
    cursor.execute('DROP TABLE IF EXISTS Departments')

    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute('''CREATE TABLE Majors (
                   MajorID INTEGER PRIMARY KEY,
                   Name TEXT)''')


    cursor.execute('''CREATE TABLE Departments (
                   DeptID INTEGER PRIMARY KEY,
                   Name TEXT)''')
    
    cursor.execute('''CREATE TABLE Students (
                   StudentID INTEGER PRIMARY KEY,
                   Name TEXT,
                   MajorID INTEGER,
                   DeptID INTEGER,
                   FOREIGN KEY (MajorID) REFERENCES Majors(MajorID),
                   FOREIGN KEY (DeptID) REFERENCES Departments(DeptID))''')

given = input("Enter the name of the database that will contain student info tables: ")
connection = sqlite3.connect(given)
cursor = connection.cursor()
add_tables(cursor)

