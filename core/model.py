from typing import List, Optional
from dataclasses import dataclass
from enum import Enum
from datetime import date, datetime

# INITIALISATION CONSTANTES
# nombres de tours (Round) par tournoi
NOMBRE_DE_TOURS = 4

# nombre de joueurs par tournoi
NOMBRE_DE_JOUEURS = 2


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


# Classe décrivant le Match
class Score(Enum):
    """Classe Enum du système de points"""
    GAGNANT = 1
    PERDANT = 0
    MATCH_NUL = 1 / 2


@dataclass
class Resultat:
    joueur: Joueur
    score: Optional[Score] = None


@dataclass
class Match:
    resultat_1: Resultat
    resultat_2: Resultat


# Classes décrivant le Round
class RoundName(Enum):
    """Classe Enum décrivant les noms de Rounds utilisés"""
    ROUND1 = 'Round 1'
    ROUND2 = 'Round 2'
    ROUND3 = 'Round 3'
    ROUND4 = 'Round 4'


@dataclass
class Round:
    nom: RoundName
    match_liste: List[Match]
    date_debut: datetime
    date_fin: datetime


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
    rounds: List[Round]
    nombre_tours: int = NOMBRE_DE_TOURS


class State:
    def __init__(self):
        self.joueurs = []
        self.nombre_joueurs = 0
        self.tournoi = None
        self.actual_round = None
        self.round_list = []

    def creer_nouveau_tournoi(self, nouveau_tournoi: Tournoi):
        self.tournoi = nouveau_tournoi

    def ajouter_joueurs(self, joueurs: List[Joueur]):
        self.joueurs = joueurs
        self.nombre_joueurs = len(joueurs)

    def creer_nouveau_round(self, nouveau_round: Round):
        self.actual_round = nouveau_round

    # def terminer_round(self):
    #     self.round_list.append(self.actual_round)
    #     self.actual_round = None

    def generer_paires_joueurs(self, joueurs: List[Joueur]):
        i = 0
        while i < len(joueurs) - 1:  # -1 pour se proteger d'indexError
            self.actual_round.match_liste.append(([joueurs[i], None], [joueurs[i + 1], None]))
            i += 2


if __name__ == '__main__':
    pass
