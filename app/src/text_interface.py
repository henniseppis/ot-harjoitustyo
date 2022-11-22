import csv
import math

class Functionality:
    id = 0
    def __init__(self):
        self.file = "saastokohteet.csv"
        self.list = []
    
    def create(self):
        item = input("What you are saving money for?: ")
        price = input("How much does it cost?: ")
        sum = input("What is the amount you are ready to put aside every month?: ")
        Functionality.id+=1
        with open(self.file, "a") as file:
            row = f"{self.id};{item};{price};{sum}"
            file.write(row+"\n")
    
    def read(self):
        with open(self.file) as file:
            for row in file:
                row = row.replace("\n", "")
                piece = row.split(";")
                    
                id = piece[0]
                item = piece[1]
                price = piece[2]
                save_per_month = piece[3]
                
                self.list.append([id,item,price,save_per_month])
            
            if self.list == []:
                return "There's nothing you are saving for atm"


    def result(self, id):
        self.read()
        target = self.list[id-1]
        months = math.floor(int(target[2])/int(target[3]))
        if months > 12:
            years, months = divmod(months, 12)
            return f"{years} years and {months} months"
        return f"{months} months"
           
    def delete_all(self):
        Functionality.id = 0
        with open(self.file, "w" ) as file:
            pass
        return "There's nothing you are saving for atm"
