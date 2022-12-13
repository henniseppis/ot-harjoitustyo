import unittest
from Repositories.csv_repository import TargetsRepository
from datetime import date
from text_interface import Functionality


class Testtext_interface(unittest.TestCase):
    def setUp(self):
        self.test_class = TargetsRepository()

    def test_delete_all(self):
        test = self.test_class.delete_all()
        self.assertEqual(test, "There's nothing you are saving for atm")

    def test_result(self):
        with open(self.test_class.file, "a") as file:
            row = f"1;2022-11-29;Lumilauta;500;50"
            file.write(row+"\n")
            creation_date = date(2022-11-29)
            today = date.today()

        test = self.test_class.result(1)
        self.assertEqual(test, f"{10-(today.month-creation_date.month)} months")

    def test_read_nothing_inside(self):
        with open(self.test_class.file, "a") as file:
            pass

        test = self.test_class.read()
        self.assertEqual(test, "There's nothing you are saving for atm")
    
    def test_over_12_months(self):
        pass

    