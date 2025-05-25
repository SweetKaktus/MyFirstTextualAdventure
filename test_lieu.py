import pytest
from tinydb import TinyDB
from tinydb.storages import MemoryStorage

from lieu import Lieu
from joueur import Joueur



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


def test_sauvegarder_lieu(lieu_setup_db):
	l = Lieu(
			titre="Camping", 
			textes={"default": "Vous êtes au camping municipal de la Motte Chalancon"},
			objets=["Mot de passe pour la Wifi", "Coupon pour les entrées à la piscine"], 
			issues={"N": "Village", "S": "Montagne", "E": "Piscine"}
		)
	assert l.sauvegarder_lieu() == 1

def test_sauvegarder_lieu_dup(lieu):
	assert lieu.sauvegarder_lieu() == -1

def test_supprimer_lieu(lieu):
	assert lieu.supprimer_lieu() == [1]

def test_supprimer_lieu_existe_pas(lieu_setup_db):
	l = Lieu(
			titre="Camping", 
			textes={"default": "Vous êtes au camping municipal de la Motte Chalancon"},
			objets=["Mot de passe pour la Wifi", "Coupon pour les entrées à la piscine"], 
			issues={"N": "Village", "S": "Montagne", "E": "Piscine"}
		)
	assert l.supprimer_lieu() == [-1]
