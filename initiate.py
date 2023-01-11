import os
import sys
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import E, W, N, S
from utils import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
from datetime import datetime
from tkinter import *
from PIL import ImageTk, Image
from threading import Thread
from random import randint, choice
import VARIABLES as var
import csv
import pandas as pd


server_name = ""

class InitTest(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        main_frame_bg = "#ffffff"  # "#010530"
        global server_name

        self.controller = controller
        self.configure(bg=main_frame_bg)

        font = tkFont.Font(family="Helvetica", size=16, weight="bold")
        out_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
        s_font = tkFont.Font(family="Helvetica", size=22, weight="bold")
        font_for_list = tkFont.Font(family="Helvetica", size=16, weight="bold")
        self.conn_flag = False
        self.commad_list_for = []
        self.current_command = 0
        self.ypad = 20
        self.xpad = 30
        self.border = "#00D2FF"

        self.btn_width = 150
        self.btn_height = 150

        # Session List ============= 
        self.sessions = os.listdir("server_lists")
        self.sframe = Frame(self)
        self.sframe.pack(pady=20, padx=5, side=LEFT)

        self.selected = StringVar()
        # Create a list of options
        self.options = ["Select", "PRE", "POST"]
        self.selected.set(self.options[0])


        self.lst = Label(self.sframe, text="server credential's", font=s_font)
        self.lst.grid(row=0, column=0, padx=5, pady=10)

        self.session_list = Listbox(self.sframe, bg="#ffffff",
                                   fg= "#000000", font=font_for_list, height=20, width=20)
        self.session_list.grid(row=1, column=0, padx=5, pady=20, rowspan=2, sticky=E+W+N+S)

        # Onselect Event
        self.session_list.bind('<<ListboxSelect>>', self.onselect)

        scr = Scrollbar(self.sframe)
        scr.grid(row=1, column=1, sticky=E+W+N+S)

        # Contecting to the listbox
        scr.config(command=self.session_list.yview)
        self.session_list.config(yscrollcommand=scr.set)
        # Fetching Server List from File

        for line in self.sessions:
            self.session_list.insert(END, line.strip())
        
        # Frame For Edit Credential
        self.Edit_frame = LabelFrame(self, text="Control Button", font=font)
        # self.Edit_frame.grid(row=0, column=0)
        self.Edit_frame.pack(pady=20, padx=5, side=LEFT)

        self.option_menu = OptionMenu(self.Edit_frame, self.selected, *self.options)
        self.option_menu.grid(row=0, column=0, pady=10, padx=10)

        # self.option_menu.configure(command=self.options_changed)


        self.add = Button(self.Edit_frame, text="Start", width=20, border=0,
                                    bg="#02FFFF", font=font, command=self.start)
        self.add.grid(row=1, column=0, pady=10, padx=10)

        self.refresh = Button(self.Edit_frame, text="Stop", width=20, border=0, bg="#02FFFF",
                                font=font, command=self.stop)
        self.refresh.grid(row=2, column=0, pady=10, padx=10)

        self.cal = Button(self.Edit_frame, text="Start All", width=20, font=font,
                        border=0, bg="#F20F00", command=self.cancel_cmd)
        self.cal.grid(row=3, column=0, pady=10, padx=10)

        self.edit = Button(self.Edit_frame, text="Stop All", width=20, border=0, bg="#02FFFF",
                            font=font, command=self.stop_all)
        self.edit.grid(row=4, column=0, pady=10, padx=10)

        self.edit = Button(self.Edit_frame, text="Back", width=20, border=0, bg="#02FFFF",
                            font=font, command=self.return_to_home)
        self.edit.grid(row=5, column=0, pady=10, padx=10)
        
        # Sessin Details
        self.frame = Frame(self)
        self.frame.pack(pady=20, side=RIGHT)

        self.tv = ttk.Treeview(self.frame, columns=(1,2,3,4), show="headings", height=30)
        self.tv.pack(side=LEFT)

        self.tv.heading(1, text="Sn")
        self.tv.heading(2, text="IP")
        self.tv.heading(3, text="user")
        self.tv.heading(4, text="Status")

        self.sb = Scrollbar(self.frame, orient=VERTICAL)
        self.sb.pack(side=LEFT, fill=Y)

        self.tv.config(yscrollcommand=self.sb.set)
        self.sb.config(command=self.tv.yview)

        
    def OnDoubleClick(self, event):
        e = event.widget                                  # Get event controls
        iid = e.identify("item",event.x,event.y)          # Get the double-click item id
        state = e.item(iid,"text")                        # Get state
        city = e.item(iid,"values")                       # Get city
        var.SERVER = city[1]
        var.EDIT_SERVER_IP = city[1]
        var.EDIT_SERVER_ID = city[2]
        var.EDIT_SERVER_PASS = city[3]

    
    
    def onselect(self, event):
        w = event.widget
        if len(w.curselection()) == 0:
            return 0
        self.index = int(w.curselection()[0])
        self.value = w.get(self.index)
        var.SESSION = self.value

        df = pd.read_csv(f"server_lists\\{self.value}\\servers.csv")
        df["password"] = ""
        df.to_csv(f"server_lists\\{self.value}\\servers_status.csv", index=False)
        
        self.server_list = []
        with open(f"server_lists\\{self.value}\\servers_status.csv") as files:
            content = csv.reader(files)
            for i in content:
                # print(i)
                self.server_list.append(i)

        serial_number = [i for i in range(len(self.server_list))]
        # Clear list of server
        for item in self.tv.get_children():
            self.tv.delete(item)
        for ind, items in enumerate(self.server_list):
            try:
                self.tv.insert(parent='', index=ind, iid=ind,
                values=(serial_number[ind],
                            self.server_list[ind][0], self.server_list[ind][1],
                            self.server_list[ind][2]))
            except TclError:
                print("Error: ")
                pass

        # self.tv.bind('<<TreeviewSelect>>', self.OnDoubleClick)
        self.tv.bind('<Double-1>', self.OnDoubleClick)

    # Define a function to be called when the options are changed
    def options_changed(self):
        print("Selected option:", self.selected.get())

    def cancel_cmd(self):
        print("Cancle Button Press")


    def start(self):
        print("Hello Start")

    def start_all(self):
        print("Hello start all")

    def stop(self):
        print("Hello stop")

    def stop_all(self):
        print("Hello stop all")
    
    def return_to_home(self):
        print("Going To Home Page")


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # print screen size
        w = self.winfo_screenwidth() - 40
        h = self.winfo_screenheight() - 40

        self.state('zoomed')

        self.title("File Syatem Extender")
        # self.geometry("{}x{}+0+0".format(w, h))
        self.resizable(True, True)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.fl = []
        for F in (PageThree,):
            frame = F(container, self)
            # self.frames[F] = frame
            self.fl.append(frame)
            frame.grid(row=0, column=0, sticky="nsew")
        # self.show_frame(PageThree)
        self.show_frame(0)


    def show_frame(self, cont):
        # frame = self.frames[cont]
        frame = self.fl[cont]
        frame.tkraise()
    
    def destroy_frame(self, cont):
        self.fl[cont].destroy()


if __name__ == "__main__":
    import sys
    app = MainWindow()
    app.mainloop()
    sys.exit()
