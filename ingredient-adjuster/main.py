#
# Christian Espinoza C
# 1/14/2025
# Ingredient Adjuster Programming Project
# SDEV 1200 
#


#Literal amount of ingredients needed to produce the EXACT (as mention in the insturctions) # of cookies.
sugar = .03125 
butter = .02083
flour = .05729


cookieAmount = float(input("How many cookies would you like to make: ")) #User input, converts to a float
# Use comments liberally throughout the program.


sugar *= cookieAmount
butter *= cookieAmount
flour *= cookieAmount 


print(f'The current amount of the ingredients work for this batch!:\n{sugar:.2f} Cups of Sugar \
\n{butter:.2f} Cups of Butter\n{flour:.2f} Cups of Flour')
