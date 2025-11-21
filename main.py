# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tlamit <titouan.lamit@gmail.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/20 21:23:48 by tlamit            #+#    #+#              #
#    Updated: 2025/11/21 16:30:55 by tlamit           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
from math import floor
import time
import subprocess
from cursor_utils import *

def add_files(path: str, files_list: list) -> None:
	for entry in os.scandir(path):
		if entry.is_dir():
			add_files(entry.path, files_list)
		if entry.is_file() and entry.name.endswith(".c"):
			files_list.append(entry.path)


def parceur(line: str, all_cfiles: list, cc_files: list, n: int) -> int:

	if ".c" in line:
		cc_files.append(line)
	if "cc -Wall -Wextra -Werror" in line:
		n += 1
		print(f"{CURSOR_TO(10, 0)}{ERASE_LINE_FULL}{line.strip()}", end="", flush=True)
		print(f"{CURSOR_TO(11, 0)}{ERASE_LINE_FULL}{n}/{len(all_cfiles)}", end="", flush=True)
		lentgh = 100
		progress_value = int((n / len(all_cfiles)) * lentgh)
		filled = "█" * progress_value
		empty = "-" * (lentgh - progress_value)
		print(f"{CURSOR_TO(12, 0)}{ERASE_LINE_FULL}>{filled}{empty}<")
		
	return n


def main():
	current_directory = os.getcwd()
	all_cfiles = []
	cc_files = []
	add_files(current_directory, all_cfiles)
	command = "make re && make clean"

	t_start = time.perf_counter()
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
		n = 0
		for line in process.stdout:
			n = parceur(line, all_cfiles, cc_files, n)
	process.stdout.close()

	_, stderr = process.communicate()
	print(f"Compiled in {round(time.perf_counter() - t_start, 3)} sec.")
	if stderr:
		print(f"\n{FG_BRIGHT_RED}--- STDERR ---")
		print(f"{FG_BRIGHT_RED}{stderr}", end='')
		return
	if (not process.returncode):
		print(FG_BRIGHT_GREEN, f"\nProcess finished with exit code {process.returncode}", FG_DEFAULT)
	newlist = []
	for i in cc_files:
		for x in all_cfiles:
			if i[i.rfind("/") + 1: -1] == x[x.rfind("/") + 1:]:
				newlist.append(x)
	if (len(set(all_cfiles) - set(newlist))):
		print(FG_RED, "Files not compiled or not included:")
		for file in set(all_cfiles) - set(newlist):
			print(FG_BRIGHT_RED ,file[len(current_directory):], FG_DEFAULT)
	
	n_process = subprocess.Popen(
		f"norminette {current_directory}",
		shell=True,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		text=True,
		cwd=current_directory,
		bufsize=1
	)
	if n_process.stdout:
		lines = [line for line in n_process.stdout if "Error" in line]
		if len(lines):
			for line in [line for line in n_process.stdout if "Error" in line]:
				if ("Error!" in line):
					print()
				print(line, end="")
		else:
			print(f"{FG_BRIGHT_GREEN}Norminette OK.")
	n_process.stdout.close()

	_, stderr = process.communicate()

if __name__ == "__main__":
	os.system("clear")
	print(FG_BRIGHT_CYAN, """
	       _                                       _           
	      | |  _                                  | |          
	 _   _| |_| |_  ____ _____         ____  _____| |  _ _____ 
	| | | | (_   _)/ ___|____ |       |    \(____ | |_/ ) ___ |
	| |_| | | | |_| |   / ___ |_______| | | / ___ |  _ (| ____|
	|____/ \_) \__)_|   \_____(_______)_|_|_\_____|_| \_)_____)
	""")
	main()
	print(FG_DEFAULT)
