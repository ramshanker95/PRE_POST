# import tkinter as tk
# from tkinter import *
# from tkinter import ttk

# class TreeView(ttk.Treeview):
#     def __init__(self, master, **kw):
#         super().__init__(master, **kw)
#         self["columns"] = ("Sn", "Pre Command", "Post Command", "Result")
#         self.column("#0", width=120, minwidth=25)
#         self.column("Sn", width=120, anchor=CENTER)
#         self.column("Pre Command", width=120, anchor=W)
#         self.column("Post Command", width=120, anchor=W)
#         self.column("Result", width=120, anchor=W)
        
#         # create a heading
#         self.heading("#0", text="Lable", anchor=W)
#         self.heading("Sn", text="Sn", anchor=CENTER)
#         self.heading("Pre Command", text="Pre Command", anchor=W)
#         self.heading("Post Command", text="Post Command", anchor=W)  
#         self.heading("Result", text="Result", anchor=W)

#         # Addig Data
#         self.insert(parent='', index='end', iid=0, 
#                     text='172.16.5.156')

#         for i in range(1,5):
#             self.insert(parent='', index='end', iid=i, 
#                         values=(f"{i}", 'Nitsh', f"{i}", 'Success'))
        
#         # Add chield
#         self.insert(parent='', index='end',  iid=5, 
#                     values=("0", 'ifconfig', f"ifconfig", 'Success'))

#         self.move('5', '0', '0')

#         self.bind('<<TreeviewSelect>>', self.OnDoubleClick)

#     def OnDoubleClick(self, event):
#         item = self.identify('item', event.x, event.y)
#         print("you clicked on", self.selection())
            
# if __name__ == "__main__":   
#     root = tk.Tk()
#     # column_name = ('name', "year", "color")
#     tr = TreeView(root)
#     tr.pack(fill=tk.BOTH, expand=True)
#     root.mainloop()



from tkinter import *
from tkinter.ttk import *
import time
from threading import Thread

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x250+1000+300')

def step():
    for i in range(50):
        ws.update_idletasks()
        pb1['value'] += 1
        
        time.sleep(0.1)

pb1 = Progressbar(ws, orient=HORIZONTAL, length=1000, mode='determinate')
pb1.pack(expand=True)

Button(ws, text='Start', command=lambda:Thread(target=step).start()).pack()

ws.mainloop()
