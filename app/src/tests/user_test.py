import unittest
from User import User

class TestUser(unittest.TestCase):
    def setUp(self):
       self.test_class = User()

    def test_username_wrong(self):
        self.username = "henni"

        test = User().username()

        self.assertNotEqual(test, self.username)
    
    def test_username_right(self):
        self.username = "hemppa"

        test = User().username()

        self.assertEqual(test, self.username)

    def test_password_wrong(self):
        self.password = "Jeejee"

        test = User().password()

        self.assertNotEqual(test, self.password)
    
    def test_password_right(self):
        self.password = "jeejee"

        test = User().password()

        self.assertEqual(test, self.password)

