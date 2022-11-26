import csv
import sys
import os

class CompareResult:
    def __init__(self, ROOT="", PRE="", POST="",
                RES="", RT="", IG_CMD_FILE=""):
        self.ROOT = ROOT
        self.PRE = PRE
        self.POST = POST
        self.RES = RES
        self.RT = RT
        self.IG_CMD_FILE = IG_CMD_FILE

        self.ignore_cmd = [cmd.replace("\n", "") for cmd in open(IG_CMD_FILE, 'r').readlines()]

    def bhai_check_karo(self):
        pre_files = [self.PRE + "/" + i for i in  os.listdir(self.ROOT + self.PRE)]
        post_files = [self.POST + "/" + i for i in  os.listdir(self.ROOT + self.POST)]
        ignore_files = []

        if pre_files.__len__() != post_files.__len__():
            print("There is some file missing in folder.")
            print(f"{pre_files.__len__()} Files in pre test but,")
            print(f"{post_files.__len__()} Files in post test")
            pre_test = os.listdir(self.ROOT + self.PRE)
            post_test = os.listdir(self.ROOT + self.POST)
            for pfile in pre_test:
                if pfile not in post_test:
                    print(f"NOT FOUND in Post test: {pfile}")
                    ignore_files.append(self.PRE + "/" + pfile)
                
                if pfile not in pre_test:
                    print(f"NOT FOUND in Pre test: {pfile}")
                    ignore_files.append(self.POST + "/" + pfile)
            if "y" not in input("Do you want to skip the file(y/n)?"):
                sys.exit(0)

        # remove Unmatched filename from files list
        for igf in ignore_files:
            if igf in pre_files:
                print("pre", pre_files.index(igf))
                pre_files.pop(pre_files.index(igf))

            if igf in post_files:
                print("post", post_files.index(igf))
                post_files.pop(post_files.index(igf))

        print(f"pre length: {pre_files.__len__()}")
        print(f"post length: {post_files.__len__()}")
        if post_files.__len__() == 0:
            print("Ther is no files fo compare")
            sys.exit()

        # Now Compareing The Files
        compare_result = [["Sn", "pre test", "post test", "result", "result_2", "error"]]
        index = 0
        success_falg = True
        for pre, post in zip(pre_files, post_files):
            with open(pre, "r") as pf:
                # pre_read = "".join(sorted(pf.read()))
                pre_read = pf.read()
            
            with open(post, "r") as rf:
                # post_read = "".join(sorted(rf.read()))
                post_read = rf.read()

            if pre_read == post_read:
                print("Succusses")
                compare_result.append([index, pre.split("/")[-1], post.split("/")[-1], "success", 1, 0])
            else:
                print(f"fails in {post}")
                print("Filed")
                compare_result.append([index, pre.split("/")[-1], post.split("/")[-1], "filed", 0, 0])
                success_falg = False if post.split(".")[0] not in self.IG_CMD_FILE else True
            index += 1
            open(f"{self.RT}resut.txt", 'w').write("Success") if success_falg else open(f"{self.RT}resut.txt", 'w').write("Faild")

            
if __name__ == "__main__":
    ROOT = ""
    PRE = r"logs\session_1\192.168.5.1\pre"
    POST = r"logs\session_1\192.168.5.1\post"
    RES = r"logs\session_1\192.168.5.1\res"
    RT = r"logs\\session_1\\192.168.5.1\\"
    IG = r"cmd_ignore.txt"
    obj = CompareResult(ROOT=ROOT, PRE=PRE, POST=POST, RES=RES, RT=RT, IG_CMD_FILE=IG)

    obj.bhai_check_karo()