import tkinter
from csv import *
from tkinter import *
from datetime import date
from tkinter import messagebox
from Services.text_interface import Functionality
from config import TARGETS_FILE_PATH

class Create:
    """Luodaan säästökohteita """
    def __init__(self):
        self.file = TARGETS_FILE_PATH

    def create_target(self):

        """Alustetaan näkymä"""

        window = Tk()
        window.title("Create")
        window.geometry("650x250")
        window.configure(bg= "lightgrey")
        list = []

        def save():
            """Käyttäjän syöttämä teksti tallennetaan CSV-tiedostoon"""

            with open(self.file, "a") as file:
                Writer = writer(file)
                Writer.writerows(list)
                messagebox.showinfo("Target","New target added well done!", parent = window)
            clear()
        
        def get():
            """Jokaiselle säästökohteelle luodaan ID sen mukaan monesko se on
            
                Args:
                    
                    id = yksilöllinen id jokaiselle säästökohteelle
                    creation_date = säästökohteen luomispäivämäärä

            """

            id = Functionality().get_id()
            creation_date = date.today()

            list2 = [id,creation_date,item_label_entry.get(), price_label_entry.get(), sum_label_entry.get()]
            list.append(list2)
            save()
        
        def clear():
            """Tyhjentää syöttöboksit"""

            item_label_entry.delete(0,END)
            price_label_entry.delete(0,END)
            sum_label_entry.delete(0,END)
            window.destroy()
        
        def check_if_numbers():
            try:
                if (int(price_label_entry.get()) >= int(sum_label_entry.get())) and (int(price_label_entry.get()) and int(sum_label_entry.get())):
                    get()
            except:
                messagebox.showerror(title="Error", message= "Please insert numbers to the second and third row. And please provide the price larger than the monthly amount", parent= window)


        """Tkinter tekstit"""

        item_label= tkinter.Label(window, text="What are you saving money for?: ", bg = "lightgrey", font = ("Calibri", 12))
        item_label_entry = tkinter.Entry(window, font = ("Calibri", 15))

        price_label= tkinter.Label(window, text="How much does it cost?: ", bg = "lightgrey", font = ("Calibri", 12))
        price_label_entry = tkinter.Entry(window, font = ("Calibri", 15))
        
        sum_label= tkinter.Label(window, text="What is the amount you are ready to put aside every month?: ", bg = "lightgrey", font = ("Calibri",12))
        sum_label_entry = tkinter.Entry(window, font = ("Calibri", 15))

        save_button = tkinter.Button(window, text= "Save", bg= "lightblue", font = ("Calibri", 15), command = check_if_numbers)


        """Tkinter miten näkyy näytöllä"""

        item_label.grid(row=0, column = 1 ,sticky="news", pady=15)
        item_label_entry.grid(row=0, column=2, pady = 15)

        price_label.grid(row=1, column = 1 ,sticky="news", pady=15)
        price_label_entry.grid(row=1, column=2, pady = 15)

        sum_label.grid(row=2, column = 1 ,sticky="news", pady=15)
        sum_label_entry.grid(row=2, column=2, pady = 15)

        save_button.grid(row= 3, column = 1, columnspan=2, pady=30)


        window.mainloop()