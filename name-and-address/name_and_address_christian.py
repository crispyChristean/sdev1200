import tkinter as tk

class myGUI:
    
    def __init__(self):
        self.main_window = tk.Tk()
        self.name_value = tk.StringVar()
        self.street_value = tk.StringVar()
        self.csz_value = tk.StringVar()

        self.info_frame = tk.Frame(self.main_window)
        self.button_frame = tk.Frame(self.main_window)

        #Frames
        self.name_label = tk.Label(self.info_frame, \
                                   textvariable = self.name_value)
        
        self.street_label = tk.Label(self.info_frame, \
                                     textvariable = self.street_value)
        
        self.csz_label = tk.Label(self.info_frame, \
                                  textvariable=self.csz_value)
        

        self.name_label.pack()
        self.street_label.pack()
        self.csz_label.pack()

        self.show_info_button = tk.Button(self.button_frame, \
                                          text='Show Info', \
                                            command=self.show)
        
        self.quit_button = tk.Button(self.button_frame, \
                                     text='Quit', \
                                        command=self.main_window.destroy)
        #Pack the Buttons
        self.show_info_button.pack(side='left')
        self.quit_button.pack(side='right')
        #Pack the Frames
        self.info_frame.pack()
        self.button_frame.pack()
        #tk mainloop, needed to run
        tk.mainloop()

    #Function to set values of the name, address and city/state/zip
    def show(self):
        self.name_value.set("Christian Espinoza")
        self.street_value.set("365 Daytona Dr.")
        self.csz_value.set("Rock Springs, Wyoming 82901")


christianGUI = myGUI()