import os
import math
from pathlib import Path


def progressBar(iterator, total, length=30):
    y = int(math.ceil(iterator * length) / total)
    print("│" + ("▚" * y) + "┈" * (length - y) + "│", end='\r')


def rename(path, sel_dir):
    formats = ['.jpg', '.jpeg', '.png']
    print(" " * 50, end='\r')
    print("Choose the format:")
    for i, format in enumerate(formats):
        print(i+1, "-", format)

    choice = int(input())
    while choice - 1 > len(dir_names) or choice <= 0:
        if choice == 0:
            exit()
        print("\033[A                             \033[A")
        print(choice, "is not valid, enter a valid entry or '0' to quit")
        choice = int(input())
        print("\033[A                             \033[A")

    print("\033[A                             \033[A")
    print("┌" + "─" * len(formats[choice-1]) + "┐")
    print("│" + formats[choice-1] + "│")
    print("└" + "─" * len(formats[choice-1]) + "┘")
    elements = len(os.listdir(path))

    new_path = Path(path)
    new_dir_name = sel_dir + "_proc"
    temp_dir = new_path.parent.joinpath(new_dir_name)
    os.mkdir(temp_dir)

    for i, each_file in enumerate(new_path.glob('*.*')):
        progressBar(i, elements)
        each_file.rename(temp_dir.joinpath(str(i)+""+str(formats[choice-1])))
    print(" " * 50, end='\r')
    temp_dir.rename(path)
    print("Renaming completed successfully. Closing.")


if __name__ == '__main__':
    abs_path = os.getcwd()
    dir_names = []
    for file_name in os.listdir(abs_path):
        if file_name[-3:] != '.py' and file_name[0] != '.':
            dir_names.append(file_name)
    print("Choose the directory: ")
    for i, dir_name in enumerate(dir_names):
        print(i + 1, "-", dir_name)
    choice = int(input())

    while choice - 1 >= len(dir_names) or choice <= 0:
        if choice == 0:
            exit()
        print("\033[A                             \033[A")
        print(choice, "is not valid, enter a valid entry or '0' to quit")
        choice = int(input())
        print("\033[A                             \033[A")

    print("\033[A                             \033[A")
    target_path = abs_path + "/" + dir_names[choice - 1]

    print("┌" + "─" * len(target_path) + "┐")
    print("│" + target_path + "│")
    print("└" + "─" * len(target_path) + "┘")

    files = os.listdir(target_path)
    file_names = []
    print("Choose one of the following categories: ")
    for file in files:
        if file[0] != '.':
            file_names.append(file)
    for i, file in enumerate(file_names):
        print(i + 1, "-", file)
    choice = int(input(""))
    while choice - 1 >= len(file_names) or choice <= 0:
        if choice == 0:
            exit()
        print("\033[A                             \033[A")
        print(choice, "is not valid, enter a valid entry or '0' to quit")
        choice = int(input(""))
        print("\033[A                             \033[A")

    print("\033[A                             \033[A")
    sel_dir = file_names[choice - 1]
    final_path = target_path + "/" + file_names[choice - 1]
    rel_path = final_path.replace(abs_path, '')
    n_elements = len(os.listdir(final_path)) - 1
    n_elements_string = str(n_elements)+" elements"
    print("┌" + "─" * (len(rel_path) + 3) + "┐ ┌"+"─" * (len(n_elements_string)) + "┐")
    print("│" + "..." + rel_path + "│ │"+ n_elements_string + "│")
    print("└" + "─" * (len(rel_path) + 3) + "┘ └"+"─" * (len(n_elements_string)) + "┘")

    rename(final_path, sel_dir)
