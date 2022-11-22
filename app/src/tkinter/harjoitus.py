from tkinter import Tk, ttk, constants

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        heading_label = ttk.Label(master=self._root, text="Log in or create a new account :)")

        username_label = ttk.Label(master=self._root, text="Username")
        username_entry = ttk.Entry(master=self._root)

        password_label = ttk.Label(master=self._root, text="Password")
        password_entry = ttk.Entry(master=self._root)


        heading_label.grid(row=0, column=2, columnspan=2)
        username_label.grid(row=2, column=0, columnspan=1)
        username_entry.grid(row=3, column=0, columnspan=1)

        password_label.grid(row=2, column=4, columnspan=2)
        password_entry.grid(row=3, column=4, columnspan=2)
    

    def all_targets(self):
        heading_label = ttk.Label(master=self._root, text="All items")

        with open("saastokohteet.csv") as file:
            row = 1
            for file_row in file:
                file_row = file_row.replace("\n", "")
                piece = file_row.split(";")

                id = piece[0]
                item = piece[1]
                price = piece[2]
                save_per_month = piece[3]
                target_label = ttk.Label(master=self._root, text= f"{id} {item} {price} {save_per_month}")
                target_label.grid(row=row, column=2)
                row += 1

        heading_label.grid(row=0, column=2, columnspan=2)

window = Tk()
window.title("I want it I got it.. but when")
window.geometry("600x300")

ui = UI(window)
ui.all_targets()

window.mainloop()