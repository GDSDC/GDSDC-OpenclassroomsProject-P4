from typing import Any, Dict, List
from dataclasses import dataclass
from enum import Enum
from datetime import date

# INITIALISATION CONSTANTES
# nombres de tours (Round) par tournoi
NOMBRE_DE_TOURS = 4

# nombre de joueurs par tournoi
NOMBRE_DE_JOUEURS = 8


# Classes Enum
class Sex(Enum):
    """Classe Enum du sexe"""
    MALE = 'm'
    FEMALE = 'f'


class ControleDuTemps(Enum):
    """Classe Enum du Contrôle du temps"""
    BULLET = 'bullet'
    BLITZ = 'blitz'
    COUP_RAPIDE = 'coup rapide'


@dataclass
class Joueur:
    """Classe décrivant un Joueur"""
    nom_de_famille: str
    prenom: str
    date_de_naissance: date
    sexe: Sex
    classement: int


@dataclass
class Tournoi:
    """Classe décrivant un Tournoi"""
    nom: str
    lieu: str
    date_debut: date
    date_fin: date
    controle_du_temps: ControleDuTemps
    description: str
    nombre_tours: int = NOMBRE_DE_TOURS

class Match:
    pass


class Round:
    pass


class State:
    def __init__(self):
        self.joueurs = []
        self.nombre_joueurs = 0
        self.tournoi = None
        self.paires_joueurs = []

    def creer_nouveau_tournoi(self, nouveau_tournoi :Tournoi):
        self.tournoi = nouveau_tournoi
        print('Nouveau Tournoi créé avec succès !')


    def ajouter_joueurs(self, joueurs: List[Joueur]):
        self.joueurs = joueurs
        self.nombre_joueurs = len(joueurs)
        print('Nouveaux Joueurs créés avec succès !')

    def generer_paires_joueurs(self, joueurs: List[Joueur]):
        self.paires_joueurs = []
        i = 0
        while i < len(joueurs):
            self.paires_joueurs.append((joueurs[i], joueurs[i+1]))
            i += 2





if __name__ == '__main__':

    liste_joueurs_test = [Joueur(nom_de_famille='Da Costa', prenom='Gabriel', date_de_naissance=date(1990, 6, 27), sexe=Sex.MALE, classement=56), Joueur(nom_de_famille='Rainaud', prenom='Lucie', date_de_naissance=date(1989, 10, 27), sexe=Sex.FEMALE, classement=9)]
    test = State()
    test.ajouter_joueurs(liste_joueurs_test)
    test.generer_paires_joueurs(test.joueurs)
    print(test.paires_joueurs)