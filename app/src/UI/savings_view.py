import tkinter
from tkinter import Tk, ttk
from tkinter import messagebox
from create_view import Create

class view:

    """Käyttäjän säästäkohteiden näkymä """

    def main_screen():
        window = Tk()
        window.title("Targets")
        window.geometry("600x450")
        window.configure(bg= "lightgrey")
        frame = tkinter.Frame(bg = "lightgrey")

        def create():
            Create.top_screen()


        #tekstit
        register_label= tkinter.Label(frame, text=" You are saving for these atm ", bg = "lightgrey", font = ("Calibri", 15))
        targets  = tkinter.Button(frame, text = "Create" ,font = ("Calibri", 15), command = create)


        #näytöllä
        register_label.grid(row=0, columnspan = 2,sticky="news", pady=40)
        targets.grid(row=1, column=0, sticky="w")

        frame.pack()

        window.mainloop()

    main_screen()