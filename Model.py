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


class Ronde:
    pass


class State:
    def __init__(self):
        self.joueurs = []
        self.nombre_joueurs = 0
        self.tournoi = None

    def creer_nouveau_tournoi(self, nouveau_tounoi :Tournoi):
        self.tournoi = Tournoi(nouveau_tounoi)
        print('Nouveau Tournoi créé avec succès !')
        print(nouveau_tounoi)
        print(type(self.tournoi))

    def ajouter_joueurs(self, joueurs: List[Joueur]):
        self.joueurs = joueurs
        self.nombre_joueurs = len(joueurs)


if __name__ == '__main__':
    nouveau_sexe = ControleDuTemps.BULLET
    print(nouveau_sexe.value)
    print(type(nouveau_sexe.value))
