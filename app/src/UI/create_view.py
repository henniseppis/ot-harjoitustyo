import tkinter
from tkinter import Tk, ttk

class Create:

    """Luodaan säästökohteita """

    def top_screen():
        window2 = Tk()
        window2.title("Create")
        window2.geometry("650x200")
        window2.configure(bg= "lightgrey")

        frame2 = tkinter.Frame(bg = "lightgrey")

        #tekstit
        item_label= tkinter.Label(frame2, text="What are you saving money for?: ", bg = "lightgrey", font = ("Calibri", 12))
        item_label_entry = tkinter.Entry(frame2, font = ("Calibri", 15))

        price_label= tkinter.Label(frame2, text="How much does it cost?: ", bg = "lightgrey", font = ("Calibri", 12))
        price_label_entry = tkinter.Entry(frame2, font = ("Calibri", 15))
        
        sum_label= tkinter.Label(frame2, text="What is the amount you are ready to put aside every month?: ", bg = "lightgrey", font = ("Calibri",12))
        sum_label_entry = tkinter.Entry(frame2, font = ("Calibri", 15))

        #näytöllä
        item_label.grid(row=0, column = 1 ,sticky="news", pady=15)
        item_label_entry.grid(row=0, column=2, pady = 15)

        price_label.grid(row=1, column = 1 ,sticky="news", pady=15)
        price_label_entry.grid(row=1, column=2, pady = 15)

        sum_label.grid(row=2, column = 1 ,sticky="news", pady=15)
        sum_label_entry.grid(row=2, column=2, pady = 15)

        frame2.pack()

        window2.mainloop()