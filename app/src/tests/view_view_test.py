import unittest
from UI.view_view import ViewTargets

class TestCreate(unittest.TestCase):
    def setUp(self):
      self.test_class = ViewTargets()
    
    def test_months_f():
        with open("targets.csv", "w") as file:
            row = f"1;2022-11-29;Hevonen;10000;10"
            file.write(row+"\n")
        
        test = ViewTargets().view_screen()
        test.month
    