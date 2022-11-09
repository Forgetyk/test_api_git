# This is a sample Python script.
import git
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name} выфвфы HOTFIXaaa')  # Press Ctrl+F8 to toggle the breakpoint.

def new_func(task):
    print("new")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
repo = git.Repo('')
t = repo.head.commit.tree
print(repo.git.diff(t, "--name-only"))