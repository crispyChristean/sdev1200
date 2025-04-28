#
# Name
# Date
# Population Database Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.


###STEP ONE IS COMPLETED, DATABASE IS SHOWING IN DIRECTORY###

#Must import sqlite3
import sqlite3 as sql3

def main():
    choice = 0
    #Establishes a connection with the database.
    connection = sql3.connect('cities.db')
#Gets a cursor for the Database, Cursor is an object that is able to access and manipulate the data in the DB
    cursor = connection.cursor()
    ###PERFORM OPERATIONS ON DATABASE HERE###
#While loop 
    while choice != 8:
        choice = get_menu_choice()
        execute(choice, cursor)
    #Commit Changes to the database
    connection.commit()
    #Close the connection between the database.
    connection.close()

def display():
    print('                 MENU')
    print('--------------------------------------------')
    print('1 - Display Cities sorted by population, Ascending Order')
    print('2 - Display Cities sorted by population, Descending Order')
    print('3 - Display Cities sorted by Name')
    print('4 - Display Total Population of ALL cities')
    print('5 - Display Average Population of ALL cities')
    print('6 - Display City with the Highest population')
    print('7 - Display Cities with the Lowest Population')
    print('8 - Exit')

def execute(choice, cursor):
    if choice == 1:
        cities_sorted_ascending(cursor)
    elif choice ==2:
        cities_sorted_descending(cursor)
    elif choice == 3:
        cities_sorted_by_name(cursor)
    elif choice == 4:
        total_population(cursor)
    elif choice == 5:
        average_population(cursor)
    elif choice == 6:
        highest_population(cursor)
    elif choice == 7:
        lowest_population(cursor)

def cities_sorted_ascending(cursor):
    cursor.execute('''SELECT CityName, Population
                   FROM Cities
                   Order BY Population''')
    results = cursor.fetchall()
    print('\nCities By Population Ascending')
    print('-----------------------')
    display_results(results)

def cities_sorted_descending(cursor):
    cursor.execute('''SELECT CityName, Population
                   FROM Cities
                   ORDER BY Population DESC''')
    results = cursor.fetchall()
    print('\nCities By Population Descending')
    display_results(results)

def cities_sorted_by_name(cursor):
    cursor.execute('''SELECT CityNAME, Population 
                   FROM Cities
                   ORDER BY CityName''')
    results = cursor.fetchall()
    print('\nCities By Name A-Z')
    display_results(results)

def total_population(cursor):
    cursor.execute('SELECT SUM(Population) FROM Cities')
    results = cursor.fetchone()
    print(f'\nTotal Population: {results[0]:,.0f}\n')

def average_population(cursor):
    cursor.execute('SELECT AVG(Population) FROM Cities')
    results = cursor.fetchone()
    print(f'Average Population: {results[0]:,.0f}\n')

def highest_population(cursor):
    cursor.execute('SELECT MAX(Population) FROM Cities')
    max_results = cursor.fetchone()
    cursor.execute('''SELECT CityName, Population 
                   FROM Cities
                   WHERE Population = ?''', (max_results[0],))
    results = cursor.fetchone()
    print(f'\n{results[0]} has the Highest Population: {results[1]:,.0f}\n')

def lowest_population(cursor):
    cursor.execute('SELECT MIN(Population) FROM Cities')
    min_results = cursor.fetchone()
    cursor.execute('''SELECT CityName, Population 
                   FROM Cities
                   WHERE Population = ?''', (min_results[0],))
    results = cursor.fetchone()
    print(f'\n{results[0]} has the Lowest Population: {results[1]:,.0f}\n')

def display_results(res):
    print(f'{"City: 20"}{"Population"}')
    for row in res:
        print(f'{row[0]:20}{row[1]:,.0f}')
    print()

def get_menu_choice():
    display()
    choice = int(input("Please enter a NUMBER: "))
    while choice > 8 and choice < 1:
        choice = int(input("Please enter a Valid Input: "))
    return choice
main()