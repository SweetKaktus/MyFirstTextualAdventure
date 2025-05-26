import pytest
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

from joueur import Joueur, get_all_joueurs
from lieu import Lieu




@pytest.fixture
def lieu_setup_db():
	Lieu.DB = TinyDB(storage=MemoryStorage)


@pytest.fixture
def lieu(lieu_setup_db):
	l = Lieu(
			titre="Camping", 
			textes={"default": "Vous êtes au camping municipal de la Motte Chalancon"},
			objets=["Mot de passe pour la Wifi", "Coupon pour les entrées à la piscine"], 
			issues={"N": "Village", "S": "Montagne", "E": "Piscine"}
		)
	l.sauvegarder_lieu()
	return l

@pytest.fixture
def joueur_setup_db():
	Joueur.DB = TinyDB(storage=MemoryStorage)


@pytest.fixture
def joueur(joueur_setup_db):
	j = Joueur(nom="Jeannot", lieu="Camping", objets=["Sandales ouvertes", "Boomerang"])
	j.sauvegarder_joueur()
	return j

def test_sauvegarder_joueur(joueur_setup_db):
	j = Joueur(nom="Nathan", lieu="Piscine", objets=["Maillot de bain", "Serviette"])

	assert j.sauvegarder_joueur() == 1

def test_sauvegarder_joueur_dup(joueur):

	assert joueur.sauvegarder_joueur() == -1

def test_supprimer_joueur(joueur):
	assert joueur.supprimer_joueur() == [1]

def test_supprimer_joueur_dup(joueur):
	joueur.supprimer_joueur()
	assert joueur.supprimer_joueur() == [-1]

def test_prendre_objet(joueur, lieu):
	joueur_query = Query()
	assert joueur.prendre_objet("Mot de passe pour la Wifi") == "Vous avez pris l'objet : Mot de passe pour la Wifi."
	assert joueur.objets == ["Sandales ouvertes", "Boomerang", "Mot de passe pour la Wifi"]
	# assert Joueur.DB.search((joueur.QUERY_JOUEUR.name == "Jeannot")) == [{'nom': 'Jeannot', 'lieu': 'Camping', 'objets': ['Sandales ouvertes', 'Boomerang', 'Mot de passe pour la Wifi']}]
	# Je dois faire en sorte de vérifier si en BDD les objets sont bien ajoutés comme il faut. assert joueur.DB.search(Query().nom==joueur.nom)

def test_pas_prendre_objet(joueur, lieu):
	assert joueur.prendre_objet(" pour la Wifi") == "L'objet indiqué n'existe pas."

def test_prendre_objet_lieu_nok(joueur, lieu_setup_db):
	assert joueur.prendre_objet("Mot de passe pour la Wifi") == "Vous n'êtes pas dans un lieu connu"

def test_mettre_a_jour_le_lieu(joueur):
	assert joueur.mettre_a_jour_le_lieu("Plage") == [1]