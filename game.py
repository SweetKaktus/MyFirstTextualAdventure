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

lieu_intro = ""
joueur_dummy = ""

all_lieux = get_all_lieux() # Tous les objets lieux à manipuler pour la partie, il ne faudra jamais modifier les infos en base sous peine de casser le jeu, je ne dois manipuler que les objets dans all_lieux

for l in get_all_lieux():
	if l.titre == "intro":
		lieu_intro = l

for j in get_all_joueurs():
	if j.nom == "dummy":
		joueur_dummy = j


class Game:
	def __init__(self, joueur: Joueur=joueur_dummy, lieu_actuel: Lieu=lieu_intro, menu: Menu=Menu()):
		self.j = joueur
		self.l_a = lieu_actuel
		self.m = menu
		self.demarrer_jeu()

	def afficher_texte_lieu_actuel(self):
		for k, v in self.l_a.textes.items():
			for o in self.j.objets:
				if k == o:
					return v
		return self.l_a.textes["defaut"]


	def demarrer_jeu(self):
		self.j = self.m.menu_principal()
		print_letters_slowly(self.afficher_texte_lieu_actuel())
		input('Appuyez sur "Entrée" pour continuer\n')
		self.choisir_une_direction("N") # PREVOIR DANS MON LIEU INTRO UNE ISSUE VERS L'AUBERGE POUR ASSURER LE BON DEMARRAGE DU JEU

	def choisir_une_direction(self, direction: str):
		d = direction.lower()
		if d in ["n", "s", "e", "o"]:
			self.j.lieu = self.l_a.issues[direction]
			self.l_a = self.j.lieu
			self.j.sauvegarder_joueur()
		else:
			print('La commande saisie est incorrecte. Appuyez sur "Entrée" pour continuer.')
			input()

	def prendre_un_objet(self, objet):
		if objet in self.l_a.objets:
			self.l_a.objets.remove(objet)
			self.j.objets.append(objet)
			input(f'Vous vous saisissez de "{objet}"')


	def charger_scene(self):
		choix = ""
		while not choix:
			compteur_objets = 0
			print(f"LIEU ACTUEL : {self.l_a.titre}\n")
			print("-" * 20)
			print_letters_slowly(self.afficher_texte_lieu_actuel()+"\n")
			print("-" * 20)
			print("OBJETS PRESENTS DANS LE LIEU:\n")
			for i, o in enumerate(self.l_a.objets, start=1):
				print(f"[{i}] {o}")
				compteur_objets = i
			print("VOS POSSESSIONS:\n")
			for i, o in enumerate(self.j.objets, start=compteur_objets+1):
				print(f"[{i}] {o}")
			print()
			print("-" * 20)
			choix = input("ACTIONS POSSIBLES:\n[1] PRENDRE UN OBJET\n[2] ALLER DANS UNE DIRECTION (N/S/E/O)\n[9] QUITTER LE JEU")
			match choix:
				case "1":
					print("PRENDRE UN OBJET\n")
					o = input("Veuillez indiquer l'objet à saisir (nombre affiché entre crochets) : ")
					self.prendre_un_objet(o)
					
				case "2":
					print("ALLER DANS UNE DIRECTION\n")
					d = input("Veuillez indiquer la direction à prendre (N/S/E/O): ")
					self.choisir_une_direction(direction=d)

				case "9":
					self.j.sauvegarder_joueur()
					print_letters_slowly("Votre progression a été sauvegardée...\n")
					print_letters_slowly("Merci d'avoir joué ! A bientôt !")
					input()
					sys.exit()
					return

				case _:
					choix = ""
					print('La commande saisie est incorrecte. Appuyez sur "Entrée" pour continuer.')
					input()



if __name__ == "__main__":
	g = Game()
	g.demarrer_jeu()
	while true:
		g.charger_scene()