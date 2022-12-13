import csv
import math
from datetime import date
from datetime import timedelta

class Functionality:

    """ Säästökohteisiin liittyviä toimenpiteitä käsittelevä luokka"""

    def __init__(self):
        self.file = "targets.csv"
        self.list = []
        self.id = 0
    
    #def get_id(self):
    # """Luodaan säästökohteelle id, sen perusteella monesko kohde on. Ei toimi joten kommentteina"""
    #    try:
    #        open = pandas.read_csv(self.file)
    #    except pandas.errors.EmptyDataError:
    #        return 1
    #    else:
    #        return (len(open)+2)

    def create(self):
        """ Luodaan säästökohteita. Tällä hetkellä kovakoodattu, mutta tavara, hinta ja säästösumma per kk kysytään käyttäjältä"""
        
        item = "Kahvi"
        price = "350"
        sum = "35"
        self.creation_date = date.today()
        self.id += 1
        with open(self.file, "a") as file:
            row = f"{self.id};{self.creation_date};{item};{price};{sum}"
            file.write(row+"\n")
        return "New target added well done!"

    def read(self):
        """Lukee CSV tiedoston, jossa säästökohteet on säilöttynä"""

        with open(self.file) as file:
            for row in file:
                row = row.replace("\n", "")
                piece = row.split(";")

                id = piece[0]
                creation_date = piece[1]
                item = piece[2]
                price = piece[3]
                save_per_month = piece[4]

                self.list.append([id, creation_date, item, price, save_per_month])

            if self.list == []:
                return "There's nothing you are saving for atm"
            else:
                names = []
                for i in range(len(self.list)):
                    names.append(self.list[i][2])
                return names
                    

    def result(self, id):
        """Laskee kuinka kauan menee, jotta kohde saadaan ostettua"""

        self.read()
        target = self.list[id-1]
        months1 = math.ceil(int(target[3])/int(target[4]))
        date_today = date.today()
        months_left = months1 - ((int(date_today.month + date_today.year*12)) - (int(target[1][5:7]) + (int(target[1][0:4])*12)))
        if months_left > 12:
            years, months_left = divmod(months_left, 12)
            if months_left > 1:
                return f"{years} years and {months_left} months"
            else:
                return f"{years} years and {months_left} month"
        return f"{months_left} months"
        
    


    def delete_all(self):
        """Poistaa kaikki säästökohteet CSV-tiedostosta"""

        Functionality.id = 0
        with open(self.file, "w") as file:
            pass
        return "There's nothing you are saving for atm"

