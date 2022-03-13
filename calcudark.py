
import os, sys


def clearscreen():
	if sys.platform == "linux2":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()
	
__banner__ = """\033[1;36m
─█▀▀█─█▀▀█─█────█▀▀█─█──█─█────█▀▀█─▀▀█▀▀─█▀▀▀█─█▀▀█          
─█────█▄▄█─█────█────█──█─█────█▄▄█───█───█───█─█▄▄▀          
─█▄▄█─█──█─█▄▄█─█▄▄█─▀▄▄▀─█▄▄█─█──█───█───█▄▄▄█─█──█             
 
"""
__text__ = """\t\033[1;32mcreator @darknet_off1cial\n\tmy channel: @termux_uz_private\n\t***************************************"""
__color__ = """\033[1;35m"""
clearscreen()
os.system("termux-open-url https://t.me/darknet_off1cial")
print(__banner__)
print(__text__)
print(__color__)

while True: print(eval(input('matematik misolni yozing:')))