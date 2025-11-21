# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tlamit <titouan.lamit@gmail.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/20 21:23:48 by tlamit            #+#    #+#              #
#    Updated: 2025/11/21 01:58:54 by tlamit           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import subprocess


def add_files(path: str, files_list: list) -> None:
    for entry in os.scandir(path):
        if entry.is_dir():
            add_files(entry.path, files_list)
        if entry.is_file() and entry.name.endswith(".c"):
            files_list.append(entry.path)


n = 0
tlist = []


def parceur(line: str, all_cfiles: list) -> None:
    global n
    global tlist

    if ".c" in line:
        tlist.append(line)
    if "cc -Wall -Wextra -Werror" in line:
        print(f"\x1b[{10};{0}H", f"\x1b[{0}J", line, end="")
        n += 1
        print(len(all_cfiles), "/", n)
    else:
        print(f"\x1b[{10};{0}H", f"\x1b[{0}J", end="")
        print(len(all_cfiles), "/", n)


def main():
    current_directory = os.getcwd()
    all_cfiles = []
    add_files(current_directory, all_cfiles)
    command = "make re && make clean"

    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=current_directory,
        bufsize=1
    )

    if process.stdout:
        for line in process.stdout:
            parceur(line, all_cfiles)
    process.stdout.close()

    _, stderr = process.communicate()
    if stderr:
        print("\n--- STDERR ---")
        print(stderr, end='')

    print(f"\nProcess finished with exit code {process.returncode}")
    global tlist
    newlist = []
    for i in tlist:
        for x in all_cfiles:
            if i[i.rfind("/") + 1: -1] == x[x.rfind("/") + 1:]:
                newlist.append(x)
    print(set(all_cfiles) - set(newlist))


if __name__ == "__main__":
    os.system("clear")
    print("""
       _                                       _           
      | |  _                                  | |          
_   _| |_| |_  ____ _____         ____  _____| |  _ _____ 
| | | | (_   _)/ ___|____ |       |    \(____ | |_/ ) ___ |
| |_| | | | |_| |   / ___ |_______| | | / ___ |  _ (| ____|
|____/ \_) \__)_|   \_____(_______)_|_|_\_____|_| \_)_____)
    """)
    main()
