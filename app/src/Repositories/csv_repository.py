#from config import TARGETS_FILE_PATH
from datetime import date
from datetime import timedelta
from Services.csv_services import TargetsServices


class TargetsRepository:
    def __init__(self, file_path):
        self.file_path_csv = file_path
        self.list = []

    def create(self):
        item = "Kahvi"
        price = "100"
        sum = "30"
        self.creation_date = date.today()
        self.id += 1
        with open(self.file, "a") as file:
            row = f"{self.id};{self.creation_date};{item};{price};{sum}"
            file.write(row+"\n")
        return "New target added well done!"

    def list_targets(self):

        self.list.append([self.id, self.creation_date, self.item, self.price, self.save_per_month])

        if self.list == []:
            return "There's nothing you are saving for atm"
        else:
            names = []
            for i in range(len(self.list)):
                names.append(self.list[i][2])
            return names


    def read(self):
        with open(self.file_path_csv) as file:
            for row in file:
                row = row.replace("\n", "")
                piece = row.split(";")

                self.id = piece[0]
                self.creation_date = piece[1]
                self.item = piece[2]
                self.price = piece[3]
                self.save_per_month = piece[4]
    

    def months(self, id):
        self.read()
        self.list_targets()
        target = self.list[id-1]

        TargetsServices.count_months(target)


        #months1 = math.floor(int(target[3])/int(target[4]))
        #date_today = date.today()
        #months_left = months1 - ((int(date_today.month + date_today.year*12)) - (int(target[1][5:7]) + (int(target[1][0:4])*12)))
        #if months_left > 12:
        #    years, months_left = divmod(months_left, 12)
        #    if months_left > 1:
        #        return f"{years} years and {months_left} months"
        #    else:
        #        return f"{years} years and {months_left} month"
        #return f"{months_left} months"
    
    def delete_all(self):
        self.id = 0
        with open(self.file, "w") as file:
            pass
        return "There's nothing you are saving for atm"
    
csv_repository = TargetsRepository("targets.csv")

