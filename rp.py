# Importing the libraries
import pandas as pd
import numpy as np

df = pd.read_csv("server_lists\session_1\servers.csv")
print(df)

# print("===============")
# # Applying the condition
# # f = df.loc[df["ip"] == "192.168.5.6"]
# df.loc[df["ip"] == "192.168.5.6", "pass"] = "pi12345"
# df.loc[df["ip"] == "192.168.5.6", "user"] = "pi1"

# print(df)