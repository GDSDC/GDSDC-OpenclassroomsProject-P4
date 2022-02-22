from typing import List, Optional, Tuple

from core.controller import Controller
from core.model import *
from core.vue import Vue
from datetime import datetime, date

# Global Constants

TOURNOI = Tournoi(nom='Tournoi_TEST',
                  lieu='lieu_TEST',
                  date_debut=date.today(),
                  date_fin=date.today(),
                  controle_du_temps=ControleDuTemps.BLITZ,
                  description='Remarques_TEST',
                  rounds=[], )

PLAYER1 = Joueur(nom_de_famille='Nom de famille TEST1', prenom='prenom TEST1',
                 date_de_naissance=date.today(), sexe=Sex.MALE, classement=1)
PLAYER2 = Joueur(nom_de_famille='Nom de famille TEST2', prenom='prenom TEST2',
                 date_de_naissance=date.today(), sexe=Sex.FEMALE, classement=2)
PLAYER3 = Joueur(nom_de_famille='Nom de famille TEST3', prenom='prenom TEST3',
                 date_de_naissance=date.today(), sexe=Sex.MALE, classement=3)
PLAYER4 = Joueur(nom_de_famille='Nom de famille TEST4', prenom='prenom TEST4',
                 date_de_naissance=date.today(), sexe=Sex.FEMALE, classement=4)

PLAYER_NOUVEAU_CLASSEMENT1 = Joueur(nom_de_famille='Nom de famille TEST1', prenom='prenom TEST1',
                                    date_de_naissance=date.today(), sexe=Sex.MALE, classement=10)
PLAYER_NOUVEAU_CLASSEMENT2 = Joueur(nom_de_famille='Nom de famille TEST2', prenom='prenom TEST2',
                                    date_de_naissance=date.today(), sexe=Sex.FEMALE, classement=20)
PLAYER_NOUVEAU_CLASSEMENT3 = Joueur(nom_de_famille='Nom de famille TEST3', prenom='prenom TEST3',
                                    date_de_naissance=date.today(), sexe=Sex.MALE, classement=30)
PLAYER_NOUVEAU_CLASSEMENT4 = Joueur(nom_de_famille='Nom de famille TEST4', prenom='prenom TEST4',
                                    date_de_naissance=date.today(), sexe=Sex.FEMALE, classement=40)


SCORES = [((PLAYER1, Score.GAGNANT), (PLAYER2, Score.PERDANT)), ((PLAYER3, Score.GAGNANT), (PLAYER4, Score.PERDANT))]

ROUND1 = Round(nom=RoundName.ROUND1, match_liste=[], date_debut=datetime.today(),
               date_fin=datetime.today())
ROUND2 = Round(nom=RoundName.ROUND2, match_liste=[], date_debut=datetime.today(),
               date_fin=datetime.today())
ROUND3 = Round(nom=RoundName.ROUND3, match_liste=SCORES, date_debut=datetime.today(),
               date_fin=datetime.today())
ROUND4 = Round(nom=RoundName.ROUND4, match_liste=SCORES, date_debut=datetime.today(),
               date_fin=datetime.today())


def init_hardcoded_state1():
    STATE = State()
    STATE.joueurs_du_tournoi = [PLAYER1, PLAYER2, PLAYER3, PLAYER4]
    STATE.joueurs_en_jeux = [PLAYER1, PLAYER2, PLAYER3, PLAYER4]
    STATE.nombre_joueurs = 0
    STATE.tournoi = TOURNOI
    STATE.actual_round = ROUND2
    STATE.round_list = [ROUND1]
    return STATE


def init_hardcoded_state2():
    STATE = State()
    STATE.joueurs_du_tournoi = [PLAYER1, PLAYER2, PLAYER3, PLAYER4]
    STATE.joueurs_en_jeux = [PLAYER1, PLAYER2, PLAYER3, PLAYER4]
    STATE.nombre_joueurs = 0
    STATE.tournoi = TOURNOI
    STATE.actual_round = ROUND4
    STATE.round_list = [ROUND1, ROUND2, ROUND3]
    return STATE


class TestVue(Vue):
    def menu_principal(self) -> int:
        # not used in tests
        return 1

    def menu_creer_nouveau_tournoi(self, test_tournoi: Optional[Tournoi]) -> Tournoi:
        return TOURNOI

    def ajouter_joueurs(self, test_liste_joueurs: Optional[List[Joueur]], nb_joueurs: Optional[int]) -> List[Joueur]:
        return [PLAYER1, PLAYER2, PLAYER3, PLAYER4]

    def creer_nouveau_round(self, numero_round: int, test_nouveau_round: Optional[Round]) -> Round:
        return ROUND3

    def entrer_scores(self, round: Round, test_scores: Optional[List[Tuple[Joueur, Score]]]) -> List[
        Tuple[Joueur, Score]]:
        return SCORES

    def modifier_classement(self, joueurs_classement: List[Joueur],
                            test_classement: Optional[List[Joueur]]) -> List[Joueur]:
        return [PLAYER_NOUVEAU_CLASSEMENT1,
                PLAYER_NOUVEAU_CLASSEMENT2,
                PLAYER_NOUVEAU_CLASSEMENT3,
                PLAYER_NOUVEAU_CLASSEMENT4]


# Initialisation
TEST_VUE = TestVue()


# MODEL TESTS

def test_model_creer_nouveau_tournoi():
    """Function to test the state.creation of tournament"""

    # Given
    state = State()
    nouveau_tournoi = TOURNOI

    # When
    state.creer_nouveau_tournoi(nouveau_tournoi)

    # Then
    assert state.tournoi == nouveau_tournoi


def test_model_ajouter_joueurs():
    """Function to test the state.creation of players"""

    # Given
    state = State()
    player1 = PLAYER1
    player2 = PLAYER2
    # When
    state.ajouter_joueurs([player1, player2])

    # Then
    assert state.joueurs_en_jeux == [player1, player2]
    assert state.nombre_joueurs == 2


def test_model_creer_nouveau_round():
    """Function to test the state.creation of new round"""

    # Given
    state = State()

    nouveau_round = ROUND3

    # When
    state.creer_nouveau_round(nouveau_round)

    # Then
    assert state.actual_round == nouveau_round


def test_model_generer_paires_joueurs():
    """Function to test the state.creation of pairs of players"""

    # Given
    state = State()
    player1 = PLAYER1
    player2 = PLAYER2
    player3 = PLAYER3
    player4 = PLAYER4

    # When
    state.creer_nouveau_round(ROUND1)
    state.generer_paires_joueurs([player1, player2, player3, player4])

    # Then
    assert state.actual_round.match_liste == [([player1, None], [player2, None]), ([player3, None], [player4, None])]


# CONTROLLER TESTS

def test_controller_creer_nouveau_tournoi():
    """Function to test the controller.creation of tournament"""

    # Given
    controller = Controller(vue=TEST_VUE)
    nouveau_tournoi = TOURNOI

    # When
    controller.creer_nouveau_tournoi()

    # Then
    assert controller.state.tournoi == nouveau_tournoi


def test_controller_ajouter_joueurs():
    """Function to test the controller.creation of players"""

    # Given
    controller = Controller(vue=TEST_VUE)
    liste_joueurs = [PLAYER1, PLAYER2, PLAYER3, PLAYER4]

    # When
    controller.ajouter_joueurs()

    # Then
    assert controller.state.joueurs_en_jeux == liste_joueurs
    assert controller.state.nombre_joueurs == len(liste_joueurs)


def test_controller_creer_nouveau_round():
    """Function to test the controller.creation of new round"""

    # Given
    STATE = init_hardcoded_state1()
    controller = Controller(vue=TEST_VUE, state=STATE)

    # When
    # Round 3 creation
    controller.creer_nouveau_round()

    # Then
    assert controller.state.actual_round == ROUND3
    assert controller.state.round_list == [ROUND1, ROUND2]


def test_controller_generer_paires_joueurs():
    """Function to test the controller.creation of paires"""

    # Given
    STATE = init_hardcoded_state1()
    controller = Controller(vue=TEST_VUE, state=STATE)

    # When
    controller.generer_paires_joueurs()

    # Then
    assert controller.state.actual_round.match_liste == [([PLAYER1, None], [PLAYER2, None]),
                                                         ([PLAYER3, None], [PLAYER4, None])]


def test_controller_mettre_a_jour_joueurs():
    """Function to test the update of players when creating new Round"""

    # Given
    STATE2 = init_hardcoded_state2()
    controller = Controller(vue=TEST_VUE, state=STATE2)

    # When
    controller.mettre_a_jour_joueurs()

    # Then
    assert controller.state.joueurs_en_jeux == [PLAYER1, PLAYER3]
    assert controller.state.joueurs_du_tournoi == [PLAYER1, PLAYER2, PLAYER3, PLAYER4]


if __name__ == '__main__':
    pass
