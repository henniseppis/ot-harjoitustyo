import tkinter
from tkinter import Tk, ttk
from tkinter import messagebox

class Create:
    def main_screen():
        window = Tk()
        window.title("Create")
        window.geometry("650x200")
        window.configure(bg= "lightgrey")

        frame = tkinter.Frame(bg = "lightgrey")

        #tekstit
        item_label= tkinter.Label(frame, text="What are you saving money for?: ", bg = "lightgrey", font = ("Calibri", 12))
        item_label_entry = tkinter.Entry(frame, font = ("Calibri", 15))

        price_label= tkinter.Label(frame, text="How much does it cost?: ", bg = "lightgrey", font = ("Calibri", 12))
        price_label_entry = tkinter.Entry(frame, font = ("Calibri", 15))
        
        sum_label= tkinter.Label(frame, text="What is the amount you are ready to put aside every month?: ", bg = "lightgrey", font = ("Calibri",12))
        sum_label_entry = tkinter.Entry(frame, font = ("Calibri", 15))

        #näytöllä
        item_label.grid(row=0, column = 1 ,sticky="news", pady=15)
        item_label_entry.grid(row=0, column=2, pady = 15)

        price_label.grid(row=1, column = 1 ,sticky="news", pady=15)
        price_label_entry.grid(row=1, column=2, pady = 15)

        sum_label.grid(row=2, column = 1 ,sticky="news", pady=15)
        sum_label_entry.grid(row=2, column=2, pady = 15)


        frame.pack()


        window.mainloop() 
    main_screen()
