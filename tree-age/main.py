#
# Name
# Date
# Tree Age Programming Project
# SDEV 1200
#

# * One Growth Ring = One Year
# *Canvas Widget - Draw the growth rings of a 5 year old tree
# * Create text method - Number Each Growth Ring from center to edge 

import tkinter as tk

class TreeAge:

    def __init__(self):

        self.x = 500
        self.y = 500
        self.x_two = 500
        self.y_two = 500
        self.holding_textValues = ['0', '1', '2', '3', '4', '5']
        self.main_window = tk.Tk()
        #Create a Frame to hold canvas
        self.text_frame = tk.Frame(self.main_window)
        #Create a frame to hold 
        self.canvas = tk.Canvas(self.main_window, width=1000, height=1000, bg='white')


        self.canvas.pack()
        self.draw_five()
        tk.mainloop()
    #x1,y1,x2,y2
    def draw_five(self):
        for iteration in range(6):
            self.canvas.create_oval(self.x, self.y, self.x_two, self.y_two, outline='black', width=10)
            self.canvas.create_text(self.x+15, 500, text=self.holding_textValues[iteration])
            self.x-=50
            self.y+=30
            self.x_two+=50
            self.y_two-=30
first_try = TreeAge()