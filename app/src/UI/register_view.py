import tkinter
from tkinter import Tk, ttk
from tkinter import messagebox

class Register_w:

    def main_screen():
        window = Tk()
        window.title("New user")
        window.geometry("450x450")
        window.configure(bg= "lightgrey")

        frame = tkinter.Frame(bg = "lightgrey")
            

        #tekstit
        register_label= tkinter.Label(frame, text="Create new user :) ", bg = "lightgrey", font = ("Calibri", 30))
        username_label = tkinter.Label(frame, text="Choose username", bg= "lightgrey", font = ("Calibri", 15))
        username_entry = tkinter.Entry(frame, font = ("Calibri", 15))
        password_entry = tkinter.Entry(frame, show="*", font = ("Calibri", 15))
        password_label = tkinter.Label(frame, text= "Choose password", bg = "lightgrey", font = ("Calibri", 15))
        register_button = tkinter.Button(frame, text = "Register", bg = "lightblue", font = ("Calibri", 15), command = register)
        #näytöllä

        register_label.grid(row=0,  column=1, columnspan = 2, sticky="news", pady=40)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=2, pady = 20)
        password_label.grid(row=2,column=0)
        password_entry.grid(row=2, column=2, pady = 20)
        register_button.grid(row=4, column=2, columnspan=2, pady = 30)

        frame.pack()


        window.mainloop() 

    main_screen()