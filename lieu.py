from pathlib import Path
from tinydb import TinyDB

class Lieu:
	BASE_DIR = Path(__file__.parent.resolve())
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
		# S'il n'existe pas le créer
		# S'il existe rentrer dans l'algo de sauvegarde:
			# insérer le dictionnaire des infos dépliées de l'instance de Lieu