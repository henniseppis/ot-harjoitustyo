#from config import TARGETS_FILE_PATH
import math
from datetime import date
from datetime import timedelta

class TargetsServices:
    def __init__():
        pass

    def count_months(self, target):
        months1 = math.floor(int(target[3])/int(target[4]))
        date_today = date.today()
        months_left = months1 - ((int(date_today.month + date_today.year*12)) - (int(target[1][5:7]) + (int(target[1][0:4])*12)))
        self.return_months(months_left)

    def return_months(self):
        if months_left > 12:
            years, months_left = divmod(months_left, 12)
            if months_left > 1:
                return f"{years} years and {months_left} months"
            else:
                return f"{years} years and {months_left} month"
        return f"{months_left} months"
    