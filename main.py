# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tlamit <titouan.lamit@gmail.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/20 21:23:48 by tlamit            #+#    #+#              #
#    Updated: 2025/11/20 22:30:31 by tlamit           ###   ########.fr        #
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

def main():
	current_directory = os.getcwd()
	print(current_directory)
	all_cfiles = []
	add_files(current_directory, all_cfiles)	
	result = subprocess.Popen(
		["make fclean", "make", "make clean"],
		cwd=current_directory,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		shell=True
	)
	print(result)

if __name__ == "__main__":
	os.system("clear")
	main()