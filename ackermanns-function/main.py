#
# Christian Espinoza
# 03.15.2025
# Ackermann's Function Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 


def main():

    first = int(input("Please define the first number for the Ackermann Function: "))
    second = int(input("Please define the Second number for the Ackermann Function: "))

    print(f'results: {ackermann(first, second)}')

def ackermann(m,n):
        if m == 0:
            return n + 1 
        elif m > 0 and n == 0:
            return ackermann(m-1, 1)
        else:
            return ackermann(m-1, ackermann(m, n-1))
main()