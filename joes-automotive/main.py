#
# Chrsitian Epsinoza
# 04/06/2025
# Joe's Automotive Programming Project
# SDEV 1200
#
# Use comments liberally throughout the program.  
# The code below was auto-generated. 
# Delete/adjust unnecessary code.

import tkinter as tk


class iAmSteve():

    def __init__(self):

        #Main Stuff
        self.main_window = tk.Tk()
        #Counter to hold total cost
        self.counter = 0 
        #Price Attributes
        self.oilChange = 30.00
        self.lubeJob = 20.00
        self.radiator = 40.00
        self.transmission = 100.00
        self.inspection = 35.00
        self.muffler = 200.00
        self.tire = 20.00
        self.full_treatment = 445.00

    #Place Frames Here
        self.button_frame = tk.Frame(self.main_window)
        self.label_frame = tk.Frame(self.main_window)
    #Place Buttons Here
        self.oil_change =  tk.Button(self.button_frame, \
                                     text='Oil Change', \
                                        command=self.change(self.oilChange))
        
        self.lube_job = tk.Button(self.button_frame, \
                                  text='Lube Job', \
                                    command=self.change(self.lubeJob))
        self.radiator_flush = tk.Button(self.button_frame, \
                                        text='Radiator Flush', \
                                            command=self.change(self.radiator))
        self.transmisson_flush = tk.Button(self.button_frame, \
                                           text="Transmission Flush", \
                                            command=self.change(self.transmission))
        self.insepction = tk.Button(self.button_frame, \
                                    text="Inspection", \
                                        command=self.change(self.inspection))
        self.muffler_replacement = tk.Button(self.button_frame, \
                                             text="Muffler Replacement", \
                                             command=self.change(self.muffler))
        self.tire_rotation = tk.Button(self.button_frame, \
                                       text="Tire Rotation", \
                                       command=self.change(self.tire))
        self.all_items = tk.Button(self.button_frame, \
                                   text="All Services", \
                                   command=self.change(self.full_treatment))
        #Label Widget Here
        self.current_cost = tk.Label(self.label_frame, \
                                     textvariable=self.counter)
        

        self.current_cost.pack(side='bottom')
        #Pack the buttons
        self.oil_change.pack(side="left")
        self.lube_job.pack(side="left")
        self.radiator_flush.pack(side="left")
        self.transmisson_flush.pack(side="left")
        self.insepction.pack(side="left")
        self.muffler_replacement.pack(side="left")
        self.tire_rotation.pack(side="left")
        self.all_items.pack(side="left")
        #Pack the Frames
        self.button_frame.pack()
        self.label_frame.pack()
        tk.mainloop()
        
    def change(self, given):
        self.counter += given
        self.current_cost = tk.Button(self.label_frame, \
                                      textvariable=self.counter)

first = iAmSteve()