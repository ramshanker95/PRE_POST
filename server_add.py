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

class ViewServer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        font = tkFont.Font(family="Helvetica", size=76, weight="bold")
        font_for_list = tkFont.Font(family="Helvetica", size=16, weight="bold")
        
        # w = self.winfo_screenwidth() -40
        h = self.winfo_screenheight() -40

        fh = round((h - 330)/10)
        # fw = round((((w - 126)-20)/8)/2)
        self.controller = controller

        self.sessions = os.listdir("logs")

        # print("session: ", self.sessions)
        
        self.lst = Label(self, text="Sessions", font=font)
        self.lst.grid(row=0, column=0, padx=100, pady=100)

        self.banner = Label(self, text="Select Session to View ->", font=font_for_list)
        self.banner.grid(row=1, column=0, padx=100, pady=100)

        self.server_list = Listbox(self, bg="#ffffff",
                                   fg= "#000000", font=font_for_list, height=10, width=20)
        self.server_list.grid(row=0, column=1, padx=2, rowspan=2, sticky=E+W+N+S)

        # Onselect Event
        self.server_list.bind('<<ListboxSelect>>', self.onselect)

        scr = Scrollbar(self)
        scr.grid(row=0, column=2, sticky=E+W+N+S)

        # Contecting to the listbox
        scr.config(command=self.server_list.yview)
        self.server_list.config(yscrollcommand=scr.set)
        # Fetching Server List from File

        for line in self.sessions*10:
            # print(line)
            self.server_list.insert(END, line.strip())

        self.next = Button(self, text="More", width=40, border=0, bg="#524136", height=20)
        self.next.grid(row=3, column=1, padx=10, pady=10)

        
    def command_frame(self):
        print("Clickes found")

    def onselect(self, event):
        print("on select")
        w = event.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print('You selected item "%s"' % (value))
        var.SESSION = value


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        main_frame_bg = "#ffffff"  # "#010530"
        login_section_bg = "#3400f0"
        font_color = "#01011f"  # "#E1341E"
        global server_name

        self.controller = controller
        self.configure(bg=main_frame_bg)
        # self.rowconfigure(0, weight=1)
        # self.columnconfigure(0, weight=1)
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
            print(line)
            self.session_list.insert(END, line.strip())
        
        # Frame For Edit Credential
        self.Edit_frame = LabelFrame(self, text="Edit Server", font=font)
        # self.Edit_frame.grid(row=0, column=0)
        self.Edit_frame.pack(pady=20, padx=5, side=LEFT)

        self.ip_label = Label(self.Edit_frame, text="IP Address", font=font)
        self.ip_label.grid(row=1, column=0)
        
        self.ip_entry = Entry(self.Edit_frame, text=var.EDIT_SERVER_ID, font=font)
        self.ip_entry.grid(row=2, column=0)

        self.user_label = Label(self.Edit_frame, text="User Id", font=font)
        self.user_label.grid(row=3, column=0)

        self.user_entry = Entry(self.Edit_frame, text=var.EDIT_SERVER_ID, font=font)
        self.user_entry.grid(row=4, column=0)

        self.pass_label = Label(self.Edit_frame, text="Password", font=font)
        self.pass_label.grid(row=5, column=0)

        self.pass_entry = Entry(self.Edit_frame, text=var.EDIT_SERVER_PASS, font=font)
        self.pass_entry.grid(row=6, column=0)


        self.add = Button(self.Edit_frame, text="Submit", width=20, border=0,
                                    bg="#02FFFF", font=font, command=self.re_create)
        self.add.grid(row=7, column=0, pady=10, padx=10)

        self.cal = Button(self.Edit_frame, text="Cancel", width=20, font=font,
                        border=0, bg="#F20F00", command=self.cancel_cmd)
        self.cal.grid(row=9, column=0, pady=10, padx=10)

        self.mess_label = Label(self.Edit_frame, text="Edit Server Information here",
                                            width=30, font=out_font)
        self.mess_label.grid(row=10, column=0)
        # ============

        self.mess_label = Label(self.Edit_frame, text="\nOther Controls",
                                            width=30, font=out_font)
        self.mess_label.grid(row=11, column=0)

        self.refresh = Button(self.Edit_frame, text="Refresh", width=20, border=0, bg="#02FFFF", font=font)
        self.refresh.grid(row=12, column=0, pady=10, padx=10)

        self.edit = Button(self.Edit_frame, text="Edit", width=20, border=0, bg="#02FFFF", font=font)
        self.edit.grid(row=13, column=0, pady=10, padx=10)

        self.btn_1 = Button(self.Edit_frame, text="Button 1", width=20, border=0, bg="#02FFFF", font=font)
        self.btn_1.grid(row=14, column=0, pady=10, padx=10)
            
        # Sessin Details ============
        self.frame = Frame(self)
        self.frame.pack(pady=20, side=RIGHT)

        self.tv = ttk.Treeview(self.frame, columns=(1,2,3,4), show="headings", height=30)
        self.tv.pack(side=LEFT)

        self.tv.heading(1, text="Sn")
        self.tv.heading(2, text="IP")
        self.tv.heading(3, text="user")
        self.tv.heading(4, text="password")

        self.sb = Scrollbar(self.frame, orient=VERTICAL)
        self.sb.pack(side=LEFT, fill=Y)

        self.tv.config(yscrollcommand=self.sb.set)
        self.sb.config(command=self.tv.yview)

        
    def OnDoubleClick(self, event):
        e = event.widget                                  # Get event controls
        iid = e.identify("item",event.x,event.y)          # Get the double-click item id
        state = e.item(iid,"text")                        # Get state
        city = e.item(iid,"values")
        print(city)                    # Get city
        outputStr = "{0} : {1}".format(state,city)        # Formatting
        var.SERVER = city[1]
        var.EDIT_SERVER_IP = city[1]
        var.EDIT_SERVER_ID = city[2]
        var.EDIT_SERVER_PASS = city[3]

        self.ip_entry.delete(0,"end")
        self.ip_entry.insert(0, var.EDIT_SERVER_IP)

        self.user_entry.delete(0,"end")
        self.user_entry.insert(0, var.EDIT_SERVER_ID)
        
        self.pass_entry.delete(0,"end")
        self.pass_entry.insert(0, var.EDIT_SERVER_PASS)

        print(var.SERVER)
        # messagebox.showinfo("Double Clicked",outputStr)   
        # self.controller.show_frame(0)
    
    
    def onselect(self, event):
        print("on select")
        w = event.widget
        print("=====>> ", w.curselection())
        if len(w.curselection()) == 0:
            return 0
        self.index = int(w.curselection()[0])
        self.value = w.get(self.index)
        print('You selected item "%s"' % (self.value))
        var.SESSION = self.value
        # data table
        # get all server ip

        self.update_server()
        
        # self.server = os.listdir(f"logs\\{value}")
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

    def update_server(self):
        self.cancel_cmd()
        for item in self.tv.get_children():
            self.tv.delete(item)
        with open(f"server_lists\\{self.value}\\servers.csv") as files:
            content = csv.reader(files)
            self.server_list = []
            for i in content:
                # print(i)
                self.server_list.append(i)
        
        serial_number = [i for i in range(len(self.server_list))]
        for ind, items in enumerate(self.server_list):
            try:
                self.tv.insert(parent='', index=ind, iid=ind,
                values=(serial_number[ind],
                            self.server_list[ind][0], self.server_list[ind][1],
                            self.server_list[ind][2]))
            except TclError:
                print("Error: ")
                pass

    def cancel_cmd(self):
        self.ip_entry.delete(0,"end")
        self.user_entry.delete(0,"end")
        self.pass_entry.delete(0,"end")


    def re_create(self):
        ip = self.ip_entry.get()
        user = self.user_entry.get()
        password = self.pass_entry.get()
        print(f"IP: {ip}, user {user}, password: {password}")
        print(f"server_lists\\{self.value}\\servers.csv")
        df = pd.read_csv(f"server_lists\\{self.value}\\servers.csv", index_col=False)
        print(df)
        df.loc[df["ip"] == ip, "password"] = password
        df.loc[df["ip"] == ip, "username"] = user
        print(df.loc[df["ip"] == ip])
        df.to_csv(f"server_lists\\{self.value}\\servers.csv", index=False)
        print(df)
        self.update_server()


class AddServer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        main_frame_bg = "#ffffff"  # "#010530"
        global server_name

        w = self.winfo_screenwidth() -40
        h = self.winfo_screenheight() -40

        fh = round((h - 330)/20)
        fw = round((((w - 126)-20)/8))
        self.controller = controller
        self.configure(bg=main_frame_bg)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        font = tkFont.Font(family="Helvetica", size=14, weight="bold")
        out_font = tkFont.Font(family="Helvetica", size=20)
        self.conn_flag = False
        self.commad_list_for = []
        self.current_command = 0
        self.ypad = 20
        self.xpad = 30
        self.border = "#00D2FF"
        self.header = ["ip","username","password"]

        self.btn_width = 150
        self.btn_height = 150

        # All session list
        self.session_list = os.listdir("logs")

        # Create a main frame

        self.Edit_frame = LabelFrame(self, text="Create Session", width=800, font=font)
        self.Edit_frame.grid(row=0, column=0, sticky=E+W+N+S)

        self.session_label = Label(self.Edit_frame, text="Sesison Name", font=font)
        self.session_label.grid(row=1, column=0)
        
        self.session_entry = Entry(self.Edit_frame, text=var.EDIT_SERVER_ID, font=font)
        self.session_entry.grid(row=2, column=0)

        self.session_des = Label(self.Edit_frame, text="Description", font=font)
        self.session_des.grid(row=3, column=0)

        self.session_des = Entry(self.Edit_frame, text=var.EDIT_SERVER_ID, font=font)
        self.session_des.grid(row=4, column=0)

        self.add = Button(self.Edit_frame, text="Add", width=20, border=0, 
                                bg="#02FFFF", font=font, command=self.session_create)
        self.add.grid(row=7, column=0, pady=10, padx=10)

        self.cal = Button(self.Edit_frame, text="Cancel", width=20, font=font,
                        border=0, bg="#F20F00", command=self.cancel_cmd)
        self.cal.grid(row=9, column=0, pady=10, padx=10)

        self.mess_label = Label(self.Edit_frame, text="You Can Create Session here",
                                            width=50, font=out_font)
        self.mess_label.grid(row=10, column=0)

        #  Create the textbox
        self.group1 = tk.LabelFrame(self, text="Server Details", padx=5, pady=5)
        self.group1.grid(row=0, column=1, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)

        self.txtbox = scrolledtext.ScrolledText(self.group1, width=40, height=fh,
                                        font=font
                                        )
        self.txtbox.grid(row=0, column=0,   sticky=E+W+N+S)

    
    def save_text(self):
        txt = self.txtbox.get("1.0", tk.END)
        print(f"Lenght of List: ", len(txt))
        if len(txt) <= 1:
            return False
        
        with open(f"server_lists/{self.session_entry.get()}/servers.csv", "w") as f:
            f.write(self.header)
        with open(f"server_lists/{self.session_entry.get()}/servers.csv", "a") as f:
            f.write(txt)
            # my_logger("Saved server list: {}".format)
            return True

    
    def cancel_cmd(self):
        self.controller.show_frame(1)

    def session_create(self):
        session_list = os.listdir("logs")
        if len(self.session_entry.get()) > 0:
            if self.session_entry.get() not in session_list:
                try:
                    os.mkdir(f"logs/{self.session_entry.get()}")
                    os.mkdir(f"server_lists/{self.session_entry.get()}")
                    if self.save_text():
                        messagebox.showinfo("Session", f"Session created Name: {self.session_entry.get()}")   
                        self.controller.show_frame(1)
                    else:
                        os.rmdir(f"logs/{self.session_entry.get()}")
                        os.rmdir(f"server_lists/{self.session_entry.get()}")
                        messagebox.showinfo("Session", f"Session Error: Empty IP List")   
                        self.controller.show_frame(0)

                except Exception as e:
                    messagebox.showinfo("Session ERROR", f"Error in Create Session: {e}")   
                    self.controller.show_frame(0)
            else:
                messagebox.showinfo("Sesion", f"Session Found: {self.session_entry.get()}")   
                self.controller.show_frame(0)
        else:
            messagebox.showinfo("Session", f"Session Error: Empty Sesion Name")   
            self.controller.show_frame(0)


class AddServerIp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        main_frame_bg = "#225FDD" #"#010530"
        login_section_bg = "#3400f0"
        font_color = "#01011f" #"#E1341E"

        self.controller = controller
        self.configure(bg='#f0f0f0')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        font = tkFont.Font(family="Helvetica", size=20, weight="bold")
        font1 = tkFont.Font(family="Helvetica", size=14, weight="bold")

        # 3. Text Editor----------------------------------------------------
        # Button Frame
        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.grid(row=0, column=0, sticky=W+E)    

        self.btn_Image = tk.Button(self.buttons_frame, text='Save',
                                font=font1, width=8,
                                bg="#00D2FF", fg="black", border=0,
                                command=self.save_text
                                )
        self.btn_Image.grid(row=0, column=0, padx=10, pady=10)

        self.btn_Folder = tk.Button(self.buttons_frame, text='Back',
                                font=font1, width=8,
                                bg="#00D2FF", fg="black", border=0,
                                command=self.prev_page
                                )
        self.btn_Folder.grid(row=0, column=2, padx=10, pady=10)

        # Group1 Frame ----------------------------------------------------
        self.group1 = tk.LabelFrame(self, text="Text Box", padx=5, pady=5)
        self.group1.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.group1.rowconfigure(0, weight=1)
        self.group1.columnconfigure(0, weight=1)

        # Create the textbox
        self.txtbox = scrolledtext.ScrolledText(self.group1, width=40, height=13,
                                        font=font
                                        )
        self.txtbox.grid(row=0, column=0,   sticky=E+W+N+S)
        with open("server_list.txt", "r") as f:
            for line in f:
                if line.strip():
                    self.txtbox.insert(tk.END, line)

    def save_text(self):
        txt = self.txtbox.get("1.0", tk.END)
        with open("server_list.txt", "w") as f:
            f.write(txt)
            my_logger("Saved server list: {}".format)
        self.btn_Image.configure(text="Saved")
        pass

    def prev_page(self):
        self.controller.show_frame(2)
        print("Backed")


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
        for F in (AddServer, PageThree, ViewServer, AddServerIp):
            frame = F(container, self)
            # self.frames[F] = frame
            self.fl.append(frame)
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(0)


    def show_frame(self, cont):
        frame = self.fl[cont]
        frame.tkraise()
    
    def destroy_frame(self, cont):
        self.fl[cont].destroy()


if __name__ == "__main__":
    import sys
    app = MainWindow()
    app.mainloop()
    sys.exit()