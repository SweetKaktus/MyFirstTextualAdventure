# Je vais me servir de cette classe pour mettre toute la logique de gameplay:
# - chargement des lieux en fonction des issues saisies par le joueur
# - affichage des items présents dans la scène
# - affichage des options disponibles (cf. Exemple_ui.txt)

from lieu import Lieu, get_all_lieux
from joueur import Joueur, get_all_joueurs


class Game:
	def __init__(self, joueur, lieu_actuel):
		self.joueur = joueur
		self.lieu_actuel = lieu_actuel

	def afficher_texte_lieu_actuel(self):
		print(lieu_actuel.texte)

	def afficher_titre_du_jeu(self):
		print(("#" * 25)+"\n#"+(" " * 23)+"#\n#       L'HOMME         #\n#     AU BRAS D'OR      #\n#"+(" " * 23)+"#\n"+("#" * 25))

	

if __name__ == "__main__":
	g = Game(joueur="test", lieu_actuel="test")
	g.afficher_titre_du_jeu()