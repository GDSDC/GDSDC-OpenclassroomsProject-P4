from typing import List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
from datetime import date, datetime

# INITIALISATION CONSTANTES
# nombres de tours (Round) par tournoi
NOMBRE_DE_TOURS = 4

# nombre de joueurs par tournoi
NOMBRE_DE_JOUEURS = 4


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


# Classes décrivant le Round
class RoundName(Enum):
    """Classe Enum décrivant les noms de Rounds utilisés"""
    ROUND1 = 'Round 1'
    ROUND2 = 'Round 2'
    ROUND3 = 'Round 3'
    ROUND4 = 'Round 4'


Match = Tuple[Tuple[Joueur, Optional[Score]], Tuple[Joueur, Optional[Score]]]


@dataclass
class Round:
    nom: Optional[RoundName]
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
    joueurs_du_tournoi: Optional[List[Joueur]] = None
    joueurs_en_jeux: Optional[List[Joueur]] = None
    nombre_tours: int = NOMBRE_DE_TOURS


class State:
    def __init__(self):
        self.acteurs: Dict[int, Joueur] = {}
        self.tournois: List[Tournoi] = []
        self.tournoi: Optional[Tournoi] = None

    # for instance comparison in testing
    def __eq__(self, other):
        if isinstance(other, State):
            return self.acteurs == other.acteurs \
                   and self.tournoi == other.tournoi \
                   and self.tournois == other.tournois
        else:
            return False

    def creer_nouveau_tournoi(self, nouveau_tournoi: Tournoi):
        self.tournoi = nouveau_tournoi

    def nombre_joueurs(self):
        return len(self.tournoi.joueurs_du_tournoi)

    def ajouter_joueurs(self, joueurs: List[Joueur]):
        self.tournoi.joueurs_du_tournoi = joueurs
        self.tournoi.joueurs_en_jeux = joueurs

    def creer_nouveau_round(self, nouveau_round: Round):
        self.tournoi.rounds.append(nouveau_round)

    def generer_paires_joueurs(self, joueurs: List[Joueur]):
        i = 0
        while i < len(joueurs) - 1:  # -1 pour se proteger d'indexError
            self.tournoi.rounds[-1].match_liste.append(((joueurs[i], None), (joueurs[i + 1], None)))
            i += 2

    def entrer_scores(self, scores: List[Match]):
        self.tournoi.rounds[-1].match_liste = scores

    def modifier_classement(self, joueurs_classement: List[Joueur]):
        self.tournoi.joueurs_du_tournoi = joueurs_classement


if __name__ == '__main__':
    pass
