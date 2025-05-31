import sys

from joueur import Joueur, get_all_joueurs
from functions_for_display import print_letters_slowly, clear, time_sleep_between_lines, print_letters_slowly_for_game_instructions
from joueur import Joueur, get_all_joueurs




class Menu:

	def __init__(self):
		pass

	def afficher_titre_du_jeu(self):
		print(("#" * 25)+"\n#"+(" " * 23)+"#\n#       L'HOMME         #\n#     AU BRAS D'OR      #\n#"+(" " * 23)+"#\n"+("#" * 25))


	def menu_principal(self):
		choix = ""

		while choix == "":
			all_joueurs = get_all_joueurs()
			clear()
			self.afficher_titre_du_jeu()
			print("1. Nouvelle Partie\n2. Charger Partie\n3. Supprimer Partie\n4. Règles\n5. Quitter")
			choix = input("Que souhaitez-vous faire ? (1/2/3/4/5)")
			match choix:
				case "1":
					nom_joueur = input("Veuillez saisir votre nom ou un pseudonyme :\n")
					j = Joueur(nom=nom_joueur, lieu="intro", objets=[])
					j.sauvegarder_joueur()
					return j
				case "2":
					j = self.selectionner_un_joueur(all_joueurs=all_joueurs)
					if not j:
						choix = ""
						print("Choix invalide.")
						input("Appuyez sur 'Entrée' pour continuer.\n")
					else:
						return j
						break
				case "3":
					j = self.selectionner_un_joueur(all_joueurs=all_joueurs)
					if not j:
						choix = ""
						print("Choix invalide.")
						input("Appuyez sur 'Entrée' pour continuer.\n")
					else:
						choix = ""
						print_letters_slowly_for_game_instructions(f"Suppression du joueur {j} ...")
						j.supprimer_joueur()
						time_sleep_between_lines()
						print_letters_slowly_for_game_instructions(f"Le joueur {j} a été supprimé ...")
						input("Appuyez sur 'Entrée' pour continuer.\n")

				case "4":
					choix = ""
					print_letters_slowly("\nBienvenue dans l'histoire de l'Homme au bras d'or.")
					print_letters_slowly("Dans ce jeu d'aventure textuelle, vous incarné le tenancier d'une auberge au beau milieu de la forêt noire en Allemagne.")
					print_letters_slowly("Ce jeu est un hommage à mon grand-père Jean qui se plaisait à nous effrayer avec cette histoire mes cousins et moi lorsque nous étions de jeunes enfants...")
					print_letters_slowly("Pour toi Papé qui m'a donné le goût des anciennes technologies et de l'ingéniosité mêlée aux arts créatifs.")
					print_letters_slowly("Merci, je t'aime.")
					print_letters_slowly(".\n" * 4)
					print_letters_slowly("Ce jeu a été développé en python dans le but de me faire travailler sur la programmation orientée objet dans le cadre de mon apprentissage au développement informatique en autodidacte.")
					print_letters_slowly("Vous pouvez trouver le code source de ce projet sur mon github: https://github.com/SweetKaktus/MyFirstTextualAdventure")
					print_letters_slowly("Créé par SweetKaktus en Juin 2025.\n")
					input("Appuyez sur 'Entrée' pour continuer.\n")

				case "5":
					print_letters_slowly_for_game_instructions("Merci d'avoir joué ! À bientôt !")
					input()
					clear()
					sys.exit()
				case _:
					print()
					choix = ""
					input("Je n'ai pas saisie votre demande.\n")

	def selectionner_un_joueur(self, all_joueurs):
		for i, j in enumerate(all_joueurs):
			print(f"{i}. {j}")
		print()
		joueur_selectionne = input("Veuillez sélectionner un joueur: ")
		for i, j in enumerate(all_joueurs):
			if str(i) == joueur_selectionne:
				return j
		return

	


if __name__ == "__main__":
	m = Menu()

	m.menu_principal()