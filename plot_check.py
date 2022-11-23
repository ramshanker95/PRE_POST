from tkinter import * 
from tkinter import ttk

class App(Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # create aCanva
        my_canva = Canvas(self)
        my_canva.pack(side=LEFT, fill=BOTH, expand=1)

        # add a scroll bar
        my_scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=my_canva.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # configure the canva
        my_canva.configure(yscrollcommand=my_scrollbar.set)
        my_canva.bind("<Configure>", lambda e: my_canva.configure(scrollregion=my_canva.bbox("all")))

        # create a another frame inside the canva
        self.second_fram = Frame(my_canva)

        # add that new frame to a window inthe canvas
        my_canva.create_window((0,0), window=self.second_fram, anchor="nw")

    def ScrollPage(self):
        return self.second_fram

root = App()

root.title("Tab testing")
root.geometry("500x400")

web = root.ScrollPage()

btn = Button(web, text="Press Me")
btn.grid(row=0, column=2)


for i in range(2, 100):
    Label(web, text="192.168.1.{}".format(i)).grid(row=i, column=0, pady=2)
    Button(web, text="View").grid(row=i, column=1, pady=2)

Button(web, text="View").grid(row=i+1, column=1, pady=2)


root.mainloop()
