from tkinter import * 
from tkinter import ttk

root = Tk()

root.title("Tab testing")

root.geometry("500x500")

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=15)

def hide():
    my_notebook.hide(1)

def show():
    my_notebook.add(frame2, text="Tab2")

def select():
    my_notebook.select(1)


frame1 = Frame(my_notebook, width=500, height=500, bg="black")
frame2 = Frame(my_notebook, width=500, height=500, bg="red")
frame3 = Frame(my_notebook, width=500, height=500, bg="blue")

frame1.pack(fill='both', expand=1)
frame2.pack(fill='both', expand=1)
frame3.pack(fill='both', expand=1)


my_notebook.add(frame1, text="Tab1")
my_notebook.add(frame2, text="Tab2")
my_notebook.add(frame3, text="Tab3")

# Hide Tab
btn = Button(frame1, text="Hide Tab 2", command=hide).pack(pady=10)
# show tab
btn1 = Button(frame1, text="Show Tab 2", command=show).pack(pady=10)

# move to tab
btn3 = Button(frame1, text="Select", command=select).pack(pady=10)


root.mainloop()