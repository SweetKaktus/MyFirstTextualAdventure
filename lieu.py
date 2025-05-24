from pathlib import Path
from tinydb import TinyDB, Query

# La classe lieu contient une liste de texte, le lieu peu en avoir un ou plusieurs, s'il en a plusieurs, le choix du
# texte affiché doit se faire en fonction des items possédés par l'objet Joueur en cours de partie.

class Lieu:
	"""
	Ceci est ma classe Lieu, elle me permet de gérer mes lieux, c'est par ce biais que je charge mes
	scenes et que j'affiche les descriptions, les objets à récupérer, les directions à prendre.

	Un Lieu contient les attributs suivants: titre: str, textes: list, objets: list, issues: list.

	Un lieu contient des méthodes pour récupérer chaque attribut, mais aussi pour sauvegarder ses données dans un json
	grâce au module TinyDB (qui se situe à l'emplacement /datas/lieux.json), également une méthode 
	pour retirer un lieu de la TinyDB, et une dernière pour retirer un objet de la scène
	"""

	BASE_DIR = Path(__file__).parent.resolve()
	DB = TinyDB(BASE_DIR / 'datas' / 'lieux.json')
	QUERY_LIEU = Query()

	def __init__(self, titre: str, textes: dict, objets: list, issues: dict):
		self.titre = titre
		self.textes = textes
		self.objets = objets
		self.issues = issues

	def __repr__(self):
		return f"Lieu(titre={self.titre})"


	def sauvegarder_lieu(self):
		# Vérifier si le fichier DB existe
		# S'il n'existe pas le créer
		# S'il existe rentrer dans l'algo de sauvegarde:
			# insérer le dictionnaire des infos dépliées de l'instance de Lieu
		test_path = self.BASE_DIR / 'datas' / 'lieux.json'
		try:
			path_parent = test_path.parent.resolve()
			path_parent.mkdir()
		except FileExistsError:
			print("Le dossier existe, action Path().mkdir() ignorée") # /!\ A CONVERTIR EN DEBUG /!\
		try:
			test_path.touch()
		except FileExistsError:
			print("Le fichier existe, action Path().touch() ignoréé.") # /!\ A CONVERTIR EN DEBUG /!\
		self.DB.insert(self.__dict__)


	def supprimer_lieu(self):
		ma_query = Query()
		self.DB.remove(ma_query.search(titre=self.titre))

	def retirer_objet_du_lieu(self, objet: str) -> None:
		for o in self.objets:
			if o == objet:
				self.objets.remove(o)


def get_all_lieux() -> list:
	all_lieux_dict = Lieu.DB.all()
	all_lieux = []
	for lieu in all_lieux_dict:
		all_lieux.append(Lieu(titre=lieu["titre"], textes=lieu["textes"], objets=lieu["objets"], issues=lieu["issues"]))
	return all_lieux



if __name__ == "__main__":
	l = Lieu(
			titre="Camping", 
			textes={"default": "Vous êtes au camping municipal de la Motte Chalancon"},
			objets=["Mot de passe pour la Wifi", "Coupon pour les entrées à la piscine"], 
			issues={"N": "Village", "S": "Montagne", "E": "Piscine"}
		)
	l.sauvegarder_lieu()

	test = get_all_lieux()
	print(test)