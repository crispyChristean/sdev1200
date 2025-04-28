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
    numbers = [2, 3, 5, 7]

    if given == 1:
        given = False
    else:
        for i in numbers:
            if i == given:
                given = True
            else:
                test = given/i 
                test -= int(test)
                if test == 0:
                    acc+=1
        if acc >= 1:
            given = False
    return given

checking = int(input("Pleae provide a number: "))

checking = is_prime(checking)

print(f'The number given is a prime number: {checking}')



