import tkinter
import csv
import math
from tkinter import *
from UI.create_view import Create
from datetime import date
from config import TARGETS_FILE_PATH

class ViewTargets:
    """Luokka jonka avulla voi tarkastella olemassa olevia säästökohteita ja joka laskee säästämiseen kuluvan ajan """
    def __init__(self):
        self.file = TARGETS_FILE_PATH
        self.targets = []


    def view_screen(self):
        """Tkinter ikkuna alustus"""

        window = Tk()
        window.title("View Targets")
        window.geometry("")
        window.configure(bg= "lightgrey")


        def create():
            """Avaa create ikkunan ja samalla sulkee säästökohteiden tarkastelun

            Tätä funktiota kutsutaan vain jos säästökohteiden näkymä on tyhjä ja haluaa lisätä sitä kautta uuden kohteen
            
            """
            window.destroy()
            Create().create_target()

        def months_f():

            """Laskee kuinka monta kuukautta kestää, jotta saa ostettua säästökohteen
            

                Args: 
                    months = kuinka monta kuukautta säästökohteen saamiseen on silloin kun se luodaan
            """


            months = math.ceil(int(row[3])/int(row[4]))
            return months

        def months_left_f():

            """Laskee kuinka kauan tänä päivästä on vielä jäljellä jotta  saa ostettua tuotteen

                Args:

                months_left = kertoo kuinka kauan tänäpäivänä on säästökohteen saamiseen 

             (vaikuttaa vain jos luomispäivämäärä ja tarkasteltava päivämäärä ovat eri) """

            date_today = date.today()
            months_left = (months_f()) - ((int(date_today.month + date_today.year*12)) - (int(row[1][5:7]) + (int(row[1][0:4])*12)))
            return months_left

        def get_date():
            """Määritellään oikea muoto, jossa jäljellä oleva aika ilmoitetaan"""    

            months_left = months_left_f()
            if months_left > 12:
                years, months_left = divmod(months_left, 12)
                if months_left > 1:
                    return f"{years} years and {months_left} months left when saving {row[4]}€ a month"
                else:
                    return f"{years} years and {months_left} month left when saving {row[4]}€ a month" 
            return f"{months_left} months left when saving {row[4]}€ a month"

        def money_saved():
            """Laskee kuinka monta kuukautta säästökohteen lisäämisestä on ja sen mukaan myös sen kuinka paljon on jo säästetty

                Args:
                
                sum = laskee kuinka paljon on jo säästettynä säästökohteeseen
             """
            months_left = months_left_f()
            sum = (months_f() - months_left)*int(row[4])            
            return sum

        with open(self.file, "r") as read_file:
            reader = csv.reader(read_file)   
            data = list(reader)

        for i, row in enumerate(data):
            getdate = months_left_f()
            if getdate>0:
                self.targets.append(row[i])
                tkinter.Label(window, text=row[2], bg="lightgray",font = ("Calibri", 20, "bold italic")).grid(row=(i), sticky="w")
                tkinter.Label(window, text=f"{row[3]}€:", bg="lightgray",font = ("Calibri", 20)).grid(row=(i), column= 2)
                tkinter.Label(window, text=get_date(), bg="lightgray", width=50,font = ("Calibri", 15)).grid(row=(i),column=5, pady=10)
                tkinter.Label(window, text=f"{money_saved()}€ saved already :)", bg="lightgray",font = ("Calibri", 15)).grid(row=(i),column=7, pady=10)
            
        if len(self.targets) == 0:
            nothing_inside = tkinter.Label(window, text="There's nothing you are saving for atm", bg= "lightgray", font= ("Calibri",20))
            nothing_inside.grid(row=2, column=2, sticky = "news")
            create_button = tkinter.Button(window, text= "Press here to create one :)", bg="lightblue", font = ("Calibri", 15), command=create)
            create_button.grid(row=4, column=2, columnspan=2, pady = 30)


        window.mainloop()

