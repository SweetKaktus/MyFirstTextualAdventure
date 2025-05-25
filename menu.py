import sys

from joueur import Joueur, get_all_joueurs
from main import clear, print_letters_slowly
from joueur import Joueur





class Menu:

	def __init__(self):
		pass

	def afficher_titre_du_jeu(self):
		print(("#" * 25)+"\n#"+(" " * 23)+"#\n#       L'HOMME         #\n#     AU BRAS D'OR      #\n#"+(" " * 23)+"#\n"+("#" * 25))


	def menu_principal(self):
		choix = ""

		while choix == "":
			clear()
			self.afficher_titre_du_jeu()
			print("1. Nouvelle Partie\n2. Charger Partie\n3. Règles\n4. Quitter")
			choix = input("Que souhaitez-vous faire ? (1/2/3/4)")
			match choix:
				case "1":
					nom_joueur = input("Veuillez saisir votre nom ou un pseudonyme :\n")
					j = Joueur(nom="", lieu="intro", objets=[])
					j.sauvegarder_joueur()
					demarrer_jeu(j)
				case "2":
					pass
				case "3":
					choix = ""
					print_letters_slowly("\nBienvenue dans l'histoire de l'Homme au bras d'or.")
					print_letters_slowly("Dans ce jeu d'aventure textuelle, vous incarné le tenancier d'une auberge au beau milieu de la forêt noire en Allemagne.")
					print_letters_slowly("Ce jeu est un hommage à mon grand-père Jean qui se plaisait à nous effrayer avec cette histoire mes cousins et moi lorsque nous étions de jeunes enfants...")
					print_letters_slowly("Pour toi Papé qui m'a donné le goût des anciennes technologies et de l'ingéniosité mêlée aux arts créatifs.")
					print_letters_slowly("Merci, je t'aime.")
					print_letters_slowly(".\n" * 4)
					print_letters_slowly("Ce jeu a été développé en python dans le but de travailler sur la programmation orientée objet dans le cadre de mon apprentissage au développement informatique en autodidacte.")
					print_letters_slowly("Vous pouvez trouver le code source de ce projet sur mon github: https://github.com/SweetKaktus/MyFirstTextualAdventure")
					print_letters_slowly("Créé par SweetKaktus en Juin 2025.\n")
					input("Appuyez sur 'Entrée' pour continuer.\n")

				case "4":
					print_letters_slowly("Merci d'avoir joué ! À bientôt !")
					input()
					clear()
				case _:
					print()
					choix = ""
					input("Je n'ai pas saisie votre demande.\n")

if __name__ == "__main__":
	m = Menu()

	m.menu_principal()