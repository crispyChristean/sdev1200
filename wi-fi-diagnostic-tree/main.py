#
# Christian Espinoza    
# 01/20/2025
# Wi-Fi Diagnostic Tree Programming Project
# SDEV 1200 
#

# Use comments liberally throughout the program.

#

#Imports the system Module 
import sys


first = "Reboot the computer and try to connect.\nDid that fix the problem?"
second = "Reboot the router and try to connect.\nDid that fix the problem?"
third = "Make sure the cables between the router and modem are plugged in firmly.\nDid that fix the problem?"
fourth = "Move the router to a new location.\nDid that fix the problem?"
fifth = "Get a new router, or at least contact your service provider."

for iteration in (first, second, third, fourth, fifth):
    given = str(input(iteration))
    if given == "Yes" or given == "yes":
        break

sys.exit()