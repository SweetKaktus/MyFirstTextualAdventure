# Je vais me servir de cette classe pour mettre toute la logique de gameplay:
# - chargement des lieux en fonction des issues saisies par le joueur
# - affichage des items présents dans la scène
# - affichage des options disponibles (cf. Exemple_ui.txt)

import time
import sys
import os

from lieu import Lieu, get_all_lieux
from joueur import Joueur, get_all_joueurs
from functions_for_display import time_sleep_between_lines, print_letters_slowly, clear, print_letters_slowly_for_game_instructions
from menu import Menu

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
		self.issues_disponibles = {}
		self.cle_objets = ""



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

	def charger_issues_disponibles(self):
		for obj in self.j.objets:
			if obj.lower() in self.l_a.issues.keys():
				self.issues_disponibles = self.l_a.issues[obj.lower()]
				return
		self.issues_disponibles = self.l_a.issues["defaut"]
		return

	def charger_cle_objets(self):
		for obj in self.j.objets:
			if obj.lower() in self.l_a.objets.keys():
				self.cle_objets = obj.lower()
				return
		self.cle_objets = "defaut"
		return

	def choisir_une_direction(self, direction: str): # J'AI UN PB AVEC CETTE FONCTION, CELA NE CHOISIT PAS LA DIRECTION
		d = direction.lower()
		# print(d)
		if d in ["n", "s", "e", "o"]:
			for l in all_lieux:
				# print(l.titre)
				# print(self.l_a.issues[direction])
				try:
					l.titre == self.issues_disponibles[d].lower()
					# print(self.l_a.issues[direction])
					print(f"Vous vous dirigez vers {self.issues_disponibles[d].capitalize()}")
					input()
					return l
				except KeyError:
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
		# print(self.objets_disponibles)
		# input()
		for o in self.l_a.objets[self.cle_objets]:
			# print(o)
			# input()
			# print(objet.lower())
			if o.lower() == objet.lower():
				# print("YAY")
				# input()
				self.l_a.objets[self.cle_objets].remove(objet.lower())
				self.j.objets.append(objet)
				print_letters_slowly_for_game_instructions(f'Vous vous saisissez de "{objet.capitalize()}"')
				input('Appuyez sur "Entrée" pour continuer.')


	def charger_scene(self):
		choix = ""
		self.charger_issues_disponibles()
		self.charger_cle_objets()
		self.l_a.objets[self.cle_objets].sort()
		self.j.objets.sort()
		for o in self.j.objets:
			for ob in self.l_a.objets[self.cle_objets]:
				if o == ob:
					self.l_a.objets[self.cle_objets].remove(o)
		self.charger_cle_objets()

		while not choix:
			clear()
			compteur_objets = 0
			print(("-" * 20) + "\n")
			print(f"LIEU ACTUEL : {self.l_a.titre.title()}\n")
			print(("-" * 20) + "\n")
			time_sleep_between_lines()
			print_letters_slowly(self.afficher_texte_lieu_actuel()+"\n")
			print(("-" * 20) + "\n")
			time_sleep_between_lines()
			print("OBJETS PRESENTS DANS LE LIEU:\n") # JE DOIS REFACTO MON AFFICHAGE D'OBJETS POUR PERMETTRE D'AFFICHER UNE LISTE SI 
			# UN OBJET DETERMINANT EST POSSÉDÉ PAR LE JOUEUR OU UNE AUTRE SI AUCUN OBJET DÉTERMINANT N'EST POSSÉDÉ PAR LE JOUEUR
			for i, o in enumerate(self.l_a.objets[self.cle_objets], start=1):
				print(f"[{i}] {o.capitalize()}")
				compteur_objets = i

			print("\nVOS POSSESSIONS:\n")
			for i, o in enumerate(self.j.objets, start=compteur_objets+1):
				print(f"[{i}] {o.capitalize()}")
			print()

			print(("-" * 20) + "\n")
			time_sleep_between_lines()
			print("ISSUES POSSIBLES:\n") # JE DOIS REFACTO MON AFFICHAGE D'ISSUES POUR PERMETTRE D'AFFICHER UNE LISTE SI 
			# UN OBJET DETERMINANT EST POSSÉDÉ PAR LE JOUEUR OU UNE AUTRE SI AUCUN OBJET DÉTERMINANT N'EST POSSÉDÉ PAR LE JOUEUR
			for k, v in self.issues_disponibles.items():
				print(f"{k.title()} : {v.title()}")
			print(("-" * 20) + "\n")
			time_sleep_between_lines()
			print("ACTIONS POSSIBLES:\n[1] PRENDRE UN OBJET\n[2] ALLER DANS UNE DIRECTION (N/S/E/O)\n[0] QUITTER LE JEU")
			choix = input("> ")
			match choix:
				case "1":
					print("PRENDRE UN OBJET\n")
					print("Veuillez indiquer l'objet à saisir (nombre affiché entre crochets) : ")
					o_index = input("> ")
					o_take = False
					for i, o in enumerate(self.l_a.objets[self.cle_objets], start=1):
						if str(i) == o_index:
							o_take = True
							self.prendre_un_objet(o)
							self.j.mettre_a_jour_les_objets(objets=self.j.objets)
					if not o_take:
						print(f"L'objet à l'index [{o_index}] n'existe pas.")
						input()

				case "2":
					print("ALLER DANS UNE DIRECTION\n")
					print("Veuillez indiquer la direction à prendre (N/S/E/O): ")
					d = input("> ")
					new_lieu = self.choisir_une_direction(direction=d)
					if new_lieu:
						self.l_a = new_lieu
						self.j.mettre_a_jour_le_lieu(new_lieu.titre)

				case "0":
					self.j.mettre_a_jour_le_lieu(nouveau_lieu=self.j.lieu)
					self.j.mettre_a_jour_les_objets(objets=self.j.objets)
					print_letters_slowly_for_game_instructions("Votre progression a été sauvegardée...\n")
					print_letters_slowly_for_game_instructions("Merci d'avoir joué ! A bientôt !")
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