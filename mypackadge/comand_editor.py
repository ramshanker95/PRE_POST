import tkinter as tk
from tkinter import filedialog, Text
import tkinter.messagebox as messagebox
import tkinter.font as tkFont


class CommandTextEditor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        w = self.winfo_screenwidth() - 40
        h = self.winfo_screenheight() -40

        size = 15
        fh = round((h - 240)/size) - 10
        fw = round(((w - 200)/10))
        self.save_flag = True

        out_font = tkFont.Font(family="Helvetica", size=size)

        self.controller = controller
        self.editor = tk.LabelFrame(self, text="Add List of Commands")
        self.editor.grid(row=0, column=0)

        self.text_area = Text(self.editor, width=fw, height=fh, font=out_font)
        self.text_area.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        # self.text_area.pack(side="left")

        self.scrollbar = tk.Scrollbar(self.editor, command=self.text_area.yview)
        self.scrollbar.grid(row=0, column=1, sticky="nsew")
        # self.scrollbar.pack(side="left")

        self.text_area.config(yscrollcommand=self.scrollbar.set)

        self.control_buttom = tk.Frame(self, width=fw)
        self.control_buttom.grid(row=1, column=0)

        self.save_button = tk.Button(self.control_buttom, text="Save",width=20, bg="#07eb44",
                      fg="black", border=0, height=2, command=self.save_file)
        self.save_button.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        # self.save_button.pack(side="left")

        self.back_button = tk.Button(self.control_buttom, text="Back",width=20, bg="#ED425D",
                      fg="black", border=0, height=2, command=self.go_back)
        self.back_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        self.open_file()

        self.text_area.bind("<Control-s>", self.save_file)
        self.text_area.bind("<Control-S>", self.save_file)
        self.text_area.bind("<Key>", self.save_chacker)


    def open_file(self):
        # filepath = filedialog.askopenfilename()
        with open("command_list.txt", 'r') as f:
            data = f.read()
            self.text_area.insert(tk.END, data)

    def save_file(self, event=None):
        # filepath = filedialog.asksaveasfilename()
        with open("command_list.txt", 'w') as f:
            data = self.text_area.get(1.0, tk.END)
            f.write(data)
            self.save_flag = True
        
        messagebox.showinfo("File Saved", "The file has been saved successfully.")
    
    def go_back(self):
        if self.save_flag:
            # data has been saved, close the application
            self.controller.show_frame(0)
        else:
            # data has not been saved, show a warning message
            tk.messagebox.showwarning("Warning", "Please save your changes")
    
    def save_chacker(self, event=None):
        self.save_flag = False


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


        self.fl = []
        for F in (CommandTextEditor, ):
            frame = F(container, self)
            self.fl.append(frame)
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(0)

    def show_frame(self, cont):
        # frame = self.frames[cont]
        frame = self.fl[cont]
        frame.tkraise()


if __name__ == "__main__":
    import sys
    app = MainWindow()
    app.mainloop()
    sys.exit()