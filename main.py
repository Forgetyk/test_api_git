import os
import re
import sys
import git


def init():
    vars = []
    roles = []
    for file in list_changed:
        with open(f"{main_dir}/{file}", mode="r", encoding="utf-8") as file:
            for line in file:
                if re.fullmatch(r"^\S+:", line):
                    vars.append(line[:-2])
    for root, dir, files in os.walk(f"{main_dir}/roles"):
        for file in files:
            if file[-4:] != "yaml" or file[-3:] != "yml":
                continue
            with open(f"{root}/{file}", mode="r", encoding="utf-8") as file_role:
                for var in vars:
                    if var in file_role:
                        roles.append(root.split("roles/")[1].split("/")[0])
    for file in os.listdir(main_dir):
        if file[-4:] != "yaml" or file[-3:] != "yml":
            continue
        with open(f"{main_dir}/{file}", mode="r", encoding="utf-8") as playbook:



if __name__ == '__main__':
    global list_changed
    global main_dir
    main_dir = os.path.abspath(__file__).split("/")[:-1]
    list_changed = git.Repo('').git.diff('HEAD~1', '--name-only').split("\n")
    if len(list_changed) == 0:
        print("no modified files found")
        sys.exit(0)
    if sys.argv[1] == "--init":
        init()
