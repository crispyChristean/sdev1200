#
# Christian Espinoza Celis 3/15/2025
# Recursive Multiplication Programming Project
# SDEV 1200
# Use comments liberally throughout the program. 


def main():

    first = int(input("Give the First Number: "))
    second = int(input("Give the Second Number: "))

    print("The Product of the two is: ", multiple(first, second))
def multiple(x, y):

    if x == 0 or y == 0:
        return 0
    else:
        return x + multiple(x, y-1)


main()