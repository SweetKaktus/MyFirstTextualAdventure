# MyFirstTextualAdventure - L'Homme au bras d'Or

![QA Testing](https://img.shields.io/badge/status-Tests%20In%20Porgress-orange.svg)
![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Licence CC0-1.0](https://img.shields.io/badge/licenses-License_CC0_1.0-white.svg)

Jeu d'aventure textuel développé en Python, conçu pour mettre en pratique la programmation orientée objet, les structures de données et la logique de navigation dans un univers narratif.

---

## 🎮 Concept

Un jeu entièrement en ligne de commande, où le joueur incarne un héros explorant différents lieux, interagissant avec des objets et prenant des décisions.

Fonctionnalités actuelles :
- Déplacement dans un monde divisé en pièces
- Gestion d’un inventaire
- Objets à ramasser
- Architecture modulaire en POO

---

## 💡 Objectifs pédagogiques

Ce projet est un support d’apprentissage personnel pour :
- Structurer un jeu via des classes et modules
- Gérer des états de jeu (scènes, inventaire, interactions)
- Implémenter une boucle de jeu efficace
- Renforcer la lisibilité et la réutilisabilité du code

---

## 📜 Licence

Ce projet est sous licence CC0 1.0 Universal.

---

## 🔗 Auteur

**SweetKaktus**  
📎 [Mon GitHub](https://github.com/SweetKaktus)
🧑‍💻 [Mon profil Malt](https://www.malt.fr/profile/nathanpinto1)

---

## Lancer le jeu

- Télécharger et installer Python 3.12 via le lien suivant: https://www.python.org/downloads/release/python-31211/

- Cloner le repo Github dans le dossier de votre choix :
```shell
git clone https://github.com/SweetKaktus/MyFirstTextualAdventure.git
```

- Supprimez le dossier ./.env/

- Dans le dossier MyFirstTextualAdventure tapez les commandes suivantes:

	Windows:
```shell
python -m venv .env
./.env/Scripts/activate.bat
pip -r requirements.txt
python game.py
```

	Unix / MacOS:
```shell
python -m venv .env
source ./.env/bin/activate
pip -r requirements.txt
python game.py
```

---