#
# Christian Espinoza 
# 03/03/2025
# Plant Information Programming Project
# SDEV 1200
#
import Plant 
# Use comments liberally throughout the program. - MAYBE 
def print_list(my_garden):
    for iteration in my_garden:
        iteration.get_info()

mint = Plant.Plant("Mint", "$10.99")
rose = Plant.Flower("Rose", "$20", False, "Pink")
lilly_vally = Plant.Flower("Lily of the valley", "$16.95", True, "White")
tulip = Plant.Flower("Tulip", "$55.55", True, "Magenta")
lupin = Plant.Flower("Lupin", "19.00", False, "Yellow")
bamboo = Plant.Plant("Bamboo", "$350.00")
coast_redwood = Plant.Plant("Coast Redwood", "$8.99")

my_garden = [mint, rose, lilly_vally, tulip, lupin, bamboo, coast_redwood]

print_list(my_garden)