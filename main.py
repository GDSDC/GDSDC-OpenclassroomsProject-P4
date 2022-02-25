from core.controller import Controller
from core.model import Joueur, Sex
from datetime import date

TEST_DATE = date(year=2022, month=2, day=24)

PLAYER1 = Joueur(nom_de_famille='Nom de famille TEST1', prenom='prenom TEST1',
                 date_de_naissance=TEST_DATE, sexe=Sex.MALE, classement=1)
PLAYER2 = Joueur(nom_de_famille='Nom de famille TEST2', prenom='prenom TEST2',
                 date_de_naissance=TEST_DATE, sexe=Sex.FEMALE, classement=3)
PLAYER3 = Joueur(nom_de_famille='Nom de famille TEST3', prenom='prenom TEST3',
                 date_de_naissance=TEST_DATE, sexe=Sex.MALE, classement=2)
PLAYER4 = Joueur(nom_de_famille='Nom de famille TEST4', prenom='prenom TEST4',
                 date_de_naissance=TEST_DATE, sexe=Sex.FEMALE, classement=4)

PLAYERS = [PLAYER4, PLAYER3, PLAYER2, PLAYER1]
ACTEURS = {1: PLAYER4, 2: PLAYER3, 3: PLAYER2, 4: PLAYER1}

init_controller = Controller()
init_controller.creer_nouveau_tournoi()
init_controller.state.tournoi.joueurs_du_tournoi = PLAYERS
init_controller.state.acteurs = ACTEURS
init_controller.rapport_joueurs_classement()
init_controller.rapport_acteur_alphabetique()
