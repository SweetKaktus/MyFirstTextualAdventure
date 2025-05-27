# Je vais me servir de cette classe pour mettre toute la logique de gameplay:
# - chargement des lieux en fonction des issues saisies par le joueur
# - affichage des items présents dans la scène
# - affichage des options disponibles (cf. Exemple_ui.txt)

import time
import sys
import os

from lieu import Lieu, get_all_lieux
from joueur import Joueur, get_all_joueurs
from menu import Menu

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

lieu_intro: Lieu 
joueur_dummy = ""

all_lieux = get_all_lieux() # Tous les objets lieux à manipuler pour la partie, il ne faudra jamais modifier les infos en base sous peine de casser le jeu, je ne dois manipuler que les objets dans all_lieux

for l in all_lieux:
	if l.titre == "intro":
		lieu_intro = l

for j in get_all_joueurs():
	if j.nom == "dummy":
		joueur_dummy = j


class Game:
	def __init__(self, lieu_actuel: Lieu=lieu_intro, joueur: Joueur=joueur_dummy, menu: Menu=Menu()):
		self.j: Joueur = joueur
		self.l_a: Lieu = lieu_actuel
		self.m: Menu = menu
		self.demarrer_jeu()

	def afficher_texte_lieu_actuel(self):
		for k, v in self.l_a.textes.items():
			for o in self.j.objets:
				if k == o:
					return v
		return self.l_a.textes["defaut"].capitalize()


	def demarrer_jeu(self):
		self.j = self.m.menu_principal()
		for l in all_lieux:
			if l.titre == self.j.lieu.lower():
				self.j.mettre_a_jour_le_lieu(nouveau_lieu=l.titre)
				self.l_a = l

		self.charger_scene()

		# print_letters_slowly(self.afficher_texte_lieu_actuel())
		# input('Appuyez sur "Entrée" pour continuer\n')
		# self.choisir_une_direction(direction="N") # PREVOIR DANS MON LIEU INTRO UNE ISSUE VERS L'AUBERGE POUR ASSURER LE BON DEMARRAGE DU JEU

	def choisir_une_direction(self, direction: str): # J'AI UN PB AVEC CETTE FONCTION, CELA NE CHOISIT PAS LA DIRECTION
		d = direction.lower()
		# print(d)
		if d in ["n", "s", "e", "o"]:
			for l in all_lieux:
				# print(l.titre)
				# print(self.l_a.issues[direction])
				if l.titre == self.l_a.issues[direction].lower():
					# print(self.l_a.issues[direction])
					return l
				else:
					print(f"Il n'y a pas de chemin vers {d.title()}")
					input()
					return

					# self.j.mettre_a_jour_le_lieu(nouveau_lieu=l.titre)
					# self.l_a = l
			# self.j.sauvegarder_joueur()
		else:
			print('La commande saisie est incorrecte. Appuyez sur "Entrée" pour continuer.')
			input()
			return

	def prendre_un_objet(self, objet):
		for o in self.l_a.objets:
			if o == objet:
				self.l_a.objets.remove(objet)
				self.j.objets.append(objet)
				input(f'Vous vous saisissez de "{objet}"')


	def charger_scene(self):
		choix = ""
		self.l_a.objets.sort()
		self.j.objets.sort()
		for o in self.j.objets:
			for ob in self.l_a.objets:
				if o == ob:
					self.l_a.objets.remove(o)
		clear()
		while not choix:
			compteur_objets = 0
			print(("-" * 20) + "\n")
			print(f"LIEU ACTUEL : {self.l_a.titre.title()}\n")
			print(("-" * 20) + "\n")

			print_letters_slowly(self.afficher_texte_lieu_actuel()+"\n")
			print(("-" * 20) + "\n")

			print("OBJETS PRESENTS DANS LE LIEU:\n")
			for i, o in enumerate(self.l_a.objets, start=1):
				print(f"[{i}] {o}")
				compteur_objets = i

			print("\nVOS POSSESSIONS:\n")
			for i, o in enumerate(self.j.objets, start=compteur_objets+1):
				print(f"[{i}] {o}")
			print()

			print(("-" * 20) + "\n")

			print("ISSUES POSSIBLES:\n")
			for k, v in self.l_a.issues.items():
				print(f"{k} : {v}")
			print(("-" * 20) + "\n")

			print("ACTIONS POSSIBLES:\n[1] PRENDRE UN OBJET\n[2] ALLER DANS UNE DIRECTION (N/S/E/O)\n[9] QUITTER LE JEU")
			choix = input("> ")
			match choix:
				case "1":
					print("PRENDRE UN OBJET\n")
					print("Veuillez indiquer l'objet à saisir (nombre affiché entre crochets) : ")
					o_index = input("> ")
					o_take = False
					for i, o in enumerate(self.l_a.objets, start=1):
						if str(i) == o_index:
							o_take = True
							self.prendre_un_objet(o)
							self.j.mettre_a_jour_les_objets(objets=self.j.objets)
					if not o_take:
						print(f"L'objet à l'index [{o_index}] n'existe pas.")
						input()

				case "2":
					print("ALLER DANS UNE DIRECTION\n")
					print("# Veuillez indiquer la direction à prendre (N/S/E/O): ")
					d = input("> ")
					new_lieu = self.choisir_une_direction(direction=d)
					if new_lieu:
						self.l_a = new_lieu
						self.j.mettre_a_jour_le_lieu(new_lieu.titre)

				case "9":
					self.j.mettre_a_jour_le_lieu(nouveau_lieu=self.j.lieu)
					self.j.mettre_a_jour_les_objets(objets=self.j.objets)
					print_letters_slowly("Votre progression a été sauvegardée...\n")
					print_letters_slowly("Merci d'avoir joué ! A bientôt !")
					input()
					clear()
					sys.exit()
					return

				case _:
					choix = ""
					print('La commande saisie est incorrecte. Appuyez sur "Entrée" pour continuer.')
					input()



if __name__ == "__main__":
	g = Game()
	while True:
		g.charger_scene()