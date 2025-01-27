import os
import sys
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import E, W, N, S
from turtle import left
from utils import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
from datetime import datetime
from tkinter import *
from PIL import ImageTk, Image  
from threading import Thread


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
        self.reset_image = PhotoImage(file = "images/RESET.png")
        self.mode_image = PhotoImage(file = "images/MODE.png")
        self.remove_image = PhotoImage(file = "images/REMOVE.png")
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
                     border=2, width=self.btn_width, height=self.btn_height)
        self.start.grid(row=0, column=0, sticky=W, pady=self.ypad, padx=self.xpad)
        
        # Button 2
        self.add_remove = Button(self.control_frame, image=self.add_img, bg=self.border,
                     border=2, width=self.btn_width, height=self.btn_height, command=self.servers)
        self.add_remove.grid(row=0, column=1, sticky=W, pady=self.ypad, padx=self.xpad)

        # Button 3
        self.report_view = Button(self.control_frame, image=self.report_image, bg=self.border,
                     border=2, width=self.btn_width, height=self.btn_height)
        self.report_view.grid(row=0, column=2, sticky=W, pady=self.ypad, padx=self.xpad)


        # Button 4
        self.reset = Button(self.control_frame, image=self.reset_image, bg=self.border,
                     border=2, width=self.btn_width, height=self.btn_height)
        self.reset.grid(row=1, column=0, sticky=W, pady=self.ypad, padx=self.xpad)

        # Button 5
        self.mode = Button(self.control_frame, image=self.mode_image, bg=self.border,
                     border=2, width=self.btn_width, height=self.btn_height)
        self.mode.grid(row=1, column=1, sticky=W, pady=self.ypad, padx=self.xpad)

        # Button 6
        self.remove = Button(self.control_frame, image=self.remove_image, bg=self.border,
                     border=2, width=self.btn_width, height=self.btn_height, command=self.remove_click)
        self.remove.grid(row=1, column=2, sticky=W, pady=self.ypad, padx=self.xpad)


        # Button 7
        self.add_remove = Button(self.control_frame, image=self.photoimage, bg=self.border,
                     border=2, width=self.btn_width, height=self.btn_height)
        self.add_remove.grid(row=2, column=0, sticky=W, pady=self.ypad, padx=self.xpad)

        # Banner
        self.message = Label(self.control_frame, image=img, width=640, height=90, border=2)
        self.message.grid(row=31, column=0, sticky=W, pady=self.ypad, padx=self.xpad, columnspan=3)


    def remove_click(self):
        self.remove.config(image=self.remove_click_image)
        print("Change")
        self.after(200, self.on_release)


    def on_release(self):
        self.remove.config(image=self.remove_image)
        print("Relese")
    

    def servers(self): 
        # os.system("python server_add.py")
        Thread(target=lambda :os.system("python server_add.py")).start()


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

        self.frames = {}
        for F in (MainPage,):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    import sys
    app = MainWindow()
    app.mainloop()
    sys.exit()