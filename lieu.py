from pathlib import Path
from tinydb import TinyDB

class Lieu:
	BASE_DIR = Path(__file__).parent.resolve()
	DB = TinyDB(BASE_DIR / 'datas' / 'lieux.json')

	def __init__(self, titre: str, texte: str, objets: list, issues: list):
		self.titre = titre
		self.texte = texte
		self.objets = objets
		self.issues = issues

	def charger_texte(self) -> str:
		return self.texte

	def charger_titre(self) -> str:
		return self.titre

	def charger_objets(self) -> str:
		return self.objets

	def charger_issues(self) -> str:
		return self.issues

	def sauvegarder_lieu(self) -> str:
		# Vérifier si le fichier DB existe
		test_path = BASE_DIR / 'datas' / 'lieux.json'
		try:
			path_parent = test_path.parent.resolve()
			path_parent.mkdir()
		except FileExistError:
			print("Le dossier existe, action Path().mkdir() ignorée") # /!\ A CONVERTIR EN DEBUG /!\
		try:
			test_path.touch()
		except FileExistError:
			print("Le fichier existe, action Path().touch() ignoréé.") # /!\ A CONVERTIR EN DEBUG /!\
		DB.insert(self.__dict__)
		# S'il n'existe pas le créer
		# S'il existe rentrer dans l'algo de sauvegarde:
			# insérer le dictionnaire des infos dépliées de l'instance de Lieu

		pass

	def retirer_objet_du_lieu(self, objet: str) -> None:
		for o in self.objets:
			if o == objet:
				self.objets.remove(o)