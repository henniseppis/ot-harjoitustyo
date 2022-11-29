import unittest
from text_interface import Functionality


class Testtext_interface(unittest.TestCase):
    def setUp(self):
        self.test_class = Functionality()

    def test_delete_all(self):
        test = self.test_class.delete_all()
        self.assertEqual(test, "There's nothing you are saving for atm")

    def test_result(self):
        with open(self.test_class.file, "a") as file:
            row = f"1;2022-11-29;Lumilauta;500;50"
            file.write(row+"\n")

        test = self.test_class.result(1)
        self.assertEqual(test, "10 months")

    def test_read_nothing_inside(self):
        with open(self.test_class.file, "a") as file:
            pass

        test = self.test_class.read()
        self.assertEqual(test, "There's nothing you are saving for atm")
