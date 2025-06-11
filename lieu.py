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

	def __init__(self, titre: str, textes: dict, objets: dict, issues: dict):
		self.titre: str = titre.lower()
		self.textes: dict = textes
		self.objets: dict = objets
		self.issues: dict = issues
		# for o in self.objets:
		# 		o = o.lower()
		for k in self.objets.keys():
			k = k.lower()
			for ke in self.objets[k]:
				ke = ke.lower()

		for k in self.issues.keys():
			k = k.lower()
			for ke, i in self.issues[k].items():
				ke = ke.lower()
				i = i.lower()
		for k, v in self.textes.items():
			k = k.lower()
			v = v.lower()

	def __repr__(self):
		return f"Lieu(titre={self.titre.title()})"


	def sauvegarder_lieu(self):
		# Je vérifie si le lieu existe
		# S'il nexiste pas je sauvegarde le lieu dans ma TinyDB et retourne sa clé, dans le cas contraire je retourne -1
		if not self.DB.search(self.QUERY_LIEU.titre==self.titre):
			return self.DB.insert(self.__dict__)
		else: return -1


	def supprimer_lieu(self):
		# Je vérifie si le lieu existe
		# S'il existe je supprime le lieu de ma TinyDB et je retourne sa clé dans une liste, dans le cas contraire je retourne [-1]
		if self.DB.search(self.QUERY_LIEU.titre==self.titre):
			return self.DB.remove(self.QUERY_LIEU.titre==self.titre)
		else: return [-1]

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
	titre = 'introduction', 
	textes = {
		"defaut" : "Vous êtes le gérant d'une auberge en plein milieu de la forêt noire,\nproche de Munich en Allemagne. Il y a peu de passage et les temps sont\ndurs. Vous ne savez par quel moyen vous subviendrez à vos besoins durant\nl'hiver prochain...\n\nNous sommes en 1956, et vous avez ouïe dire qu'un américain du nom de William H. Carter,\nvétéran de la Seconde Guerre Mondiale était passé il y a peu.\nCe vétéran se distinguait facilement, car il avait perdu son bras à\ncause d'un tir d'obus sur le front, après quoi il a été rapatrié aux\nÉtats-Unis.\n\nQuelques temps après, il héritait d'une grande fortune, et décida par\nce biais de remplacer son bras. Il aurait à la place bras en or massif.\nIl demanda les meilleurs médecins pour s'occuper de son cas.\nAlors ces derniers se mirent sur le coup afin de lui greffer un bras en or.\n\nCet homme, l'homme au bras d'or était donc de passage pour\nse rendre à Munich. Il avait pu venir à bord de sa belle voiture, une\ncadillac rouge décapotable. Tandis qu'il parcourait ces longues routes\ndésertes tout en faisant rugir son moteur, si vite dans une forêt si sombre\nqu'elle ne laissait passer aucun rayon du Soleil, il ne vit\nmalheureusement pas ce virage... un virage en tete d'epingle...\n\n*BOOM* *CRACK* *VLAN*\n\nIl succomba à ses blessures dans un accident tragique.\n\nCe genre d'accident se produisaient si souvent au niveau de ce virage,\nqu'un cimetière avait finit par être construit non loin.\nC'est là-bas qu'on l'y avait enterre... avec son bras en or.\n\nUne idée vous traverse alors l'esprit... \"ce bras en or\nne manquera à personne après tout, et si je ne trouve pas une solution,\nje finirai comme lui avant le prochain printemps.\"\n\nC'est decidez, vous irez chercher ce bras en or quoi qu'il\nen coûte.\n\nVous devez preparer d'abord vos affaires...\n\nVous devez prendre votre clé pour sortir de l'auberge ainsi que\nde quoi creuser pour parvenir a recuperer le bras.",
	}, 
	objets = {
		"defaut" : [],
	}, 
	issues = {
		"defaut" : {
			"n" : "auberge",
		},
	}
)
	l.sauvegarder_lieu()