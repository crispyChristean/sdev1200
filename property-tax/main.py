#
# Christian
# 04/27/2025
# Property Tax Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 

import tkinter as tk 

class values:

    def __init__(self):
        #Create main window
        self.main_window = tk.Tk()
        #Set Frames
        self.main_frame = tk.Frame(self.main_window)
        self.second_frame = tk.Frame(self.main_window)
        #Create variables for tkinter
        self.assess_val = tk.DoubleVar()
        self.tax_amount = tk.DoubleVar()
        # self.assess_val = property_value*.6
        # self.tax_amount = (assess_val/100) * .75
        #Create Label, Input, and Button for first frame 
        self.show_quest = tk.Label(self.main_frame, text= "Please put in your property Value")
        self.property_value = tk.Entry(self.main_frame, width = 10)
        self.button_quest = tk.Button(self.main_frame, text="Show Assessment Value and Tax!", command=self.display)

        #Create Labels for tax-property-assessment-values.
        self.show_assessment = tk.Label(self.second_frame, textvariable=self.assess_val)
        self.show_tax_value = tk.Label(self.second_frame, textvariable=self.tax_amount)
        #Pack Widgets Here
        self.show_assessment.pack()
        self.show_tax_value.pack()
        self.show_quest.pack()
        self.property_value.pack()
        self.button_quest.pack()
        #Pack Frames Here
        self.main_frame.pack()
        self.second_frame.pack()
        tk.mainloop()
    # self.assess_val = property_value*.6
    # self.tax_amount = (assess_val/100) * .75
    def display(self):
        self.prop_val_convert = float(self.property_value.get())
        self.assess_val.set(self.prop_val_convert*0.6)
        self.tax_amount.set((self.assess_val.get()/100)*.75)

firstRun = values()
