"""
Date: 23-07-2022
Author: Arun Bansal
Objective: This file contains utility functions for the project.
    1. connect to the linux system with ssh
    2. Execute commands on the linux system
    5. return the output of the commands

License: copyright 2022 Arun Bansal
"""

from paramiko import SSHClient, AutoAddPolicy
from time import sleep
import pandas as pd
from threading import Thread
from random import randint


# Class for connecting to a remote host and executing commands
class RemoteHost(Thread):
    def __init__(self, host, username, password, command_list_path="", multiT=False):
        Thread.__init__(self)
        self.check_con_ = False
        self.host = host
        self.username = username
        self.password = password
        self.ssh = SSHClient()
        self.ssh.set_missing_host_key_policy(AutoAddPolicy())
        self.com_list_path = command_list_path

        self.multiT = multiT
        self.result = {}
        self.command_list = []
        with open(self.com_list_path, 'r') as fil:
            self.command_list = [i.replace("\n", "") for i in fil.readlines()]
        
        print(self.command_list)
        

    def connect(self):
        try:
            self.ssh.connect(self.host, username=self.username, password=self.password, timeout=5.0)
            self.check_con_ = True
            return True, "Connected to host: " + self.host
        except Exception as e:
            print("Could not connect to host: " + self.host)
            print("Error: " + str(e))
            return None, "Error: " + str(e)

    # Execute a command on the remote host
    def execute_command(self, command):
        if self.check_con_ == False:
            print("Could not connect to host: " + self.host)
            return None
        stdin, stdout, stderr = self.ssh.exec_command(command)
        st_out = f'STDOUT: \n{stdout.read().decode("utf8")}'
        st_err = f'STDERR: \n{stderr.read().decode("utf8")}'
        return st_out, st_err

    # Close the connection to the remote host
    def close(self):
        print("Clossing SSH Connection")
        self.ssh.close()


    def execute_all_command(self):
        na = randint(10,1000)
        if self.check_con_ == False:
            print("Could not connect to host From Execute: " + self.host)
            with open("result_folder/{}.txt".format(na), 'a', encoding="utf-8", errors="ignore") as f:
                f.write("ERROR :: \nCould not connect to host From Execute: " + self.host)
                f.write("\n")
            return False
        for command in self.command_list:
            out = self.execute_command(command)
            self.result[command] = out
            print("COMMAND: ", command)
            # print(out[0])
            # print(out[1])
            with open("result_folder/{}.txt".format(na), 'a') as f:
                f.write(command)
                f.write("{}".format(out[0]))
                f.write("{}".format(out[1]))
                f.write("\n-----------------------------\n")
            # input("---------------------\nPress Enter :")

        return True

    def run(self):
        self.connect()
        self.execute_all_command()
        self.close()


if __name__ == "__main__":
    host = "192.168.1.39"
    username = "pi"
    password = "pi1"
    servers = pd.read_csv("servers.csv")
    print(servers.head())
    for host, username, password in zip(servers["ip"], servers["username"], servers["password"]):
        print(type(host), type(username), type(password))
        remote_host = RemoteHost(host, username, password, command_list_path="command_list.txt")
        remote_host.start()
        print("Connected to host: " + host)
        # res = remote_host.execute_all_command()
        # print(res)
        
        print("clossing... the connection")
        remote_host.close()
        print("Connection closed")


