#
# Christian Espinoza Celis 
# 01/25/2025
# Rock, Paper, Scissors Game Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 

# Input --> Take an integer, pass it as an argument to a function --> returns true or false. 

def is_prime(given):
    acc = 0
    test = 0
    torf = 0
    test_numbers = [1,2,3,4,5,6,7,8]
    if given == 2:
        given = True
        return given 
    else: 
        for i in test_numbers:
            test = int(given/i)
        if acc == 1:
            given = True
            return True
        else: 
            given = False 
            return given


checking = int(input("Pleae provide a number: "))

checking = is_prime(checking)

print(f'The number given is a prime number: {checking}')



