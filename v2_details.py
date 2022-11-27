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
import VARIABLES as var

global server_name
server_name = ""

print(var.NAME)
print(var.SERVER)

# https://apidemos.com/tkinter/tkinter-progressbar/tkinter-progressbar-start-step-stop-method.html
# https://www.activestate.com/resources/quick-reads/how-to-add-images-in-tkinter/#:~:text=However%2C%20Tkinter%20does%20not%20support%20images%20directly.%20Instead%2C,%E2%80%9Ctest%E2%80%9D%20in%20the%20background%3A%20label1%20%3D%20tkinter.Label%28image%3Dtest%29%20


def my_logger(message=""):
    # with open("logs/{}.log".format(file_name), "a") as f:
    #     f.write("{}\t{}\n".format(datetime.today(), message))
    pass

class SessionList(tk.Frame):
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

        print("session: ", self.sessions)
        
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
            print(line)
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
        s_font = tkFont.Font(family="Helvetica", size=26, weight="bold")
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
        self.sessions = os.listdir("logs")
        self.sframe = Frame(self)
        self.sframe.pack(pady=20, side=LEFT)

        self.lst = Label(self.sframe, text="Sessions", font=s_font)
        self.lst.grid(row=0, column=0, padx=50, pady=10)

        self.session_list = Listbox(self.sframe, bg="#ffffff",
                                   fg= "#000000", font=font_for_list, height=10, width=20)
        self.session_list.grid(row=1, column=0, padx=50, rowspan=2, sticky=E+W+N+S)

        # Onselect Event
        self.session_list.bind('<<ListboxSelect>>', self.onselect)

        scr = Scrollbar(self.sframe)
        scr.grid(row=1, column=1, sticky=E+W+N+S)

        # Contecting to the listbox
        scr.config(command=self.session_list.yview)
        self.session_list.config(yscrollcommand=scr.set)
        # Fetching Server List from File

        for line in self.sessions*10:
            print(line)
            self.session_list.insert(END, line.strip())

            
        # Sessin Details ============
        self.frame = Frame(self)
        self.frame.pack(pady=20, side=RIGHT)

        self.tv = ttk.Treeview(self.frame, columns=(1,2,3,4), show="headings", height=30)
        self.tv.pack(side=LEFT)

        self.tv.heading(1, text="Sn")
        self.tv.heading(2, text="IP")
        self.tv.heading(3, text="ST")
        self.tv.heading(4, text="Resut")

        self.sb = Scrollbar(self.frame, orient=VERTICAL)
        self.sb.pack(side=RIGHT, fill=Y)

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
        print(var.SERVER)
        # messagebox.showinfo("Double Clicked",outputStr)   
        self.controller.show_frame(0)
    
    
    def onselect(self, event):
        print("on select")
        w = event.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print('You selected item "%s"' % (value))
        var.SESSION = value
        # data table
        # get all server ip
        self.server = os.listdir(f"logs\\{value}")

        stat = ["pass", "fiald"]
        error = ["NA", "Connection Error", "Authentication Error", "Other"]

        serial_number = [i for i in range(1, 255)]
        Errors = ["{}".format(choice(error)) for _ in range(1, 100)]

        test_results = ["{}".format(choice(stat)) for _ in range(1, 100)]

        i = 1
        for sn, ser, err, res in zip(serial_number, self.server, Errors, test_results):
            self.tv.insert(parent='', index=i, iid=i, values=(sn, ser, err, res))
            i +=1

        # self.tv.bind('<<TreeviewSelect>>', self.OnDoubleClick)
        self.tv.bind('<Double-1>', self.OnDoubleClick)


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        main_frame_bg = "#ffffff"  # "#010530"
        login_section_bg = "#3400f0"
        font_color = "#01011f"  # "#E1341E"
        global server_name

        w = self.winfo_screenwidth() -40
        h = self.winfo_screenheight() -40

        fh = round((h - 330)/10)
        fw = round((((w - 126)-20)/8)/2)
        self.controller = controller
        self.configure(bg=main_frame_bg)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        font = tkFont.Font(family="Helvetica", size=10, weight="bold")
        out_font = tkFont.Font(family="Helvetica", size=10)
        self.conn_flag = False
        self.commad_list_for = []
        self.current_command = 0
        self.ypad = 20
        self.xpad = 30
        self.border = "#00D2FF"

        self.btn_width = 150
        self.btn_height = 150

        # get all server ip
        self.server = os.listdir("logs\\session_1")


        # Create a main frame
        self.pre_frame = LabelFrame(self, text="PRE")
        self.pre_frame.grid(row=0, column=0)

        # Text Area
        # Create the textbox
        self.txtbox = scrolledtext.ScrolledText(
            self.pre_frame, width=fw, height=fh, font=out_font)
        self.txtbox.grid(row=0, column=0)

        # default Result
        # with open(r"logs\session_1\192.168.5.2\pre\CPUINFO.TXT", "r") as f:
        #     self.txtbox.insert(END, f.read())

        self.post_frame = LabelFrame(self, text="POST")
        self.post_frame.grid(row=0, column=1)

        # Create the textbox
        self.txtbox1 = scrolledtext.ScrolledText(
            self.post_frame, width=fw, height=fh, font=out_font)
        self.txtbox1.grid(row=0, column=0)

        # Default result
        # with open(r"logs\session_1\192.168.5.2\pre\CPUINFO.TXT", "r") as f:
        #     self.txtbox1.insert(END, f.read())

        # Controll Section
        self.command_frame = LabelFrame(self, text="Commands")
        self.command_frame.grid(row=0, column=2)
        self.server_list = Listbox(self.command_frame, bg=main_frame_bg,
                                   fg=font_color, font=font, height=fh-5, width=20)
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
               for i in os.listdir(r"logs\session_1\192.168.5.2\post")]

        for line in cmd:
            self.server_list.insert(END, line.strip())

        # next = Button(self.command_frame, text="Next", font=font, width=10, bg="#00D2ff",
        #               fg="black", border=0)
        # next.grid(row=1, column=0)

        quit = Button(self.command_frame, text="Exit", font=font, width=10, bg="#ED425D",
                      fg="black", border=0, command=self.exit_tool)
        quit.grid(row=2, column=0, pady=10)

        
        self.sr_name = Label(self.command_frame, text=var.SERVER)
        self.sr_name.grid(row=3, column=0, pady=1)

        
    def onselect(self, evt):
        w = evt.widget
        try:
            index = int(w.curselection()[0])
            value = w.get(index)
            # value = self.server_list.get(tk.ACTIVE)
            print('You selected item "%s"' % (value))
            print("Selected Server: ", var.SERVER)
            self.sr_name.configure(text=var.SERVER)

            with open(r"logs\session_1\{}\pre\{}.TXT".format(var.SERVER, value), "r") as f:
                self.txtbox.delete('1.0', END)
                self.txtbox.insert(END, f.read())
                self.txtbox.tag_add("start", "1.11", "1.27")
                self.txtbox.tag_config(
                    "start", background="red", foreground="white")

            with open(r"logs\session_1\{}\post\{}.TXT".format(var.SERVER, value), "r") as f:
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
            self.controller.show_frame(1)
            print("Exit Tool")
        else:
            # my_logger("Exit Tool: No")
            pass


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # print screen size
        w = self.winfo_screenwidth() - 40
        h = self.winfo_screenheight() - 40

        self.title("File Syatem Extender")
        self.geometry("{}x{}+0+0".format(w, h))
        self.resizable(True, True)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.fl = []
        for F in (PageOne, PageThree, SessionList):
            frame = F(container, self)
            # self.frames[F] = frame
            self.fl.append(frame)
            frame.grid(row=0, column=0, sticky="nsew")
        # self.show_frame(PageThree)
        self.show_frame(1)

    def show_frame(self, cont):
        print("Frame: ", cont)
        print(self.frames)
        print(self.fl)
        # frame = self.frames[cont]
        frame = self.fl[cont]
        frame.tkraise()


if __name__ == "__main__":
    import sys
    app = MainWindow()
    app.mainloop()
    sys.exit()
