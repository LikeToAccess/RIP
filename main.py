# -*- coding: utf-8 -*-
# filename          : main.py
# description       : Download and convert Instagram posts from an account
# author            : Ian Ault
# email             : liketoaccess@protonmail.com
# date              : 04-27-2022
# version           : v1.0
# usage             : python main.py profile [profile ...]
# notes             :
# license           : MIT
# py version        : 3.10.2 (must run on 3.6 or higher)
#==============================================================================
import platform
import sys
import os


OS = platform.system()
profiles = sys.argv[1:]


def main():
	if OS == "Windows":
		ffmpeg_binary = "ffmpeg.exe"
	else: # Works for MacOS and Linux
		ffmpeg_binary = "./ffmpeg"

	for profile in profiles:
		print(profile)
		os.system(f"instaloader --fast-update {profile}")




if __name__ == "__main__":
	main()
