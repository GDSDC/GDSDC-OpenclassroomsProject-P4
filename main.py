from core.controller import Controller
from core.model import Joueur, Sex, State, Tournoi, ControleDuTemps, Round, RoundName, Score
from datetime import datetime, timedelta

from persistence import init_project_database

PLAYER1 = Joueur(nom_de_famille='Nom de famille TEST1', prenom='prenom TEST1',
                 date_de_naissance=datetime.now(), sexe=Sex.MALE, classement=1)
PLAYER2 = Joueur(nom_de_famille='Nom de famille TEST2', prenom='prenom TEST2',
                 date_de_naissance=datetime.now(), sexe=Sex.FEMALE, classement=3)
PLAYER3 = Joueur(nom_de_famille='Nom de famille TEST3', prenom='prenom TEST3',
                 date_de_naissance=datetime.now(), sexe=Sex.MALE, classement=2)
PLAYER4 = Joueur(nom_de_famille='Nom de famille TEST4', prenom='prenom TEST4',
                 date_de_naissance=datetime.now(), sexe=Sex.FEMALE, classement=4)
PLAYER2_1 = Joueur(nom_de_famille='Nom de famille TEST2_1', prenom='prenom TEST2_1',
                   date_de_naissance=datetime.now(), sexe=Sex.MALE, classement=1)
PLAYER2_2 = Joueur(nom_de_famille='Nom de famille TEST2_2', prenom='prenom TEST2_2',
                   date_de_naissance=datetime.now(), sexe=Sex.FEMALE, classement=3)
PLAYER2_3 = Joueur(nom_de_famille='Nom de famille TEST2_3', prenom='prenom TEST2_3',
                   date_de_naissance=datetime.now(), sexe=Sex.MALE, classement=2)
PLAYER2_4 = Joueur(nom_de_famille='Nom de famille TEST2_4', prenom='prenom TEST2_4',
                   date_de_naissance=datetime.now(), sexe=Sex.FEMALE, classement=4)
PLAYER3_1 = Joueur(nom_de_famille='Nom de famille TEST3_1', prenom='prenom TEST3_1',
                   date_de_naissance=datetime.now(), sexe=Sex.MALE, classement=1)
PLAYER3_2 = Joueur(nom_de_famille='Nom de famille TEST3_2', prenom='prenom TEST3_2',
                   date_de_naissance=datetime.now(), sexe=Sex.FEMALE, classement=3)
PLAYER3_3 = Joueur(nom_de_famille='Nom de famille TEST3_3', prenom='prenom TEST3_3',
                   date_de_naissance=datetime.now(), sexe=Sex.MALE, classement=2)
PLAYER3_4 = Joueur(nom_de_famille='Nom de famille TEST3_4', prenom='prenom TEST3_4',
                   date_de_naissance=datetime.now(), sexe=Sex.FEMALE, classement=4)

SCORES_2 = [((PLAYER2_1, Score.GAGNANT), (PLAYER2_2, Score.PERDANT)),
            ((PLAYER2_3, Score.GAGNANT), (PLAYER2_4, Score.PERDANT))]
SCORES_VIDE_2 = [((PLAYER2_1, None), (PLAYER2_2, None)), ((PLAYER2_3, None), (PLAYER2_4, None))]

# PLAYERS = [PLAYER4, PLAYER3, PLAYER2, PLAYER1]
ACTEURS = {1: PLAYER4, 2: PLAYER3, 3: PLAYER2, 4: PLAYER1}

ROUND1 = Round(nom=RoundName.ROUND1, match_liste=SCORES_VIDE_2, date_debut=datetime.now(),
               date_fin=datetime.now())
ROUND2 = Round(nom=RoundName.ROUND2, match_liste=SCORES_2, date_debut=datetime.now(),
               date_fin=datetime.now())

TOURNOI1 = Tournoi(nom='Tournoi_TEST_1',
                   lieu='lieu_TEST_1',
                   date_debut=datetime.now(),
                   date_fin=datetime.now(),
                   controle_du_temps=ControleDuTemps.BLITZ,
                   description='Remarques_TEST',
                   joueurs_du_tournoi=[PLAYER1, PLAYER2, PLAYER3, PLAYER4],
                   joueurs_en_jeux=[PLAYER1, PLAYER2, PLAYER3, PLAYER4],
                   rounds=[])

TOURNOI2 = Tournoi(nom='Tournoi_TEST_2',
                   lieu='lieu_TEST_2',
                   date_debut=datetime.now() + timedelta(days=10),
                   date_fin=datetime.now() + timedelta(days=10),
                   controle_du_temps=ControleDuTemps.BLITZ,
                   description='Remarques_TEST',
                   joueurs_du_tournoi=[PLAYER2_4, PLAYER2_2, PLAYER2_3, PLAYER2_1],
                   joueurs_en_jeux=[PLAYER2_1, PLAYER2_2, PLAYER2_3, PLAYER2_4],
                   rounds=[ROUND1, ROUND2])

TOURNOI3 = Tournoi(nom='Tournoi_TEST_3',
                   lieu='lieu_TEST_3',
                   date_debut=datetime.now() + timedelta(days=20),
                   date_fin=datetime.now() + timedelta(days=20),
                   controle_du_temps=ControleDuTemps.BLITZ,
                   description='Remarques_TEST',
                   joueurs_du_tournoi=[PLAYER3_1, PLAYER3_2, PLAYER3_3, PLAYER3_4],
                   joueurs_en_jeux=[PLAYER3_1, PLAYER3_2, PLAYER3_3, PLAYER3_4],
                   rounds=[])
#
# init_controller = Controller()
# init_controller.state.acteurs = ACTEURS
# # init_controller.state.tournois = [TOURNOI2, TOURNOI3, TOURNOI1]
# init_controller.afficher_rapport_matchs_tournoi(tournoi=TOURNOI2)

state = State(acteurs=ACTEURS, tournois=[TOURNOI2, TOURNOI3], tournoi=TOURNOI1)
# state = init_project_database.load_state()

init_controller = Controller(state=state)
init_controller.start()
