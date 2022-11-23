from tkinter import * 
from tkinter import ttk
from random import randint, choice
from tkinter import scrolledtext
import tkinter.font as tkFont
import os

root = Tk()

def onselect(self, evt):
    w = evt.widget
    try:
        index = int(w.curselection()[0])
        value = w.get(index)
        # value = self.server_list.get(tk.ACTIVE)
        self.status.configure(text="SC: {}".format(value))
        print('You selected item "%s"' % ( value))
    except:
        print("Error")
        
    with open("logs\logs\server_48\pre\CPUINFO.TXT", "r") as f:
        txtbox.insert(END, f.read())
    
    with open("logs\logs\server_48\post\CPUINFO.TXT", "r") as f:
        txtbox1.insert(END, f.read())


w = root.winfo_screenwidth()
h = root.winfo_screenheight()

font = tkFont.Font(family="Helvetica", size=16, weight="bold")
out_font = tkFont.Font(family="Helvetica", size=12, weight="bold")


main_frame_bg =  "#ffffff" #225FDD" #"#010530"
login_section_bg = "#3400f0"
font_color = "#01011f" #"#E1341E"

root.title("Tab testing")
root.geometry("{}x{}+0+0".format(w-20, h-100))
# Create a main frame
pre_frame = LabelFrame(root, text="PRE")
pre_frame.grid(row=0, column=0)

# Text Area
# Create the textbox
txtbox = scrolledtext.ScrolledText(pre_frame, width=63, height=40, wrap=WORD)
txtbox.grid(row=0, column=0)

with open("logs\logs\server_48\pre\CPUINFO.TXT", "r") as f:
    txtbox.insert(END, f.read())

post_frame = LabelFrame(root, text="POST")
post_frame.grid(row=0, column=1)
# Create the textbox
txtbox1 = scrolledtext.ScrolledText(post_frame, width=63, height=40, wrap=WORD)
txtbox1.grid(row=0, column=0)

with open("logs\logs\server_48\post\CPUINFO.TXT", "r") as f:
    txtbox1.insert(END, f.read())


# Controll Section
       
command_frame = LabelFrame(root, text="Commands")
command_frame.grid(row=0, column=2)
server_list = Listbox(command_frame, bg=main_frame_bg, 
                                    fg=font_color, font=font, height=22, width=20)
server_list.grid(row=0, column=0, sticky="w", padx=2)
 
# Onselect Event
server_list.bind('<<ListboxSelect>>', onselect)

scr =  Scrollbar(command_frame)
scr.grid(row=0, column=1, sticky=E+W+N+S)

# Contecting to the listbox
scr.config(command=server_list.yview)
server_list.config(yscrollcommand=scr.set)
# Fetching Server List from File

cmd = [i.replace(".TXT", "") for i in os.listdir("logs\logs\server_48\post")]

for line in cmd:
    server_list.insert(END, line.strip())


next = Button(command_frame, text="Next", font=font, width=10, bg="#00D2ff",
                                fg="black", border=0)
next.grid(row=1, column=0)

quit = Button(command_frame, text="Exit", font=font, width=10, bg="#00D2ff",
                                fg="black", border=0)
quit.grid(row=2, column=0, pady=10)

root.mainloop()