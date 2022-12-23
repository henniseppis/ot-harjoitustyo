import unittest
from datetime import date
from Services.text_interface import Functionality


class TestText_interafce(unittest.TestCase):
    def setUp(self):
        self.test_class = Functionality()

    def test_get_id(self):
        with open(self.test_class.file, "w") as file:
            row = f"1;2022-11-29;Hevonen;10000;10"
            row2= f"2;2022-11-29;Imuri;600;20"
            row3=f"3;2022-11-29;Lumilauta;500;50"
            file.write(row+"\n")
            file.write(row2+"\n")
            file.write(row3+"\n")
        
        test = self.test_class.get_id()
        self.assertEqual(test,  4)

        """Alin käsky poistaa yllä lisäämät testi säästökohteet"""
        self.test_class.delete_all()
    
    def test_delete_all(self):
        test = self.test_class.delete_all()
        self.assertEqual(test, "Everything deleted")



    
   