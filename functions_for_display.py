import time
import sys
import os

time_between_lines = 0.5
time_between_letters = 0.05
time_between_letters_for_game_instructions = 0.02
time_between_letters_who_stole_golden_arm = 0.25


def time_sleep_between_lines():
	time.sleep(time_between_lines)

def print_letters_slowly(sentence: str):
	for character in sentence:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(time_between_letters)
	print()

def print_letters_slowly_for_game_instructions(sentence: str):
	for character in sentence:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(time_between_letters_for_game_instructions)
	print()


def print_letters_slowly_who_stole_golden_arm(sentence: str):
	for character in sentence:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(time_between_letters_who_stole_golden_arm)
	print()

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

if __name__ == "__main__":
	print_letters_slowly_who_stole_golden_arm("QUI A VOLÉ MON BRAS D'OR")