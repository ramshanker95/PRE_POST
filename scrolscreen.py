from tkinter import * 
from tkinter import ttk
from random import randint, choice

root = Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

root.title("Tab testing")
root.geometry("{}x{}+0+0".format(w-20, h-100))
# Create a main frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# create aCanva
my_canva = Canvas(main_frame)
my_canva.pack(side=LEFT, fill=BOTH, expand=1)

# add a scroll bar
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canva.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# configure the canva
my_canva.configure(yscrollcommand=my_scrollbar.set)
my_canva.bind("<Configure>", lambda e: my_canva.configure(scrollregion=my_canva.bbox("all")))

# create a another frame inside the canva
second_fram = Frame(my_canva)


# add that new frame to a window inthe canvas
my_canva.create_window((0,0), window=second_fram, anchor="nw")

# data table
stat = ["pass", "fiald"]
error = ["NA", "Connection Error", "Authentication Error", "Other"]
os_name = ["Ubuntu", "kali Linux", "Unix", "Fadora"]


serial_number = [i for i in range(1, 255)]
servers = ["192.16.8.{}".format(i) for i in range(1, 255)]
kernals = ["CTP-T56-M{}".format(randint(0, 1000)) for _ in range(1, 100)]
Errors = ["{}".format(choice(error)) for _ in range(1, 100)]
os_names = ["{}".format(choice(os_name)) for _ in range(1, 100)]
test_results = ["{}".format(choice(stat)) for _ in range(1, 100)]


i = 1
for sn, ser, os, ker, err, res in zip(serial_number, servers, os_names, kernals, Errors, test_results):
    if i%2 == 0:
        Label(second_fram, text="{}".format(sn), width=15, bg="#c2c2c4").grid(row=i, column=0, pady=2, padx=0)
        Label(second_fram, text="{}".format(ser), width=15, bg="#c2c2c4").grid(row=i, column=1, pady=2, padx=0)
        Label(second_fram, text="{}".format(os), width=15, bg="#c2c2c4").grid(row=i, column=2, pady=2, padx=0)
        Label(second_fram, text="{}".format(ker), width=15, bg="#c2c2c4").grid(row=i, column=3, pady=2, padx=0)
        Label(second_fram, text="{}".format(err), width=15, bg="#c2c2c4").grid(row=i, column=4, pady=2, padx=0)
        if res == "fiald":
            Label(second_fram, text="{}".format(res), width=15, bg="red").grid(row=i, column=5, pady=2, padx=0)
            Button(second_fram, text="View", width=15, border=0, bg="#526345").grid(row=i, column=6, pady=2, padx=20)
        else:
            Label(second_fram, text="{}".format(res), width=15, bg="green").grid(row=i, column=5, pady=2, padx=0)
            Button(second_fram, text="View", width=15, border=0, bg="#526345").grid(row=i, column=6, pady=2, padx=20)

    else:
        Label(second_fram, text="{}".format(sn), width=15, bg="#a3a3a3").grid(row=i, column=0, pady=2, padx=0)
        Label(second_fram, text="{}".format(ser), width=15, bg="#a3a3a3").grid(row=i, column=1, pady=2, padx=0)
        Label(second_fram, text="{}".format(os), width=15, bg="#a3a3a3").grid(row=i, column=2, pady=2, padx=0)
        Label(second_fram, text="{}".format(ker), width=15, bg="#a3a3a3").grid(row=i, column=3, pady=2, padx=0)
        Label(second_fram, text="{}".format(err), width=15, bg="#a3a3a3").grid(row=i, column=4, pady=2, padx=0)
        if res == "fiald":
            Label(second_fram, text="{}".format(res), width=15, bg="red").grid(row=i, column=5, pady=2, padx=0)
            Button(second_fram, text="View", width=15, border=0, bg="#526345").grid(row=i, column=6, pady=2)
        else:
            Label(second_fram, text="{}".format(res), width=15, bg="green").grid(row=i, column=5, pady=2, padx=0)
            Button(second_fram, text="View", width=15, border=0, bg="#526345").grid(row=i, column=6, pady=2)
    i += 1


root.mainloop()