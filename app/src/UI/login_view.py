import tkinter
from tkinter import Tk
from tkinter import *
from tkinter import messagebox
from UI.main_view import View
from User import User

class LoginView:
    """Käyttäjä voi kirjautua sisään. Tällä hetkellä vain yhdet tunnarit toimii """
    def __init__(self):

        """Args:
            username = käyttäjänimi
            password = salasana
            """
        self.username = User().username()
        self.password = User().password()

    def main_screen(self):
        window = Tk()
        window.title("I want it I got it.. but when?")
        window.geometry("470x320")
        window.configure(bg= "lightgrey")
        frame = tkinter.Frame(bg = "lightgrey")

        def login():
            """Tarkastetaan onko käyttäjätunnus ja salasana oikein, jos kyllä pääsee sisään. Jos ei pongahtaa error."""

            if username_entry.get()==self.username and password_entry.get()==self.password:
                window.destroy()
                View.main_screen()
            else:
                messagebox.showerror(title="Oh no invalid username or password", message="Please check the user manual to find the correct info")
                username_entry.delete(0, END)
                password_entry.delete(0, END)
    

        """Tkinter tekstit"""
        login_label= tkinter.Label(frame, text="Login", bg = "lightgrey", font = ("Calibri", 30, "bold"))
        username_label = tkinter.Label(frame, text="Username", bg= "lightgrey", font = ("Calibri", 15))
        username_entry = tkinter.Entry(frame, font = ("Calibri", 15))
        password_entry = tkinter.Entry(frame, show="*", font = ("Calibri", 15))
        password_label = tkinter.Label(frame, text= "Password", bg = "lightgrey", font = ("Calibri", 15))
        login_button = tkinter.Button(frame, text = "Login", bg ="lightblue", font = ("Calibri", 15), command = login)
    
        """Tkinter miten näkyy näytöllä"""

        login_label.grid(row=0, column=1, columnspan=2, sticky="w", pady=30)
        username_label.grid(row=2, column=0)
        username_entry.grid(row=2, column=2, pady = 20)
        password_label.grid(row=3,column=0)
        password_entry.grid(row=3, column=2, pady = 20)
        login_button.grid(row=4, column=1, columnspan=2, sticky="w", pady = 10)
    
        frame.pack()

        window.mainloop()