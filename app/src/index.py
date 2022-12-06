from tkinter import Tk
from UI.login_view import Login_view

def main():
    window = Tk()
    window.title("I want it I got it...but when?")

    start = Login_view()
    start.main_screen()

    window.mainloop()


if __name__ == "__main__":
    main()
