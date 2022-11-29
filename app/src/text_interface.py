import csv
import math
from datetime import date
from datetime import timedelta


class Functionality:
    id = 0

    def __init__(self):
        self.file = "saastokohteet.csv"
        self.list = []

    def create(self):
        item = input("What you are saving money for?: ")
        price = input("How much does it cost?: ")
        sum = input(
            "What is the amount you are ready to put aside every month?: ")
        self.creation_date = date.today()
        Functionality.id += 1
        with open(self.file, "a") as file:
            row = f"{self.id};{self.creation_date};{item};{price};{sum}"
            file.write(row+"\n")
        print("New target added well done!")

    def read(self):
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

    def result(self, id):
        self.read()
        target = self.list[id-1]
        months1 = math.floor(int(target[3])/int(target[4]))
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
        Functionality.id = 0
        with open(self.file, "w") as file:
            pass
        return "There's nothing you are saving for atm"


luokka = Functionality()
print(luokka.result(2))

