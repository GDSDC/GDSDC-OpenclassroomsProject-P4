from core.controller import Controller
from core.model import Joueur, Sex, Tournoi, ControleDuTemps, Round, RoundName, Score
from datetime import datetime, timedelta
from tests.test_script import player_test

PLAYER1 = player_test(indice=1)
PLAYER2 = player_test(indice=2)
PLAYER3 = player_test(indice=3)
PLAYER4 = player_test(indice=4)
PLAYER5 = player_test(indice=5)
PLAYER6 = player_test(indice=6)
PLAYER7 = player_test(indice=7)
PLAYER8 = player_test(indice=8)
PLAYER9 = player_test(indice=9)
PLAYER10 = player_test(indice=10)
PLAYER11 = player_test(indice=11)
PLAYER12 = player_test(indice=12)

SCORES_2 = [((PLAYER5, Score.GAGNANT), (PLAYER6, Score.PERDANT)),
            ((PLAYER7, Score.GAGNANT), (PLAYER8, Score.PERDANT))]
SCORES_VIDE_2 = [((PLAYER5, None), (PLAYER6, None)), ((PLAYER7, None), (PLAYER8, None))]

# PLAYERS = [PLAYER4, PLAYER3, PLAYER2, PLAYER1]
ACTEURS = {1: PLAYER4, 2: PLAYER3, 3: PLAYER2, 4: PLAYER1, 5:PLAYER5, 6:PLAYER6, 7:PLAYER7, 8:PLAYER8}

ROUND1 = Round(nom=RoundName.ROUND1, match_liste=SCORES_2, date_debut=datetime.now(),
               date_fin=datetime.now())
ROUND2 = Round(nom=RoundName.ROUND2, match_liste=SCORES_2, date_debut=datetime.now(),
               date_fin=datetime.now())

TOURNOI1 = Tournoi(nom='Tournoi_TEST_1',
                   lieu='lieu_TEST_1',
                   date_debut=datetime.now(),
                   date_fin=datetime.now(),
                   controle_du_temps=ControleDuTemps.BLITZ,
                   description='Remarques_TEST',
                   joueurs_du_tournoi=[player_test(indice=i) for i in range(1,9)],
                   joueurs_en_jeux=[player_test(indice=i) for i in range(1,9)],
                   rounds=[])

TOURNOI2 = Tournoi(nom='Tournoi_TEST_2',
                   lieu='lieu_TEST_2',
                   date_debut=datetime.now() + timedelta(days=10),
                   date_fin=datetime.now() + timedelta(days=10),
                   controle_du_temps=ControleDuTemps.BLITZ,
                   description='Remarques_TEST',
                   joueurs_du_tournoi=[PLAYER8, PLAYER6, PLAYER7, PLAYER5],
                   joueurs_en_jeux=[PLAYER5, PLAYER6, PLAYER7, PLAYER8],
                   rounds=[ROUND1, ROUND2])

TOURNOI3 = Tournoi(nom='Tournoi_TEST_3',
                   lieu='lieu_TEST_3',
                   date_debut=datetime.now() + timedelta(days=20),
                   date_fin=datetime.now() + timedelta(days=20),
                   controle_du_temps=ControleDuTemps.BLITZ,
                   description='Remarques_TEST',
                   joueurs_du_tournoi=[PLAYER9, PLAYER10, PLAYER11, PLAYER12],
                   joueurs_en_jeux=[PLAYER9, PLAYER10, PLAYER11, PLAYER12],
                   rounds=[ROUND1, ROUND2])
#
# init_controller = Controller()
# init_controller.state.acteurs = ACTEURS
# # init_controller.state.tournois = [TOURNOI2, TOURNOI3, TOURNOI1]
# init_controller.afficher_rapport_matchs_tournoi(tournoi=TOURNOI2)

init_controller = Controller()
init_controller.state.acteurs = ACTEURS
init_controller.state.tournois = [TOURNOI2, TOURNOI3]
init_controller.state.tournoi = TOURNOI1
init_controller.start()
