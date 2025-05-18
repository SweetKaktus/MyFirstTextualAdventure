import time
import sys

time_between_lines = 2
time_between_letters = 0.06


def main_loop():
	run : bool = True
	choix_start = ''
	while run:
		title = [
			'',
			'',
			'#' * 24,
			'#                      #',
			"#      L'envolée       #",
			'#                      #',
			'#' * 24,
			'',
			''
			]
		for element in title:
			print(element)
		while choix_start == '':
			main_menu = [
					'1. NOUVELLE PARTIE',
					'2. CHARGER UNE PARTIE',
					'3. RÈGLES',
					'4. QUITTER',
					''
			]
			for element in main_menu:
				print(element)
			choix = input('Que voulez-vous faire ? (1/2/3/4)\n')
			print()
			match choix:
				case '1':
					start_scene_1()
					return
				case '2':
					pass
				case '3':
					rule_s1 = "Hello ! Moi c'est SweetKaktus ! Bienvenu dans mon premier jeu d'aventure textuel !"
					rule_s2 = "Tu vas devoir faire des choix afin de progresser dans l'aventure que je te propose !"
					print_letters_slowly(rule_s1)
					print_letters_slowly(rule_s2)
					input("")
					choix = ''
				case '4':
					print_letters_slowly("Merci d'avoir jouer !")
					print_letters_slowly("À bientôt !")
					input("")
					return
				case _:
					print_letters_slowly("Votre choix est incorrect, veuillez réessayer.")
					choix = ''

		return

def print_letters_slowly(sentence: str):
	for character in sentence:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(time_between_letters)
	print()

def start_scene_1():
	print('#' * 24)
	print('#                      #')
	print('#      Chapitre 1      #')
	print('#                      #')
	print('#' * 24)
	print()
	input('')


	return

if __name__ == '__main__':
	main_loop()