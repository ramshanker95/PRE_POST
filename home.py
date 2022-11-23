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

# https://developers.turing.com/dashboard/turing_test?s=outbound

global file_name
file_name = "{}".format(datetime.today())
file_name = file_name.replace(".", "_").replace("-", "_").replace(":", "_").replace(" ", "_")
print(file_name)
# with open("logs/{}.log".format(file_name), "w") as f:
#     f.write("{}\t{}".format(datetime.today(), "------"))

def my_logger(message=""):
    with open("logs/{}.log".format(file_name), "a") as f:
        f.write("{}\t{}\n".format(datetime.today(), message))



default_text = """[root@rhel7 ~]# df -hT
    Filesystem                  Type      Size  Used Avail Use% Mounted on
    /dev/mapper/rhel_rhel7-root xfs        37G  1.8G   36G   5% /
    devtmpfs                    devtmpfs  484M     0  484M   0% /dev
    tmpfs                       tmpfs     496M     0  496M   0% /dev/shm
    tmpfs                       tmpfs     496M  6.8M  489M   2% /run
    tmpfs                       tmpfs     496M     0  496M   0% /sys/fs/cgroup
    /dev/sda1                   xfs      1014M  133M  882M  14% /boot
    /dev/mapper/TEST_VG-TEST_LV xfs       8.0G   33M  8.0G   1% /test
    tmpfs                       tmpfs     100M     0  100M   0% /run/user/0
"""


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
        my_logger("Login")
        my_logger(self.user_name_entry.get())
        my_logger(self.password_entry.get())

        if self.user_name_entry.get() == "admin" and self.password_entry.get() == "admin":
            my_logger("Login Successful")
            self.controller.show_frame(PageOne)
        else:
            my_logger("Login Failed Invalid Credentials")
            self.error_message.configure(text="Invalid User Name or Password!")



class PageOneP(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        main_frame_bg = "#225FDD" #"#010530"
        login_section_bg = "#3400f0"
        font_color = "#E1341E"

        self.controller = controller
        self.configure(bg=main_frame_bg)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        font = tkFont.Font(family="Helvetica", size=20, weight="bold")

        # Need to create 3 Frames 1. User Inputs, 2. server list, 3. Outputs logs
        # 1. User Inputs
        self.frame1 = tk.Frame(self, bg=login_section_bg, width=1020, height=620)
        self.frame1.place(relx=0.0, rely=0.0, anchor='center')

        # 2. Server List
        self.frame2 = tk.Frame(self, bg="#0f0f0f", width=400, height=620)
        self.frame2.place(relx=0.86, rely=0.0, anchor='center')

        # 3. Outputs logs
        self.frame3 = tk.Frame(self, bg="#ff0f0f", width=1640, height=250)
        self.frame3.place(relx=0.0, rely=0.9, anchor='center')
        
        btn = tk.Button(self, text="next", command=lambda: controller.show_frame(PageTwo))
        btn.place(relx=0.5, rely=0.9, anchor='center')


class PageOneV1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        main_frame_bg = "#225FDD" #"#010530"
        login_section_bg = "#3400f0"
        font_color = "#E1341E"

        self.controller = controller
        self.configure(bg=main_frame_bg)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        font = tkFont.Font(family="Helvetica", size=20, weight="bold")

        # Need to create 3 Frames 1. User Inputs, 2. server list, 3. Outputs logs
        # 1. User Inputs
        self.frame1 = tk.Frame(self, bg="#ff000f")
        self.frame1.pack(side="left", fill="both", expand=True)

        # 2. Server List
        self.frame2 = tk.Frame(self, bg="#0f0fff")
        self.frame2.pack(side="right", fill="both", expand=True)

        # 3. Outputs logs
        self.frame3 = tk.Frame(self, bg="#ff0f0f")
        self.frame3.pack(side="bottom", fill="both", expand=True)

        # Page Title
        self.page_title = tk.Label(self, text="File Extension in Linux", bg=main_frame_bg, fg=font_color, font=font)
        self.page_title.pack(side="top", fill="y", expand=True)
        
        # User ID
        self.id = tk.Label(self.frame1, text="User Id", bg="#ff000f", fg=font_color, font=font)
        self.id.grid(row=0, column=0, sticky="w")
        self.id_entry = tk.Entry(self.frame1, font=font, width=40)
        self.id_entry.grid(row=0, column=1, sticky="w")

        # Password
        self.password = tk.Label(self.frame1, text="password", bg="#ff000f", fg=font_color, font=font)
        self.password.grid(row=1, column=0, sticky="w")
        self.password_entry = tk.Entry(self.frame1, font=font, width=40)
        self.password_entry.grid(row=1, column=1, sticky="w")

        # Name of File Sydtem to Extend
        self.fileSystem = tk.Label(self.frame1, text="File System", bg="#ff000f", fg=font_color, font=font)
        self.fileSystem.grid(row=2, column=0, sticky="w")
        self.fileSystem_entry = tk.Entry(self.frame1, font=font, width=40)
        self.fileSystem_entry.grid(row=2, column=1, sticky="w")

        # Disk name
        self.disk_name = tk.Label(self.frame1, text="Disk Name", bg="#ff000f", fg=font_color, font=font)
        self.disk_name.grid(row=3, column=0, sticky="w")
        self.disk_name_entry = tk.Entry(self.frame1, font=font, width=40)
        self.disk_name_entry.grid(row=3, column=1, sticky="w")

        # Disk Size
        self.disk_size = tk.Label(self.frame1, text="Disk Size", bg="#ff000f", fg=font_color, font=font)
        self.disk_size.grid(row=4, column=0, sticky="w")
        self.disk_size_entry = tk.Entry(self.frame1, font=font, width=40)
        self.disk_size_entry.grid(row=4, column=1, sticky="w")

        
        btn = tk.Button(self, text="next", command=lambda: controller.show_frame(PageTwo))
        btn.place(relx=0.5, rely=0.9, anchor='center')


        
        # Group1 Frame ----------------------------------------------------
        group1 = tk.LabelFrame(self.frame3, text="Text Box", padx=5, pady=5)
        group1.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        group1.rowconfigure(0, weight=1)
        group1.columnconfigure(0, weight=1)

        # Create the textbox
        txtbox = scrolledtext.ScrolledText(group1, width=40, height=10, wrap=tk.WORD)
        txtbox.grid(row=0, column=0)



class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        main_frame_bg =  "#ffffff" #225FDD" #"#010530"
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

        # Need to create 3 Frames 1. User Inputs, 2. server list, 3. Outputs logs
        # 1. User Inputs
        self.frame1 = tk.LabelFrame(self, text="User Inputs", 
                                    bg=main_frame_bg, padx=5,
                                    pady=5, border=1)
        self.frame1.grid(row=0, column=0, sticky="w", rowspan=2,
                                    padx=10, pady=00, ipadx=10,
                                    ipady=10)
                                

        # User Name
        self.user_name = tk.Label(self.frame1, text="User Name", bg= main_frame_bg, fg=font_color, font=font)
        self.user_name.grid(row=0, column=0, sticky="w", pady=2)
        self.user_name_entry = tk.Entry(self.frame1, font=font,
                                    width=20, border=2)
        self.user_name_entry.grid(row=0, column=1, sticky="w", pady=2)

        # Password
        self.password = tk.Label(self.frame1, text="Password", bg=main_frame_bg, fg=font_color, font=font)
        self.password.grid(row=1, column=0, sticky="w")
        self.password_entry = tk.Entry(self.frame1, font=font, width=20, show="*")
        self.password_entry.grid(row=1, column=1, sticky="w", pady=2)

        # File System to extend
        self.fileSystem = tk.Label(self.frame1, text="File system to Extend", bg=main_frame_bg, fg=font_color, font=font)
        self.fileSystem.grid(row=2, column=0, sticky="w")
        self.fileSystem_entry = tk.Entry(self.frame1, font=font, width=20)
        self.fileSystem_entry.grid(row=2, column=1, sticky="w", pady=2)

        # Disk Name
        self.disk_name = tk.Label(self.frame1, text="New Disk Name", bg=main_frame_bg, fg=font_color, font=font)
        self.disk_name.grid(row=3, column=0, sticky="w", pady=2)
        self.disk_name_entry = tk.Entry(self.frame1, font=font, width=20)
        self.disk_name_entry.grid(row=3, column=1, sticky="w", pady=2)

        # Disk Size
        self.disk_size = tk.Label(self.frame1, text="Current Disk Size", bg=main_frame_bg, fg=font_color, font=font)
        self.disk_size.grid(row=4, column=0, sticky="w", pady=2)
        self.disk_size_entry = tk.Entry(self.frame1, font=font, width=20)
        self.disk_size_entry.grid(row=4, column=1, sticky="w", pady=2)

        # Status of Server
        self.status = tk.Label(self.frame1, text="SN: --.--.--.--", bg="red", fg="black", font=font)
        self.status.grid(row=5, column=0, sticky="w", pady=2, columnspan=2)

        # Connect to Server
        self.connect_server = tk.Button(self.frame1,text="Connect",
                                font=font, width=10, bg="#00D2ff",
                                fg="black", command=self.Connect_ip, 
                                border=0)
        self.connect_server.grid(row=5, column=1, sticky="w", pady=2, columnspan=2)


        # # Connect Button
        # self.btn_next = tk.Button(self.frame1, text="Connect",
        #                         font=font, width=10,
        #                         bg="#00D2FF", fg="black", border=0,
        #                         command=self.Connect_server)
        # self.btn_next.grid(row=5, column=1, padx=5, pady=1)


        self.serv = tk.LabelFrame(self, text="Server List", 
                                bg=main_frame_bg, padx=5,
                                pady=5, border=1)
        self.serv.grid(row=0, column=1, sticky="w", rowspan=2, padx=20, pady=0)
    
        self.server_list = tk.Listbox(self.serv, bg=main_frame_bg, 
                                    fg=font_color, font=font, height=8
                                    )
        self.server_list.grid(row=0, column=0, sticky="w", padx=2)
        
        # Onselect Event
        self.server_list.bind('<<ListboxSelect>>', self.onselect)

        self.scr =  tk.Scrollbar(
                                self.serv
                                )
        self.scr.grid(row=0, column=1, sticky=E+W+N+S)

        # Contecting to the listbox
        self.scr.config(command=self.server_list.yview)
        self.server_list.config(yscrollcommand=self.scr.set)

        # Fetching Server List from File
        with open("server_list.txt", "r") as f:
            for line in f:
                if line.strip():
                    self.server_list.insert(tk.END, line.strip())
                    my_logger("Server List: {}".format(line.strip()))


        # 3. Output Frame----------------------------------------------------
        self.group1 = tk.LabelFrame(self, text="Output", padx=5, pady=5)
        self.group1.grid(row=5, column=0, columnspan=3, padx=10, 
                        pady=10, sticky=E+W+N+S)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.group1.rowconfigure(0, weight=1)
        self.group1.columnconfigure(0, weight=1)

        # Create the textbox
        self.txtbox = scrolledtext.ScrolledText(self.group1, width=60,
                                            height=14, font=out_font,
                                            )

        self.txtbox.grid(row=0, column=0, sticky=E+W+N+S)
    
        # Bind A event to the textbox
        # self.txtbox.bind("<Key>", self.on_key)

        # with open("home.py", "r") as f:
        #     self.txtbox.insert(tk.END, f.read())
        self.txtbox.config(state=tk.DISABLED, exportselection=0)

        # self.txtbox.insert(tk.END, "Welcome to the Disk Extendtion Tool")

        # Create 3 buttons 1. Previous 2.Next 3. Exit
        # frame for control butto
        self.control_frame = tk.Frame(self, bg=main_frame_bg)
        self.control_frame.grid(row=6, column=0, columnspan=2, pady=2)

        # Add Server IP
        self.add_server = tk.Button(self.control_frame, text="Add server",
                                font=font, width=10, bg="#00D2ff",
                                fg="black", command=self.next_page, border=0)
        self.add_server.grid(row=0, column=0, padx=5, pady=1)

        # prev Button
        self.btn_prev = tk.Button(self.control_frame, text="Next",
                                font=font, width=10,
                                bg="#00D2FF", fg="black", border=0,
                                command=self.run_next_command)
        self.btn_prev.grid(row=0, column=1, padx=5, pady=1)

        # next Button
        self.btn_next = tk.Button(self.control_frame, text="Exit",
                                font=font, width=10,
                                bg="#00D2FF", fg="black", border=0,
                                command= self.exit_tool)
        self.btn_next.grid(row=0, column=2, padx=5, pady=1)

        # Refresh Button
        self.btn_exit = tk.Button(self.control_frame, text="Refresh IP",
                                font=font, width=10,
                                bg="#00D2FF", fg="black", border=0,
                                command=self.update_ip)
        self.btn_exit.grid(row=0, column=3, padx=5, pady=1)

        # Clear output Button
        self.btn_clear = tk.Button(self.control_frame, text="Clear",
                                    font=font, width=10,
                                    bg="#00D2FF", fg="black", border=0,
                                command=self.clear_output)
        self.btn_clear.grid(row=0, column=4, padx=5, pady=1)

        self.btn_prev.configure(state=tk.DISABLED)
        # self.btn_next.configure(state=tk.DISABLED)
        # self.btn_exit.configure(state=tk.DISABLED)


        # Controler of the page

        self.update_ip()

    def clear_output(self):
        if self.confirm("Are you sure you want to clear the output?"):
            self.txtbox.config(state=tk.NORMAL)
            self.txtbox.delete(1.0, tk.END)
            self.txtbox.config(state=tk.DISABLED)
            my_logger("Are Youo Sure? Yes: Cleared the output")
        else:
            pass

    def update_ip(self):
        self.server_list.delete(0, tk.END)
        with open("server_list.txt", "r") as f:
            for line in f:
                if line.strip():
                    self.server_list.insert(tk.END, line.strip())
                    my_logger("Server List: {}".format(line.strip()))

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


    def run_next_command(self):
        if self.current_command == len(self.commad_list_for):
            self.btn_next.configure(state=tk.DISABLED)
            dft = self.remote_host.execute_command("df -hT {}".format(file_to_extend))
            self.console_out(dft[0])
            return
        self.btn_prev.configure(state=tk.NORMAL)

        if self.current_command > len(self.commad_list_for):
            self.current_command = -1

        nc = self.commad_list_for[self.current_command]
        self.next_out = self.remote_host.execute_command(nc)[0]
        self.console_out(self.next_out)
        self.current_command += 1  


    def prev_page(self):
        # self.controller.show_frame("PageOne")
        if self.current_command == 0:
            self.current_command = 0
            self.btn_prev.configure(state=tk.DISABLED)
            return
        self.btn_next.configure(state=tk.NORMAL)
        self.current_command -= 1
        nc = self.commad_list_for[self.current_command]
        self.next_out = self.remote_host.execute_command(nc)[0]
        self.console_out(self.next_out)


    def next_page(self):
        self.controller.show_frame(PageTwo)
        print("Next Page")


    def exit_tool(self):
        my_logger("Exit Tool Confirm?")
        if self.confirm("Are you sure you want to exit?"):
            my_logger("Exit Tool: Yes")
            self.controller.destroy()
            print("Exit Tool")
        else:
            my_logger("Exit Tool: No")
            pass


    def console_out(self, text):
        my_logger("Console Out: {}".format(text))
        self.txtbox.config(state=tk.NORMAL)
        self.txtbox.insert(tk.END, text+"\n")
        self.txtbox.config(state=tk.DISABLED)
        self.txtbox.see(tk.END)

    def Connect_ip(self):
        # print all input from entry box
        username = self.user_name_entry.get()
        password = self.password_entry.get()
        file_to_extend = self.fileSystem_entry.get()
        new_disk_name = self.disk_name_entry.get()
        new_disk_size = self.disk_size_entry.get()

        # Logging All Entry Box
        my_logger("Logging All Entry Box")
        my_logger("Username: {}".format(username))
        my_logger("Password: {}".format(password))
        my_logger("File to Extend: {}".format(file_to_extend))
        my_logger("New Disk Name: {}".format(new_disk_name))
        my_logger("New Disk Size: {}".format(new_disk_size))

        # Check if all entry box is empty
        if not self.check_entry_box(username, password, file_to_extend, new_disk_name, new_disk_size):
            self.console_out("Some Entry Box is Empty")
            return False

        # Connect to the server
        try:
            host = self.server_list.get(self.server_list.curselection())
            self.console_out(host)
        except:
            self.console_out("Please select a server")
            self.error_message("No server selected")
            return False

        # Connect to the server
        self.console_out("Connecting to " + host)
        self.remote_host = RemoteHost(host, username, password)
        self.report = self.remote_host.connect()
        if self.report[0] is not None:
            self.console_out("Connected to host: " + host)
            self.conn_flag = True
            self.connect_server.config(text="Connected", bg="#00110f",
                                    fg="black")
            self.connect_server.configure(state=tk.DISABLED)
        else:
            self.console_out("Failed to connect to host: " + host)
            self.console_out(self.report[1])
            self.error_message("Failed to connect to host: " + host)
            return False

        my_logger("Execute Command: df -hT {}".format(file_to_extend))
        ress = ""
        dft = self.remote_host.execute_command("df -hT {}".format(file_to_extend))
        if dft:
            self.console_out(dft[0])
            abc = imp_lines(dft[0])
            # abc = imp_lines(default_text)
            print("-<>>", abc)
            if abc is not None:
                cmd = generate_command(abc, file_to_extend,
                                new_disk_name, new_disk_size)
                if cmd[0]:
                    for com in cmd[1]:
                        ress += com + "\n"
                        self.commad_list_for.append(com)

                    # self.commad_list_for = ["ls -l", "df -hT", "tree", "ls -la /dev"]
                    self.console_out(ress)
                    if self.confirm("Are you sure you want to execute the commands?\n\n" + ress):
                        self.btn_prev.configure(state=tk.NORMAL)
                        self.btn_next.configure(state=tk.NORMAL)
                    else:
                        self.console_out("Cancelled")
                        self.error_message("Cancelled")
                        return False
                else:
                    self.console_out("Failed to generate command" + cmd[1])
                    self.error_message("Failed to generate command" + cmd[1])
                    return False
            else:
                self.console_out("==========================\nERROR:: \nFailed to get LVM2 Mount point, \nPlease check correct LVM2 mount point again!! \nBTRFS Filesystem and SIOS managed Filesystem extentions are not supported by this application.\n========================")
        else:
            self.console_out("ERROR::\nFailed to Execute Command to get file system info")
            self.error_message("ERROR::\nFailed to Execute Command to get file system info")
            self.conn_flag = False
            self.remote_host.close() if self.conn_flag else None
            self.console_out("ERROR::\nCheck the server connection")
            return False

    # Function For checking the Entry Box is empty or not and 
    # rise error message if empty
    def check_entry_box(self, username, password, file_to_extend, new_disk_name, new_disk_size):
        if username == "":
            self.console_out("ERROR::\nUsername is empty")
            self.error_message("Username is empty")
            return False
        if password == "":
            self.console_out("ERROR::\nPassword is empty")
            self.error_message("Password is empty")
            return False
        if file_to_extend == "":
            self.console_out("ERROR::\nFile System to Extend is empty")
            self.error_message("File to Extend is empty")
            return False
        if new_disk_name == "":
            self.console_out("ERROR::\nNew Disk Name is empty")
            self.error_message("New Disk Name is empty")
            return False
        if new_disk_size == "":
            self.console_out("ERROR::\nNew Disk Size is empty")
            self.error_message("New Disk Size is empty")
            return False
        print("Print True")
        return True

    def onselect(self, evt):
        # Note here that Tkinter passes an event object to onselect()
        if self.conn_flag:
            self.remote_host.close()
            print("Disconnected from host")
            self.console_out("Disconnected from host")
            self.conn_flag = False
            self.connect_server.configure(state=tk.NORMAL)
            self.connect_server.config(text="Connect", bg="red",
                                    fg="black")
            self.commad_list_for = []
            self.current_command = 0
            self.btn_prev.configure(state=tk.DISABLED)
            self.btn_next.configure(state=tk.DISABLED)

        w = evt.widget
        try:
            index = int(w.curselection()[0])
            value = w.get(index)
            # value = self.server_list.get(tk.ACTIVE)
            self.status.configure(text="SC: {}".format(value))
            print('You selected item "%s"' % ( value))
        except:
            pass
        

    # Define a function to show the error message
    def on_click(self):
        my_logger("SSH Error: Setrver IP is not correct")
        messagebox.showerror('SSH Error', 'Error: Setrver IP is not correct')

    def error_message(self, message):
        my_logger("Error Message: {}".format(message))
        messagebox.showerror('SSH Error', 'Error: {}'.format(message))



        
class PageTwo(tk.Frame):
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

        # self.btn_File = tk.Button(self.buttons_frame, text='NA',
        #                     font=font1, width=8,
        #                     bg="#00D2FF", fg="black", border=0
        #                     )
        # self.btn_File.grid(row=0, column=1, padx=10, pady=10)

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


        # for i in range(1, 255):
        #     self.txtbox.insert(tk.END, "192.168.1.{}\n".format(i))
        #     break
        
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
        self.controller.show_frame(PageOne)
        print("Backed")


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # print screen size
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()

        self.title("File Syatem Extender")
        self.geometry("820x600+{}+{}".format(int(w/2-410), int(h/2-300)))
        self.resizable(False, False)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Homepage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Homepage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    import sys
    my_logger("Started")
    app = MainWindow()
    app.mainloop()
    my_logger("Ended")
    my_logger("----------------------------------------------------")
    sys.exit()