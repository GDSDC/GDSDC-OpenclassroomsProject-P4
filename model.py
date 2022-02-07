from typing import Any, Dict, List
from dataclasses import dataclass
from enum import Enum
from datetime import date

# INITIALISATION CONSTANTES
# nombres de tours (Round) par tournoi
NOMBRE_DE_TOURS = 4

# nombre de joueurs par tournoi
NOMBRE_DE_JOUEURS = 8


# Classe décrivant le Joueur
class Sex(Enum):
    """Classe Enum du sexe"""
    MALE = 'm'
    FEMALE = 'f'


@dataclass
class Joueur:
    """Classe décrivant un Joueur"""
    nom_de_famille: str
    prenom: str
    date_de_naissance: date
    sexe: Sex
    classement: int


# Classe décrivant le Tournoi
class ControleDuTemps(Enum):
    """Classe Enum du Contrôle du temps"""
    BULLET = 'bullet'
    BLITZ = 'blitz'
    COUP_RAPIDE = 'coup rapide'


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


# Classe décrivant le Match
class Score(Enum):
    """Classe Enum du système de points"""
    GAGNANT = 1
    PERDANT = 0
    MATCH_NUL = 1/2


@dataclass
class Resultat:
    joueur: Joueur
    resultat: Resultat


@dataclass
class Match:
    resultat_1: Resultat
    resultat_2: Resultat


# Classes décrivant le Round
class Round:
    pass


class State:
    def __init__(self):
        self.joueurs = []
        self.nombre_joueurs = 0
        self.tournoi = None
        self.paires_joueurs = []

    def creer_nouveau_tournoi(self, nouveau_tournoi: Tournoi):
        self.tournoi = nouveau_tournoi

    def ajouter_joueurs(self, joueurs: List[Joueur]):
        self.joueurs = joueurs
        self.nombre_joueurs = len(joueurs)

    def generer_paires_joueurs(self, joueurs: List[Joueur]):
        self.paires_joueurs = []
        i = 0
        while i < len(joueurs) - 1:  # -1 pour se proteger d'indexError
            self.paires_joueurs.append((joueurs[i], joueurs[i+1]))
            i += 2


if __name__ == '__main__':
    pass
