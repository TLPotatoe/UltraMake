# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tlamit <titouan.lamit@gmail.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/20 21:23:48 by tlamit            #+#    #+#              #
#    Updated: 2025/12/15 18:19:07 by tlamit           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys
from math import floor
import time
import subprocess
from cursor_utils import *


def add_files(path: str) -> list[str]:
    cfiles = []
    for entry in os.scandir(path):
        if entry.is_dir():
            cfiles.extend(add_files(entry.path))
        if entry.is_file() and entry.name.endswith(".c"):
            cfiles.append(entry.path)
    return cfiles


def parceur(
    line: str, all_cfiles: list, cc_files: list, n: int, start_time: float
) -> int:

    if ".c" in line:
        cc_files.append(line)
    if "cc -" in line:
        n += 1
        print(f"{CURSOR_TO(10, 0)}{ERASE_LINE_FULL}{line.strip()}", end="", flush=True)
        print(
            f"{CURSOR_TO(11, 0)}{ERASE_LINE_FULL} \
{FG_GREEN}Compiled Files {n}{FG_DEFAULT}/{FG_MAGENTA}{len(all_cfiles)} \
            {FG_DEFAULT}{round(time.perf_counter() - start_time, 3)} sec.",
            end="",
            flush=True,
        )
        lentgh = min(100, os.get_terminal_size()[0] - 2)
        progress_value = int((n / len(all_cfiles)) * lentgh)
        filled = "█" * progress_value
        empty = "-" * (lentgh - progress_value)
        print(
            f"{CURSOR_TO(12, 0)}{ERASE_LINE_FULL}>{FG_GREEN}{filled}{FG_BRIGHT_YELLOW}{empty}{FG_DEFAULT}<"
        )

    return n


def run_subp(command: str, cwd: str = None) -> subprocess.Popen:
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=cwd,
        bufsize=1,
    )
    return process


def run_make(cwd: str):
    all_cfiles = add_files(cwd)
    cc_files = []
    command = "make re && make clean"
    if "DEBUG" in sys.argv:
        command = command[:8] + "DEBUG=True " + command[8:]
    print(command)
    t_start = time.perf_counter()
    process = run_subp(command, cwd)

    if process.stdout:
        n = 0
        for line in process.stdout:
            n = parceur(line, all_cfiles, cc_files, n, t_start)
    process.stdout.close()

    _, stderr = process.communicate()
    print(f"Make running for {round(time.perf_counter() - t_start, 3)} sec.")
    if stderr:
        print(f"\n{FG_BRIGHT_RED}--- STDERR ---")
        print(f"{FG_BRIGHT_RED}{stderr}", end="")
        return
    if not process.returncode:
        print(
            FG_BRIGHT_GREEN,
            f"\nProcess finished with exit code {process.returncode}",
            FG_DEFAULT,
        )
    newlist = []
    for i in cc_files:
        for x in all_cfiles:
            if i[i.rfind("/") + 1 : -1] == x[x.rfind("/") + 1 :]:
                newlist.append(x)
    if len(set(all_cfiles) - set(newlist)):
        print(FG_RED, "Files not compiled or not included:")
        for file in set(all_cfiles) - set(newlist):
            print(FG_BRIGHT_RED, file[len(cwd) :], FG_DEFAULT)


def run_norm(cwd: str):
    command = f"norminette {cwd}"
    n_process = run_subp(command, cwd)
    if n_process.stdout:
        lines = [line for line in n_process.stdout if "Error" in line]
        if len(lines):
            for line in lines:
                if "Error!" in line:
                    print(f"\n{FG_BRIGHT_RED}{line}{FG_DEFAULT}", end="")
                else:
                    print(line, end="")
        else:
            print(f"{FG_BRIGHT_GREEN}Norminette OK.")
    n_process.stdout.close()
    _, stderr = n_process.communicate()
    if stderr:
        print(f"\n{FG_BRIGHT_RED}--- STDERR ---")
        print(f"{FG_BRIGHT_RED}{stderr}", end="")
        return

def update():
    import requests
    from version import VERSION

def main():
    current_directory = os.getcwd()
    if not "Makefile" in os.listdir(current_directory):
        print(f"{FG_BRIGHT_RED}No MakeFile found in ./{FG_DEFAULT}")
        return
    run_make(current_directory)

    if "-n" in sys.argv:
        run_norm(current_directory)


if __name__ == "__main__":
    os.system("clear")
    # print(FG_BRIGHT_CYAN, """
    #        _                                       _
    #       | |  _                                  | |
    #  _   _| |_| |_  ____ _____         ____  _____| |  _ _____
    # | | | | (_   _)/ ___|____ |       |    \(____ | |_/ ) ___ |
    # | |_| | | | |_| |   / ___ |_______| | | / ___ |  _ (| ____|
    # |____/ \_) \__)_|   \_____(_______)_|_|_\_____|_| \_)_____)
    # """)
    print(
        f"""
{FG_BRIGHT_CYAN}Ultra - Make
"""
    )
    main()
    print(FG_DEFAULT)
