import time
import sys

time_between_lines = 2
time_between_letters = 0.05


def print_letters_slowly(sentence: str):
	for character in sentence:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(time_between_letters)
	print()


