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
    date_de_naissance: datetime
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

    # for instance comparison in testing
    def __eq__(self, other):
        if isinstance(other, Round):
            return self.nom == other.nom \
                   and self.match_liste == other.match_liste \
                   and self.date_debut.date() == other.date_debut.date() \
                   and self.date_fin.date() == other.date_fin.date()
        else:
            return False


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
    date_debut: datetime
    date_fin: datetime
    controle_du_temps: ControleDuTemps
    description: str
    rounds: List[Round]
    joueurs_du_tournoi: Optional[List[Joueur]] = None
    joueurs_en_jeux: Optional[List[Joueur]] = None
    nombre_tours: int = NOMBRE_DE_TOURS

    # for instance comparison in testing
    def __eq__(self, other):
        if isinstance(other, Tournoi):
            return self.nom == other.nom \
                   and self.lieu == other.lieu \
                   and self.date_debut.date() == other.date_debut.date() \
                   and self.date_fin.date() == other.date_fin.date() \
                   and self.controle_du_temps == other.controle_du_temps \
                   and self.description == other.description \
                   and self.joueurs_du_tournoi == other.joueurs_du_tournoi \
                   and self.joueurs_en_jeux == other.joueurs_en_jeux \
                   and self.nombre_tours == other.nombre_tours
        else:
            return False


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

    def ajouter_nouveau_joueur(self, nouveaux_joueurs: List[Joueur]):
        for joueur in nouveaux_joueurs:
            nouvel_indice = list(self.acteurs.keys())[-1] + 1
            self.acteurs[nouvel_indice] = joueur

    def supprimer_joueur(self, joueur_a_supprimer: Joueur):
        """Function to delete joueur_a_supprimer from self.acteurs"""
        for key, value in self.acteurs.items():
            if value == joueur_a_supprimer:
                del self.acteurs[key]
                break

    def creer_nouveau_round(self, nouveau_round: Round):
        self.tournoi.rounds.append(nouveau_round)

    def generer_paires_joueurs(self, joueurs: List[Joueur]):
        i = 0
        while i < len(joueurs) - 1:  # -1 pour se proteger d'indexError
            self.tournoi.rounds[-1].match_liste.append(((joueurs[i], None), (joueurs[i + 1], None)))
            i += 2

    def entrer_scores(self, scores: List[Match]):
        self.tournoi.rounds[-1].match_liste = scores

    def modifier_classement_tournoi(self, joueurs_classement: List[Joueur]):
        self.tournoi.joueurs_du_tournoi = joueurs_classement

    def modifier_classement(self, joueur_classement: Joueur):
        """Function to update players ranking"""
        for key, acteur in self.acteurs.items():
            if (acteur.date_de_naissance.date() == joueur_classement.date_de_naissance.date()) and (
                    acteur.nom_de_famille == joueur_classement.nom_de_famille) and (
                    acteur.prenom == joueur_classement.prenom) and (acteur.sexe == joueur_classement.sexe) and (
                    acteur.classement != joueur_classement.classement):
                acteur.classement = joueur_classement.classement
                break


if __name__ == '__main__':
    pass
