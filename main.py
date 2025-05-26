import time
import sys
import os


time_between_lines = 2
time_between_letters = 0.05






def print_letters_slowly(sentence: str):
	for character in sentence:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(time_between_letters)
	print()

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

