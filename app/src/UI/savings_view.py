import tkinter
from tkinter import Tk, ttk
from tkinter import messagebox
from text_interface import Functionality

class view:
    def main_screen():
        window = Tk()
        window.title("Targets")
        window.geometry("600x450")
        window.configure(bg= "lightgrey")

        def create_target():
            Functionality().create()
            
            
        frame = tkinter.Frame(bg = "lightgrey")

        #tekstit
        register_label= tkinter.Label(frame, text=" You are saving for these atm ", bg = "lightgrey", font = ("Calibri", 15))
        targets  = tkinter.Button(frame, text = "Create" ,font = ("Calibri", 15), command = create_target)

        #näytöllä
        register_label.grid(row=0, columnspan = 2,sticky="news", pady=40)
        targets.grid(row=1, column=0, sticky="w")

        frame.pack()


        window.mainloop() 