import os
import sys
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import E, W, N, S
from turtle import left
from mypackadge.utils import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
from datetime import datetime
from tkinter import *
from PIL import ImageTk, Image
from threading import Thread
from mypackadge.initiate import InitTest
from mypackadge.v2_details import ResultAnalysia, SessionList
from mypackadge.server_add import AddServer, PageThree, ViewServer, AddServerIp
from mypackadge.ignore_error import IngnoreTextEditor
from mypackadge.comand_editor import CommandTextEditor


class Homepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        main_frame_bg = "#225FDD" #"#010530"
        login_section_bg = "#141F5F"
        font_color = "#ffffff"

        self.controller = controller
        self.configure(bg=main_frame_bg)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        font = tkFont.Font(family="Helvetica", size=20, weight="bold")
        self.font = tkFont.Font(family="Helvetica", size=18)

        user_name = tk.Label(self, text="Login To Continue", bg=main_frame_bg, fg=font_color, font=font)
        user_name.place(relx=0.5, rely=0.1, anchor='center')

        # next_button = tk.Button(self, text="Next", command=lambda: controller.show_frame(PageOne))
        # next_button.place(relx=0.5, rely=0.9, anchor='center')

        # Center frame for Login Page
        self.frame1 = tk.Frame(self, bg=login_section_bg, width=400, height=300)
        self.frame1.place(relx=0.5, rely=0.5, anchor='center')

        # User Name
        self.user_name = tk.Label(self.frame1, width=40, text="User Name", bg=login_section_bg, fg=font_color, font=font)
        self.user_name.place(relx=0.3, rely=0.15, anchor='center', width=150, height=80)

        self.user_name_entry = tk.Entry(self.frame1, font=self.font, width=40)
        self.user_name_entry.place(relx=0.5, rely=0.3, anchor='center', width=300, height=30)

        # Password
        self.password = tk.Label(self.frame1, width=40, text="Password", bg=login_section_bg, fg=font_color, font=font)
        self.password.place(relx=0.3, rely=0.55, anchor='center')

        self.password_entry = tk.Entry(self.frame1, font=self.font, width=40, show="*")
        self.password_entry.place(relx=0.5, rely=0.7, anchor='center', width=300, height=30)

        # Login Button
        self.login_button = tk.Button(self.frame1, width=40, font=self.font,  text="Login",  bg="#00D2FF", fg="black", border=0, command=self.login)
        self.login_button.place(relx=0.5, rely=0.9, anchor='center', width=100, height=40)

        # Error Message
        self.error_message = tk.Label(self, width=40, text="", bg=main_frame_bg, fg='#5F141F', font=font)
        self.error_message.place(relx=0.5, rely=0.85, anchor='center', width=500, height=30)

    def login(self):
        print("Login")
        print(self.user_name_entry.get())
        print(self.password_entry.get())
        print("Login")
        print(self.user_name_entry.get())
        print(self.password_entry.get())

        if self.user_name_entry.get() == "admin" and self.password_entry.get() == "admin":
            print("Login Successful")
            self.controller.show_frame(0)
        else:
            print("Login Failed Invalid Credentials")
            self.error_message.configure(text="Invalid User Name or Password!")



class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        main_frame_bg =  "#514e65" #"#010530"
        login_section_bg = "#3400f0"
        font_color = "#01011f" #"#E1341E"

        self.controller = controller
        self.configure(bg=main_frame_bg)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        font = tkFont.Font(family="Helvetica", size=16, weight="bold")
        out_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
        self.conn_flag = False
        self.commad_list_for = []
        self.current_command = 0
        self.ypad = 20
        self.xpad = 30
        self.border="#00D2FF"

        self.btn_width = 150
        self.btn_height = 150

        row_img = Image.open("images/PRE_POST_CHECK.png")
        row_img = row_img.resize((640, 900), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(row_img)

        # START BUTTON
        self.photo = PhotoImage(file = "images/START.png")
        # Resize image to fit on button
        self.photoimage = self.photo #self.photo.subsample(2, 2)

        # START BUTTON
        self.add_img = PhotoImage(file = "images/ADD.png")
        self.report_image = PhotoImage(file = "images/VIEW.png")
        self.reset_image = PhotoImage(file = "images/add_cmd.png")
        self.mode_image = PhotoImage(file = "images/ignore.png")
        self.remove_image = PhotoImage(file = "images/Exit.png")
        self.remove_click_image = PhotoImage(file = "images/CLICK_REMOVE.png")


        # Create 3 buttons 1. Previous 2.Next 3. Exit
        # frame for control butto
        self.banner_frame = tk.Frame(self, bg=main_frame_bg)
        self.banner_frame.image = img
        self.banner_frame.pack(side = LEFT)

        self.control_frame = tk.Frame(self, bg="#514e65")
        self.control_frame.pack(side = LEFT)

        # Banner
        self.banner = Label(self.banner_frame, image=img, width=640, height=900)
        self.banner.pack(side=TOP)

        # Button 1
        self.start = Button(self.control_frame, image=self.photoimage, bg=self.border,
                     border=2, width=self.btn_width, height=self.btn_height,
                     command=lambda : self.controller.show_frame(8))
        self.start.grid(row=0, column=0, sticky=W, pady=self.ypad, padx=self.xpad)
        
        # Button 2
        self.add_remove = Button(self.control_frame, image=self.add_img, bg=self.border,
                     border=2, width=self.btn_width, height=self.btn_height, command=self.servers)
        self.add_remove.grid(row=0, column=1, sticky=W, pady=self.ypad, padx=self.xpad)

        # Button 3
        self.report_view = Button(self.control_frame, image=self.report_image, bg=self.border,
                     border=2, width=self.btn_width, height=self.btn_height, command=self.view_result)
        self.report_view.grid(row=0, column=2, sticky=W, pady=self.ypad, padx=self.xpad)


        # Button 4
        self.reset = Button(self.control_frame, image=self.reset_image, bg=self.border,
                     border=2, width=self.btn_width, height=self.btn_height, command=self.edit_command)
        self.reset.grid(row=1, column=0, sticky=W, pady=self.ypad, padx=self.xpad)

        # Button 5
        self.mode = Button(self.control_frame, image=self.mode_image, bg=self.border,
                     border=2, width=self.btn_width, height=self.btn_height, command=self.edit_ignore)
        self.mode.grid(row=1, column=1, sticky=W, pady=self.ypad, padx=self.xpad)

        # Button 6
        self.remove = Button(self.control_frame, image=self.remove_image, bg=self.border,
                     border=2, width=self.btn_width, height=self.btn_height, command=self.confirm)
        self.remove.grid(row=1, column=2, sticky=W, pady=self.ypad, padx=self.xpad)


        # # Button 7
        # self.add_remove = Button(self.control_frame, image=self.photoimage, bg=self.border,
        #              border=2, width=self.btn_width, height=self.btn_height)
        # self.add_remove.grid(row=2, column=0, sticky=W, pady=self.ypad, padx=self.xpad)

        # Banner
        self.message = Label(self.control_frame, image=img, width=640, height=90, border=2)
        self.message.grid(row=31, column=0, sticky=W, pady=self.ypad, padx=self.xpad, columnspan=3)


    def remove_click(self):
        # self.remove.config(image=self.remove_click_image)
        print("Change")
        # self.after(200, self.on_release)


    def on_release(self):
        self.remove.config(image=self.remove_image)
        print("Relese")
    

    def servers(self): 
        # os.system("python server_add.py")
        self.controller.show_frame(3)
        # Thread(target=lambda :os.system("python server_add.py")).start()

    def view_result(self):
        self.controller.show_frame(1)
    
    def add_session(self):
        self.controller.show_frame(3)

    def edit_command(self):
        self.controller.show_frame(9)

    def edit_ignore(self):
        self.controller.show_frame(10)

    def confirm(self, mess=""):
        print("Confirm: {}".format(mess))
        answer = askyesno(title='exit confirmation',
                        message='Are you sure? \n\n'+mess)
        
        if answer:
            print("Confirm: Yes")
            exit(0)
            # return True
        else:
            print("Confirm: No")
            return False


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # print screen size
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()

        self.title("File Syatem Extender")
        self.geometry("{}x{}".format(w, h-40))
        self.resizable(True, True)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.fl = []
        all_pages = (MainPage, SessionList, ResultAnalysia, AddServer, PageThree, ViewServer, 
                        AddServerIp, Homepage, InitTest, CommandTextEditor, IngnoreTextEditor)
        for F in all_pages:
            frame = F(container, self)
            self.fl.append(frame)
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(7)

    def show_frame(self, cont):
        frame = self.fl[cont]
        frame.tkraise()


if __name__ == "__main__":
    import sys
    app = MainWindow()
    app.mainloop()
    sys.exit()