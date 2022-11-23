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
from random import randint, choice

# https://www.activestate.com/resources/quick-reads/how-to-add-images-in-tkinter/#:~:text=However%2C%20Tkinter%20does%20not%20support%20images%20directly.%20Instead%2C,%E2%80%9Ctest%E2%80%9D%20in%20the%20background%3A%20label1%20%3D%20tkinter.Label%28image%3Dtest%29%20


def my_logger(message=""):
    # with open("logs/{}.log".format(file_name), "a") as f:
    #     f.write("{}\t{}\n".format(datetime.today(), message))
    pass


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        main_frame_bg = "#ffffff"  # "#010530"
        login_section_bg = "#3400f0"
        font_color = "#01011f"  # "#E1341E"

        self.controller = controller
        self.configure(bg=main_frame_bg)
        # self.rowconfigure(0, weight=1)
        # self.columnconfigure(0, weight=1)
        font = tkFont.Font(family="Helvetica", size=16, weight="bold")
        out_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
        self.conn_flag = False
        self.commad_list_for = []
        self.current_command = 0
        self.ypad = 20
        self.xpad = 30
        self.border = "#00D2FF"

        self.btn_width = 150
        self.btn_height = 150

        self.result = LabelFrame(self, text="Result of Test")
        self.result.grid(row=0, column=0)

        # data table
        stat = ["pass", "fiald"]
        error = ["NA", "Connection Error", "Authentication Error", "Other"]
        os_name = ["Ubuntu", "kali Linux", "Unix", "Fadora"]

        serial_number = [i for i in range(1, 25)]
        servers = ["192.16.8.{}".format(i) for i in range(1, 25)]
        kernals = ["CTP-T56-M{}".format(randint(0, 1000))
                   for _ in range(1, 100)]
        Errors = ["{}".format(choice(error)) for _ in range(1, 100)]
        os_names = ["{}".format(choice(os_name)) for _ in range(1, 100)]
        test_results = ["{}".format(choice(stat)) for _ in range(1, 100)]

        i = 1
        for sn, ser, os, ker, err, res in zip(serial_number, servers, os_names, kernals, Errors, test_results):
            if i % 2 == 0:
                Label(self.result, text="{}".format(sn), width=15, bg="#c2c2c4").grid(
                    row=i, column=0, pady=2, padx=0)
                Label(self.result, text="{}".format(ser), width=15, bg="#c2c2c4").grid(
                    row=i, column=1, pady=2, padx=0)
                Label(self.result, text="{}".format(os), width=15, bg="#c2c2c4").grid(
                    row=i, column=2, pady=2, padx=0)
                Label(self.result, text="{}".format(ker), width=15, bg="#c2c2c4").grid(
                    row=i, column=3, pady=2, padx=0)
                Label(self.result, text="{}".format(err), width=15, bg="#c2c2c4").grid(
                    row=i, column=4, pady=2, padx=0)
                if res == "fiald":
                    Label(self.result, text="{}".format(res), width=15, bg="red").grid(
                        row=i, column=5, pady=2, padx=0)
                    Button(self.result, text="View", width=15, border=0, bg="#526345", command=self.view_details).grid(
                        row=i, column=6, pady=2, padx=20)
                else:
                    Label(self.result, text="{}".format(res), width=15, bg="green").grid(
                        row=i, column=5, pady=2, padx=0)
                    Button(self.result, text="View", width=15, border=0, bg="#526345", command=self.view_details).grid(
                        row=i, column=6, pady=2, padx=20)

            else:
                Label(self.result, text="{}".format(sn), width=15, bg="#a3a3a3").grid(
                    row=i, column=0, pady=2, padx=0)
                Label(self.result, text="{}".format(ser), width=15, bg="#a3a3a3").grid(
                    row=i, column=1, pady=2, padx=0)
                Label(self.result, text="{}".format(os), width=15, bg="#a3a3a3").grid(
                    row=i, column=2, pady=2, padx=0)
                Label(self.result, text="{}".format(ker), width=15, bg="#a3a3a3").grid(
                    row=i, column=3, pady=2, padx=0)
                Label(self.result, text="{}".format(err), width=15, bg="#a3a3a3").grid(
                    row=i, column=4, pady=2, padx=0)
                if res == "fiald":
                    Label(self.result, text="{}".format(res), width=15, bg="red").grid(
                        row=i, column=5, pady=2, padx=0)
                    Button(self.result, text="View", width=15, border=0,
                           bg="#526345", command=self.view_details).grid(row=i, column=6, pady=2)
                else:
                    Label(self.result, text="{}".format(res), width=15, bg="green").grid(
                        row=i, column=5, pady=2, padx=0)
                    Button(self.result, text="View", width=15, border=0,
                           bg="#526345", command=self.view_details).grid(row=i, column=6, pady=2)
            i += 1

    def view_details(self, ser="13"):
        self.controller.show_frame(PageOne)


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        main_frame_bg = "#ffffff"  # "#010530"
        login_section_bg = "#3400f0"
        font_color = "#01011f"  # "#E1341E"

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
        self.border = "#00D2FF"

        self.btn_width = 150
        self.btn_height = 150

        # Create a main frame
        self.pre_frame = LabelFrame(self, text="PRE")
        self.pre_frame.grid(row=0, column=0)

        # Text Area
        # Create the textbox
        self.txtbox = scrolledtext.ScrolledText(
            self.pre_frame, width=63, height=40, wrap=WORD)
        self.txtbox.grid(row=0, column=0)

        with open("logs\logs\server_48\pre\CPUINFO.TXT", "r") as f:
            self.txtbox.insert(END, f.read())

        self.post_frame = LabelFrame(self, text="POST")
        self.post_frame.grid(row=0, column=1)

        # Create the textbox
        self.txtbox1 = scrolledtext.ScrolledText(
            self.post_frame, width=63, height=40, wrap=WORD)
        self.txtbox1.grid(row=0, column=0)

        with open("logs\logs\server_48\post\CPUINFO.TXT", "r") as f:
            self.txtbox1.insert(END, f.read())

        # Controll Section
        self.command_frame = LabelFrame(parent, text="Commands")
        self.command_frame.grid(row=0, column=2)
        self.server_list = Listbox(self.command_frame, bg=main_frame_bg,
                                   fg=font_color, font=font, height=22, width=20)
        self.server_list.grid(row=0, column=0, sticky="w", padx=2)

        # Onselect Event
        self.server_list.bind('<<ListboxSelect>>', self.onselect)

        scr = Scrollbar(self.command_frame)
        scr.grid(row=0, column=1, sticky=E+W+N+S)

        # Contecting to the listbox
        scr.config(command=self.server_list.yview)
        self.server_list.config(yscrollcommand=scr.set)
        # Fetching Server List from File

        cmd = [i.replace(".TXT", "")
               for i in os.listdir("logs\logs\server_48\post")]

        for line in cmd:
            self.server_list.insert(END, line.strip())

        # next = Button(self.command_frame, text="Next", font=font, width=10, bg="#00D2ff",
        #               fg="black", border=0)
        # next.grid(row=1, column=0)

        quit = Button(self.command_frame, text="Exit", font=font, width=10, bg="#00D2ff",
                      fg="black", border=0, command=self.exit_tool)
        quit.grid(row=2, column=0, pady=10)

    def remove_click(self):
        self.remove.config(image=self.remove_click_image)
        print("Change")
        self.after(200, self.on_release)

    def on_release(self):
        self.remove.config(image=self.remove_image)
        print("Relese")

    def servers(self):
        Thread(target=lambda: os.system("python server_control.py")).start()

    def onselect(self, evt):
        w = evt.widget
        try:
            index = int(w.curselection()[0])
            value = w.get(index)
            # value = self.server_list.get(tk.ACTIVE)
            print('You selected item "%s"' % (value))

            with open("logs\logs\server_48\pre\{}.TXT".format(value), "r") as f:
                self.txtbox.delete('1.0', END)
                self.txtbox.insert(END, f.read())
                self.txtbox.tag_add("start", "1.11", "1.27")
                self.txtbox.tag_config(
                    "start", background="red", foreground="white")

            with open("logs\logs\server_48\post\{}.TXT".format(value), "r") as f:
                self.txtbox1.delete('1.0', END)
                self.txtbox1.insert(END, f.read())
        except Exception as e:
            print("Error", e)
    

    # click event handler
    def confirm(self, mess):
        my_logger("Confirm: {}".format(mess))
        answer = askyesno(title='confirmation',
                        message='Are you sure? \n\n' + mess)
        
        if answer:
            my_logger("Confirm: Yes")
            return True
        else:
            my_logger("Confirm: No")
            return False
        
    
    def exit_tool(self):
        my_logger("Exit Tool Confirm?")
        if self.confirm("Are you sure you want to exit?"):
            # my_logger("Exit Tool: Yes")
            # self.controller.destroy()
            self.controller.show_frame(PageTwo)
            print("Exit Tool")
        else:
            # my_logger("Exit Tool: No")
            pass


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # print screen size
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()

        self.title("File Syatem Extender")
        self.geometry("{}x{}+0+0".format(w, h-40))
        self.resizable(True, True)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(PageOne)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    import sys
    app = MainWindow()
    app.mainloop()
    sys.exit()
