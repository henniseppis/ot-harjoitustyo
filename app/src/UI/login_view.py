import tkinter
from tkinter import Tk, ttk
from tkinter import messagebox
from UI.savings_view import view

class Login_view: 
    def main_screen():
        window = Tk()
        window.title("I want it I got it.. but when?")
        window.geometry("600x450")
        window.configure(bg= "lightgrey")

        def login():
            username = "hennzzu"
            password = "jeejee"
            if username_entry.get()==username and password_entry.get()==password:
                window.destroy()
                view.main_screen()
                
            else:
                messagebox.showerror(title="Oh no invalid username or password", message="Please have another try or if u are new here press register")

        frame = tkinter.Frame(bg = "lightgrey")

        def register():
            pass

        #tekstit
        login_label= tkinter.Label(frame, text="Login :)", bg = "lightgrey", font = ("Calibri", 30))
        username_label = tkinter.Label(frame, text="Username", bg= "lightgrey", font = ("Calibri", 15))
        username_entry = tkinter.Entry(frame, font = ("Calibri", 15))
        password_entry = tkinter.Entry(frame, show="*", font = ("Calibri", 15))
        password_label = tkinter.Label(frame, text= "Password", bg = "lightgrey", font = ("Calibri", 15))
        login_button = tkinter.Button(frame, text = "Login", bg ="lightblue", font = ("Calibri", 15), command = login)
        register_button = tkinter.Button(frame, text = "Register", bg ="lightblue", font = ("Calibri", 15))

        #näytöllä

        login_label.grid(row=0, column=2, columnspan=2, sticky="news", pady=40)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=2, pady = 20)
        password_label.grid(row=2,column=0)
        password_entry.grid(row=2, column=2, pady = 20)
        login_button.grid(row=3, column=2, columnspan=2, pady = 30)
        register_button.grid(row=4, column=2, columnspan=2, pady = 30)

        frame.pack()

        window.mainloop()
    main_screen()