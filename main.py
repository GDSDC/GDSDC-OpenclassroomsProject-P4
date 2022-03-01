from core.controller import Controller
from core.model import Joueur, Sex, Tournoi, ControleDuTemps, Round, RoundName, Score
from datetime import datetime, date, timedelta

TEST_DATETIME = datetime(year=2022, month=2, day=24)
TEST_DATE = TEST_DATETIME.date()

PLAYER1 = Joueur(nom_de_famille='Nom de famille TEST1', prenom='prenom TEST1',
                 date_de_naissance=TEST_DATE, sexe=Sex.MALE, classement=1)
PLAYER2 = Joueur(nom_de_famille='Nom de famille TEST2', prenom='prenom TEST2',
                 date_de_naissance=TEST_DATE, sexe=Sex.FEMALE, classement=3)
PLAYER3 = Joueur(nom_de_famille='Nom de famille TEST3', prenom='prenom TEST3',
                 date_de_naissance=TEST_DATE, sexe=Sex.MALE, classement=2)
PLAYER4 = Joueur(nom_de_famille='Nom de famille TEST4', prenom='prenom TEST4',
                 date_de_naissance=TEST_DATE, sexe=Sex.FEMALE, classement=4)

SCORES = [((PLAYER1, Score.GAGNANT), (PLAYER2, Score.PERDANT)), ((PLAYER3, Score.GAGNANT), (PLAYER4, Score.PERDANT))]
SCORES_VIDE = [((PLAYER1, None), (PLAYER2, None)), ((PLAYER3, None), (PLAYER4, None))]

PLAYERS = [PLAYER4, PLAYER3, PLAYER2, PLAYER1]
ACTEURS = {1: PLAYER4, 2: PLAYER3, 3: PLAYER2, 4: PLAYER1}

ROUND1 = Round(nom=RoundName.ROUND1, match_liste=SCORES_VIDE, date_debut=TEST_DATETIME,
               date_fin=TEST_DATETIME)
ROUND2 = Round(nom=RoundName.ROUND2, match_liste=SCORES, date_debut=TEST_DATETIME,
               date_fin=TEST_DATETIME)

TOURNOI1 = Tournoi(nom='Tournoi_TEST_1',
                   lieu='lieu_TEST_1',
                   date_debut=TEST_DATE,
                   date_fin=TEST_DATE,
                   controle_du_temps=ControleDuTemps.BLITZ,
                   description='Remarques_TEST',
                   joueurs_du_tournoi=[PLAYER1, PLAYER2, PLAYER3, PLAYER4],
                   joueurs_en_jeux=[PLAYER1, PLAYER2, PLAYER3, PLAYER4],
                   rounds=[])

TOURNOI2 = Tournoi(nom='Tournoi_TEST_2',
                   lieu='lieu_TEST_2',
                   date_debut=TEST_DATE + timedelta(days=10),
                   date_fin=TEST_DATE + timedelta(days=10),
                   controle_du_temps=ControleDuTemps.BLITZ,
                   description='Remarques_TEST',
                   joueurs_du_tournoi=[PLAYER4, PLAYER2, PLAYER3, PLAYER1],
                   joueurs_en_jeux=[PLAYER1, PLAYER2, PLAYER3, PLAYER4],
                   rounds=[ROUND1, ROUND2])

TOURNOI3 = Tournoi(nom='Tournoi_TEST_3',
                   lieu='lieu_TEST_3',
                   date_debut=TEST_DATE + timedelta(days=20),
                   date_fin=TEST_DATE + timedelta(days=20),
                   controle_du_temps=ControleDuTemps.BLITZ,
                   description='Remarques_TEST',
                   joueurs_du_tournoi=[PLAYER1, PLAYER2, PLAYER3, PLAYER4],
                   joueurs_en_jeux=[PLAYER1, PLAYER2, PLAYER3, PLAYER4],
                   rounds=[])

init_controller = Controller()
init_controller.state.acteurs = ACTEURS
# init_controller.state.tournois = [TOURNOI2, TOURNOI3, TOURNOI1]
init_controller.afficher_rapport_matchs_tournoi(tournoi=TOURNOI2)

