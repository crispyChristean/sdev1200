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












class FinalDraft():
    
    def __init__(self):

        #Main Stuff
        self.main_window = tk.Tk()
        #Counter to hold total cost
        self.counter = tk.DoubleVar()
        #Price Attributes

        #To utilize variables in tkinter, must use a tk.VariableType.
        self.count = tk.DoubleVar()
        self.oilChange = tk.DoubleVar()
        self.lubeJob = tk.DoubleVar()
        self.radiator = tk.DoubleVar()
        self.transmission = tk.DoubleVar()
        self.inspection = tk.DoubleVar()
        self.muffler = tk.DoubleVar()
        self.tire = tk.DoubleVar()
        self.full_treatment = tk.DoubleVar()

        self.counter.set(0)
        self.oilChange.set(0)
        self.lubeJob.set(0)
        self.radiator.set(0)
        self.transmission.set(0)
        self.inspection.set(0)
        self.muffler.set(0)
        self.tire.set(0)
        self.full_treatment.set(0)

        #Place Frames Here
        self.button_frame = tk.Frame(self.main_window)
        self.label_frame = tk.Frame(self.main_window)
        #Buttons are here, the parameters are: frame widget, text, and variable)
        self.o_c = tk.Checkbutton(self.button_frame, text='Oil Change: 30', variable=self.oilChange)
        self.l_j = tk.Checkbutton(self.button_frame, text = 'Lube Job: 20', variable = self.lubeJob)
        self.rad = tk.Checkbutton(self.button_frame, text = 'Radiator: 40', variable = self.radiator)
        self.t_m = tk.Checkbutton(self.button_frame, text = 'transmission: 100', variable = self.transmission)
        self.i_sp = tk.Checkbutton(self.button_frame, text = 'Insepction: 35', variable=self.inspection)
        self.m_f = tk.Checkbutton(self.button_frame, text = 'Muffler: 200', variable = self.muffler)
        self.t_r = tk.Checkbutton(self.button_frame, text= 'Tire Rotation', variable = self.tire)
        self.f_t = tk.Checkbutton(self.button_frame, text = 'Full Treatment', variable=self.full_treatment)
        #Label Widget 
        self.c_c = tk.Label(self.label_frame, textvariable= self.count)

        self.o_c.pack()
        self.l_j.pack()
        self.rad.pack()
        self.t_m.pack()
        self.i_sp.pack()
        self.m_f.pack()
        self.t_r.pack()
        self.f_t.pack()
        self.c_c.pack()

        self.button_frame.pack()
        self.label_frame.pack()

        tk.mainloop()
testingOne = FinalDraft()