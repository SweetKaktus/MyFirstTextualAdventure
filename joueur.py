from pathlib import Path
from tinydb import TinyDB, Query
from lieu import Lieu, get_all_lieux


# Classe Joueur, elle contient un nom de joueur, un lien tinydb vers un
# fichier de sauvegarde, une liste d'item, un lieu associé, une liste d'action ?

# note pour plus tard => A partir de tinydb penser à un système de sauvegarde de plusieurs parties à même la db

# Pour associer un lieu je pense mettre simplement le nom du lieu et l'appli réconciliera cette donnée avec le Titre du lieu dans la tinydb des lieux
# pour charger la carte, et de toute façon les descriptions des lieux seront sensiblements les mêmes, 
# modulo la possession d'items qui font progresser l'histoire et donc qui charge une autre description du lieu



class Joueur:
	BASE_DIR = Path(__file__).parent.resolve()
	DB = TinyDB(BASE_DIR / "datas" / "joueur.json")
	QUERY_JOUEUR = Query()

	def __init__(self, nom: str, lieu: str, objets: list):
		self.nom = nom
		self.lieu = lieu
		self.objets = objets
		for o in self.objets:
			o = o.lower()


	def __str__(self):
		return self.nom

	def __repr__(self):
		return f"Joueur(nom={self.nom}, lieu={self.lieu})"

	def sauvegarder_joueur(self):
		if not self.DB.search(self.QUERY_JOUEUR.nom==self.nom):
			return self.DB.insert(self.__dict__)
		else: return -1

	def supprimer_joueur(self):
		if self.DB.search(self.QUERY_JOUEUR.nom==self.nom):
			return self.DB.remove(self.QUERY_JOUEUR.nom==self.nom)
		else: return [-1]

	def prendre_objet(self, objet: str):
		lieu_actuel = None
		for lieu in get_all_lieux():
			if lieu.titre == self.lieu:
				lieu_actuel = lieu

		if lieu_actuel:
			for o in lieu_actuel.objets:
				if o == objet:
					self.objets.append(o.lower())
					return f"Vous avez pris l'objet : {o.title()}."
			return "L'objet indiqué n'existe pas."
		else:
			return "Vous n'êtes pas dans un lieu connu"

	def mettre_a_jour_le_lieu(self, nouveau_lieu: str):
		self.lieu = nouveau_lieu
		return self.DB.update({"lieu" : nouveau_lieu}, self.QUERY_JOUEUR.nom==self.nom)

	def mettre_a_jour_les_objets(self, objets: str):
		self.objets = objets
		return self.DB.update({"objets": objets}, self.QUERY_JOUEUR.nom==self.nom)

def get_all_joueurs():
	all_joueurs = [Joueur(nom=j["nom"], lieu=j["lieu"], objets=j["objets"]) for j in Joueur.DB.all()]

	# for j in Joueur.DB.all():
	# 	joueur = Joueur(nom=j["nom"], lieu=j["lieu"], objets=j["objets"])
	# 	all_joueurs.append(joueur)

	return all_joueurs


if __name__ == "__main__":
	j = Joueur(nom="Nathan", lieu="Piscine", objets=["Maillot de bain", "Serviette"])
	j.sauvegarder_joueur()
	print(Joueur.DB.search(Joueur.QUERY_JOUEUR.nom == "Jeannot"))