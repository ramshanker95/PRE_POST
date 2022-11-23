from cProfile import label
from cgitb import text
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

# https://www.activestate.com/resources/quick-reads/how-to-add-images-in-tkinter/#:~:text=However%2C%20Tkinter%20does%20not%20support%20images%20directly.%20Instead%2C,%E2%80%9Ctest%E2%80%9D%20in%20the%20background%3A%20label1%20%3D%20tkinter.Label%28image%3Dtest%29%20

# https://pythonguides.com/python-tkinter-messagebox/

def my_logger(message=""):
    # with open("logs/{}.log".format(file_name), "a") as f:
    #     f.write("{}\t{}\n".format(datetime.today(), message))
    pass


class PageOne_P(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # super().__init__()
        # print(self.employee_list)

        main_frame_bg =  "#050022" #"#010530"
        self.login_section_bg = "#3400f0"
        self.font_color = "#01011f" #"#E1341E"

        self.controller = controller
        self.configure(bg=main_frame_bg)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.font = tkFont.Font(family="Arial", size=16, weight="bold")
        out_font = tkFont.Font(family="Arial", size=12, weight="bold")
        self.conn_flag = False
        self.commad_list_for = []
        self.current_command = 0
        self.ypad = 20
        self.xpad = 30
        self.border="#00D2FF"

        self.btn_width = 150
        self.btn_height = 150
        self.employee_list = [('ID', 'IP', 'Hostname', 'User Name', 'Password'),
                        (1, '172.16.5.12', 'pi','pi','pi1'),
                        (2, '172.16.5.13', 'pi','pi','pi1'),
                        (3, '172.16.5.14', 'pi','pi','pi1')
                        ]

        # find total number of rows and
        # columns in list
        self.rows = []
        self.create_gui()

    def create_gui(self):
        # For Table
        self.editor = Frame(self, bg="#050022", width=45)
        self.editor.pack(side=LEFT, fill = BOTH, expand = True)

        # For Control
        self.control = Frame(self, bg="#050022", width=100)
        self.control.pack(side=RIGHT, fill = BOTH, expand = True)

        # self.scr =  tk.Scrollbar(self.editor)
        # self.scr.grid(row=0, column=5, sticky=E+W+N+S, rowspan=25)


        # self.create_table(self.editor)
        self.create_table(self.editor)
        

        # Conrtol Buttons
        self.save = Button(self.control, bg="#00fa00", text="Save", width=15, 
                            border=0, height=2, font=self.font)
        self.save.grid(row=0, column=0, padx=10, pady=10)

        self.cancle = Button(self.control, bg="#00fa00", text="Add New", width=15, 
                            border=0, height=2, font=self.font, command=self.count)
        self.cancle.grid(row=1, column=0, padx=10, pady=10)

        self.cancle = Button(self.control, bg="#fa0000", text="Cancle", width=15, 
                            border=0, height=2, font=self.font)
        self.cancle.grid(row=2, column=0, padx=10, pady=10)

        self.prev = Button(self.control, bg="#fa0000", text="Previous", width=15, 
                            border=0, height=2, font=self.font)
        self.prev.grid(row=3, column=0, padx=10, pady=10)
        
        self.next = Button(self.control, bg="#fa0000", text="Next", width=15, 
                            border=0, height=2, font=self.font)
        self.next.grid(row=4, column=0, padx=10, pady=10)


    def count(self):
        self.insert_new_row()
    
    
    def create_table(self, gui):
        self.gui = gui    
        self.total_rows = len(self.employee_list)
        self.total_columns = len(self.employee_list[0])
 

        # An approach for creating the table
        for i in range(self.total_rows):
            temp = []
            for j in range(self.total_columns):
                if i ==0:
                    if j == 0:
                        self.entry = Label(self.gui, width=5, bg='LightSteelBlue',fg='Black', border=1, 
                                        text=self.employee_list[i][j], font=('Arial', 16, 'bold'))
                    else:
                        self.entry = Label(self.gui, width=20, bg='LightSteelBlue',fg='Black', border=1,
                                        text=self.employee_list[i][j], font=('Arial', 16, 'bold'))
                else:
                    if j == 0:
                        self.entry = Label(self.gui, width=5, fg='blue', border=1,  
                                        text=self.employee_list[i][j], font=('Arial', 16, 'bold'))
                    else:
                        self.entry = Label(self.gui, width=20, fg='blue', border=1, 
                                        text=self.employee_list[i][j], font=('Arial', 16, 'bold'))

                self.entry.grid(row=i, column=j, ipadx=0)
                temp.append(self.entry)
            self.rows.append(temp)


    def insert_new_row(self):
        print(len(self.rows))
        self.last_row = len(self.rows)
        for i in range(1):
            temp = []
            for j in range(self.total_columns):
                if i ==0:
                    if j == 0:
                        self.entry = Label(self.gui, width=5, fg='Black', border=1,
                                       font=('Arial', 16, 'bold'))
                        # self.entry.insert(END, f"{self.last_row}")
                    else:
                        self.entry = Label(self.gui, width=20,fg='Black', border=1,
                                        font=('Arial', 16, 'bold'))
                        # self.entry.insert(END, "")

                self.entry.grid(row=self.last_row + i, column=j)
                
                temp.append(self.entry)
            self.rows.append(temp)


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # super().__init__()
        # print(self.employee_list)

        main_frame_bg =  "#050022" #"#010530"
        self.login_section_bg = "#3400f0"
        self.font_color = "#01011f" #"#E1341E"

        self.controller = controller
        self.configure(bg=main_frame_bg)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.font = tkFont.Font(family="Arial", size=16, weight="bold")
        out_font = tkFont.Font(family="Arial", size=12, weight="bold")
        self.conn_flag = False

        self.server_list = LabelFrame(self, text="Server")
        self.server_list.grid(row=0, column=0)


        self.session = LabelFrame(self, text="Session")
        self.session.grid(row=0, column=1)

        

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # print screen size
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()

        self.title("Pre Post Check")
        self.geometry("{}x{}+350+150".format(620, 420))
        self.resizable(True, True)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (PageOne,):
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