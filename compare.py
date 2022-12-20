import os
import csv 
import sys

mode = input("Enter the mode: ")

ROOT = ""
PRE = r"logs\session_1\192.168.5.1\pre"
POST = r"logs\session_1\192.168.5.1\post"
RES = r"logs\session_1\192.168.5.1\res"
RT = r"logs\\session_1\\192.168.5.1\\"

ig_cmd = [cmd.replace("\n", "") for cmd in open("cmd_ignore.txt").readlines()]
print(ig_cmd)

pre_files = [PRE + "/" + i for i in  os.listdir(ROOT + PRE)]
post_files = [POST + "/" + i for i in  os.listdir(ROOT + POST)]
ignore_files = []

if pre_files.__len__() != post_files.__len__():
    print("There is some file missing in folder.")
    print(f"{pre_files.__len__()} Files in pre test but,")
    print(f"{post_files.__len__()} Files in post test")
    pre_test = os.listdir(ROOT + PRE)
    post_test = os.listdir(ROOT + POST)
    for pfile in pre_test:
        if pfile not in post_test:
            print(f"NOT FOUND in Post test: {pfile}")
            ignore_files.append(PRE + "/" + pfile)
        
        if pfile not in pre_test:
            print(f"NOT FOUND in Pre test: {pfile}")
            ignore_files.append(POST + "/" + pfile)
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
if mode.lower() == "hard":
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
            success_falg = False if post.split(".")[0] not in ig_cmd else True
        index += 1
        open(f"{RT}resut.txt", 'w').write("Success") if success_falg else open(f"{RT}resut.txt", 'w').write("Faild")


elif mode.lower() == "soft":
    compare_result = [["Sn", "pre test", "post test", "result", "result_2", "error", "error_line"]]
    index = 0
    success_falg = True
    for pre, post in zip(pre_files, post_files):
        error_line = ""
        with open(pre, "r") as pf:
            # pre_read = "".join(sorted(pf.read()))
            pre_read = pf.readlines()
        
        with open(post, "r") as rf:
            # post_read = "".join(sorted(rf.read()))
            post_read = rf.readlines()

        count = 0
        # Pre to post check
        for ind, pl1 in enumerate(pre_read):
            if pl1 not in post_read:
                count += 1
                print(f"ERROR: {pl1}")
                print(f"Error pre in Line: {ind}")
                error_line += f"-pr={ind+1}"

        # Post to pre check
        for ind, pl1 in enumerate(post_read):
            if pl1 not in pre_read:
                count += 1
                print(f"ERROR: {pl1}")
                print(f"Error post in Line: {ind}")
                error_line += f"-po={ind+1}"

        if count == 0:
            print("Success")
            compare_result.append([index, pre.split("/")[-1], post.split("/")[-1], "success", 1, count , error_line])
        else:
            print(f"fails {count} times in {post}")
            compare_result.append([index, pre.split("/")[-1], post.split("/")[-1], "filed", 0, count, error_line])
        index += 1
else:
    print(f"Failed To initialized with mode: {mode}")

# write result in csv file in result folder
with open(ROOT+RES+"/"+"result.csv", "w") as res_file:
    writer = csv.writer(res_file)
    writer.writerows(compare_result)
    print("Result Saved")

print("End the programm")
sys.exit()