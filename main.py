import os
import re
import sys
import git
import yaml


def init():
    vars = []
    roles = []
    playbooks = {}
    for file in list_changed:
        if file[-4:] != "yaml" and file[-3:] != "yml":
            continue
        with open(f"{main_dir}\\{file}", mode="r", encoding="utf-8") as file:
            for line in file:
                if re.fullmatch(r"^\S+:\n", line):
                    vars.append(line[:-2])
    for root, dir, files in os.walk(f"{main_dir}\\roles"):
        for file in files:
            if file[-4:] != "yaml" and file[-3:] != "yml":
                continue
            with open(f"{root}\\{file}", mode="r", encoding="utf-8") as file_role:
                for var in vars:
                    if var in file_role.read():
                        roles.append(root.split("roles\\")[1].split("\\")[0])
    roles = list(set(roles))
    for file in os.listdir(main_dir):
        if file[-4:] != "yaml" and file[-3:] != "yml":
            continue
        with open(f"{main_dir}\\{file}", mode="r", encoding="utf-8") as playbook:
            tmp = []
            for role in roles:
                if role in yaml.safe_load(playbook)[0]["roles"]:
                    tmp.append(role)
            playbooks[str(file)] = tmp
    for key in playbooks.keys():
        if re.search(r"git", key) is None:
            with open(f"{main_dir}\\{key}", 'r') as stream:
                hosts = yaml.safe_load(stream)[0]["hosts"]
                if type(hosts) == str:
                    print(f"{key}:\n  {hosts}")
                else:
                    print(f"{key}:\n")
                    for host in hosts:
                        print(f"  {host}")


if __name__ == '__main__':
    global list_changed
    global main_dir
    main_dir = "\\".join(os.path.abspath(__file__).split("\\")[:-1])
    list_changed = git.Repo('').git.diff('HEAD~1', '--name-only').split("\n")
    print(list_changed)
    if len(list_changed) == 0:
        print("no modified files found")
        sys.exit(1)
    init()
