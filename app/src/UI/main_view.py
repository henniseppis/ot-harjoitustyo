import tkinter
from tkinter import Tk
from tkinter import messagebox
from UI.create_view import Create
from UI.view_view import ViewTargets
from Services.text_interface import Functionality

class View:

    """Käyttäjän säästökohteiden näkymä """

    def main_screen():
        window = Tk()
        window.title("Targets")
        window.geometry("450x300")
        window.configure(bg= "lightgrey")
        frame = tkinter.Frame(bg = "lightgrey")

        def create():

            """Voi luoda säästökohteen"""

            Create().create_target()

        def view():
            """Voi tarkastella mitä on laittanut säästöön. Näkyy myös kuinka kauan on siihen, että saa säästettyä tarpeeksi"""

            ViewTargets().view_screen()
        
        def delete_all():
            """Poistaa kaikki säästökohteet"""

            delete = Functionality().delete_all()
            messagebox.showinfo(title="INFO" ,message=delete)
            


        """Tkinter tekstit"""
        register_label= tkinter.Label(frame, text=" Welcome! ", bg = "lightgrey", font = ("Calibri", 20, "bold"))
        create_targets_button  = tkinter.Button(frame,bg= "lightblue", text = "Create" ,font = ("Calibri", 15), command = create)
        view_targets_button = tkinter.Button(frame, bg= "lightblue", text = "View" ,font = ("Calibri", 15), command = view)
        delete_all_button = tkinter.Button(frame, bg= "lightblue", text = "Delete all" ,font = ("Calibri", 15), command = delete_all)


        """Tkinter miten näkyy näytöllä"""
        register_label.grid(row=0, column= 2,sticky="news", pady=50)
        create_targets_button.grid(row=1, column=0)
        view_targets_button.grid(row=1, column=2)
        delete_all_button.grid(row=1, column=4)

        frame.pack()

        window.mainloop()