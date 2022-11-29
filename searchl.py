import os

cmd = [i.replace(".TXT", "").lower() for i in os.listdir("logs\\session_1\\192.168.5.1\\post")]

st = input("Enter Query: ")
result = []
for cm in cmd:
    if st in cm:
        print(st, cm)
