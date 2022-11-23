import tkinter as tk
from tkinter import *
from tkinter import ttk

class TreeView(ttk.Treeview):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self["columns"] = ("Sn", "Pre Command", "Post Command", "Result")
        self.column("#0", width=120, minwidth=25)
        self.column("Sn", width=120, anchor=CENTER)
        self.column("Pre Command", width=120, anchor=W)
        self.column("Post Command", width=120, anchor=W)
        self.column("Result", width=120, anchor=W)
        
        # create a heading
        self.heading("#0", text="Lable", anchor=W)
        self.heading("Sn", text="Sn", anchor=CENTER)
        self.heading("Pre Command", text="Pre Command", anchor=W)
        self.heading("Post Command", text="Post Command", anchor=W)  
        self.heading("Result", text="Result", anchor=W)

        # Addig Data
        self.insert(parent='', index='end', iid=0, 
                    text='172.16.5.156')

        # for i in range(1,5):
        #     self.insert(parent='', index='end', iid=i, 
        #                 values=(f"{i}", 'Nitsh', f"{i}", 'Success'))
        
        # Add chield
        self.insert(parent='', index='end',  iid=5, 
                    values=("0", 'ifconfig', f"ifconfig", 'Success'))

        self.move('5', '0', '0')
        
if __name__ == "__main__":   
    root = tk.Tk()
    # column_name = ('name', "year", "color")
    tr = TreeView(root)
    tr.pack(fill=tk.BOTH, expand=True)
    root.mainloop()


