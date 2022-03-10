from typing import List, Optional, Tuple, Dict

from core.controller import Controller
from core.model import *
from core.vue import Vue
from datetime import datetime, timedelta, date


# PLayer Test Generator
def player_test(indice: int) -> Joueur:
    player = Joueur(nom_de_famille='Nom de famille TEST' + str(indice), prenom='prenom TEST' + str(indice),
                    date_de_naissance=datetime(date.today().year,date.today().month, date.today().day), sexe=Sex.MALE, classement=indice)
    return player


PLAYER1 = player_test(1)
PLAYER2 = player_test(2)
PLAYER3 = player_test(3)
PLAYER4 = player_test(4)


# Changing ranking
def nouveau_classement(joueur: Joueur, nouveau_classement_valeur: int) -> Joueur:
    player_nouveau_classement = joueur
    player_nouveau_classement.classement = nouveau_classement_valeur
    return player_nouveau_classement


PLAYER_NOUVEAU_CLASSEMENT1 = nouveau_classement(joueur=PLAYER1, nouveau_classement_valeur=10)
PLAYER_NOUVEAU_CLASSEMENT2 = nouveau_classement(joueur=PLAYER2, nouveau_classement_valeur=20)
PLAYER_NOUVEAU_CLASSEMENT3 = nouveau_classement(joueur=PLAYER3, nouveau_classement_valeur=30)
PLAYER_NOUVEAU_CLASSEMENT4 = nouveau_classement(joueur=PLAYER4, nouveau_classement_valeur=40)

SCORES_VIDE = [((PLAYER1, None), (PLAYER2, None)), ((PLAYER3, None), (PLAYER4, None))]
SCORES = [((PLAYER1, Score.GAGNANT), (PLAYER2, Score.PERDANT)), ((PLAYER3, Score.GAGNANT), (PLAYER4, Score.PERDANT))]

ACTEURS = {1: PLAYER1, 5: PLAYER2, 3: PLAYER3, 4: PLAYER4}


def tournoi1(rounds_input: Optional[List[Round]] = []) -> Tournoi:
    return Tournoi(nom='Tournoi_TEST',
                   lieu='lieu_TEST',
                   date_debut=datetime.now(),
                   date_fin=datetime.now(),
                   controle_du_temps=ControleDuTemps.BLITZ,
                   description='Remarques_TEST',
                   joueurs_du_tournoi=[PLAYER1, PLAYER2, PLAYER3, PLAYER4],
                   joueurs_en_jeux=[PLAYER1, PLAYER2, PLAYER3, PLAYER4],
                   rounds=rounds_input)


def tournoi2():
    return Tournoi(nom='Tournoi_TEST',
                   lieu='lieu_TEST',
                   date_debut=datetime.now() + timedelta(days=10),
                   date_fin=datetime.now() + timedelta(days=10),
                   controle_du_temps=ControleDuTemps.BLITZ,
                   description='Remarques_TEST',
                   joueurs_du_tournoi=[PLAYER1, PLAYER2, PLAYER3, PLAYER4],
                   joueurs_en_jeux=[PLAYER1, PLAYER2, PLAYER3, PLAYER4],
                   rounds=[])


def tournoi3():
    return Tournoi(nom='Tournoi_TEST',
                   lieu='lieu_TEST',
                   date_debut=datetime.now() + timedelta(days=20),
                   date_fin=datetime.now() + timedelta(days=20),
                   controle_du_temps=ControleDuTemps.BLITZ,
                   description='Remarques_TEST',
                   joueurs_du_tournoi=[PLAYER1, PLAYER2, PLAYER3, PLAYER4],
                   joueurs_en_jeux=[PLAYER1, PLAYER2, PLAYER3, PLAYER4],
                   rounds=[])


def round1():
    return Round(nom=RoundName.ROUND1, match_liste=[], date_debut=datetime.now(),
                 date_fin=datetime.now())


def round2():
    return Round(nom=RoundName.ROUND2, match_liste=[], date_debut=datetime.now(),
                 date_fin=datetime.now())


def round3():
    return Round(nom=RoundName.ROUND3, match_liste=SCORES, date_debut=datetime.now(),
                 date_fin=datetime.now())


def round4():
    return Round(nom=RoundName.ROUND4, match_liste=SCORES_VIDE, date_debut=datetime.now(),
                 date_fin=datetime.now())


def state1():
    state = State(acteurs=ACTEURS, tournoi=tournoi1(rounds_input=[round1(), round2()]))
    return state


def state2():
    state = State(tournoi=tournoi1(rounds_input=[round1(), round2(), round3()]))
    return state


def state3():
    state = State(tournoi=tournoi1(rounds_input=[round1(), round2(), round3(), round4()]))
    return state


def state4():
    state = State(acteurs=ACTEURS, tournoi=tournoi1(rounds_input=[round3()]))
    return state


def state5():
    state = State(tournois=[tournoi1(rounds_input=[round1(), round2(), round3()])])
    return state


class TestVue(Vue):
    @staticmethod
    def menu_principal() -> int:
        # not used in tests
        return 1

    def creer_nouveau_tournoi(self, acteurs: Dict[int, Joueur]) -> [Tournoi, List[Joueur]]:
        return tournoi1(), []

    # def ajouter_joueurs(self, nb_joueurs: Optional[int]) -> List[Joueur]:
    #     return [PLAYER1, PLAYER2, PLAYER3, PLAYER4]

    def creer_nouveau_round(self, numero_round: int) -> Round:
        return round3()

    def entrer_scores(self, round_param: Round) -> List[Match]:
        return SCORES

    def modifier_classement(self, joueurs_classement: List[Joueur]) -> List[Joueur]:
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
    nouveau_tournoi = tournoi1()

    # When
    state.creer_nouveau_tournoi(nouveau_tournoi)

    # Then
    assert state.tournoi == nouveau_tournoi


# def test_model_ajouter_joueurs():
#     """Function to test the state.creation of players"""
#
#     # Given
#     state = state1()
#     player1 = PLAYER1
#     player2 = PLAYER2
#     # When
#     state.ajouter_joueurs([player1, player2])
#
#     # Then
#     assert state.tournoi.joueurs_en_jeux == [player1, player2]
#     assert state.nombre_joueurs() == 2


def test_model_creer_nouveau_round():
    """Function to test the state.creation of new round"""

    # Given
    state = state1()

    nouveau_round = round3()

    # When
    state.creer_nouveau_round(nouveau_round)

    # Then
    assert state.tournoi.rounds == [round1(), round2(), round3()]


def test_model_generer_paires_joueurs():
    """Function to test the state.creation of pairs of players"""

    # Given
    state = state1()

    # When
    state.generer_paires_joueurs([PLAYER1, PLAYER2, PLAYER3, PLAYER4])

    # Then
    assert state.tournoi.rounds[-1].match_liste == [((PLAYER1, None), (PLAYER2, None)),
                                                    ((PLAYER3, None), (PLAYER4, None))]


def test_model_entrer_scores():
    """Function that test the model.entrer_scores"""

    # Given
    state = state3()
    scores = SCORES

    # When
    state.entrer_scores(scores=scores)

    # Then
    assert state.tournoi.rounds[-1].match_liste == scores


def test_model_modifier_classement():
    """Function that test the model.modifier_classement_tournoi"""

    # Given
    state = state1()
    joueurs_classement = [PLAYER_NOUVEAU_CLASSEMENT1,
                          PLAYER_NOUVEAU_CLASSEMENT2,
                          PLAYER_NOUVEAU_CLASSEMENT3,
                          PLAYER_NOUVEAU_CLASSEMENT4]

    # When
    state.modifier_classement_tournoi(joueurs_classement=joueurs_classement)

    # Then
    assert state.tournoi.joueurs_du_tournoi == joueurs_classement


# CONTROLLER TESTS

def test_controller_creer_nouveau_tournoi():
    """Function to test the controller.creation of tournament"""

    # Given
    controller = Controller(vue=TEST_VUE)
    nouveau_tournoi = tournoi1()

    # When
    controller.creer_nouveau_tournoi()

    # Then
    assert controller.state.tournoi == nouveau_tournoi


# def test_controller_ajouter_joueurs():
#     """Function to test the controller.creation of players"""
#
#     # Given
#     init_sate = state1()
#     controller = Controller(vue=TEST_VUE, state=init_sate)
#     liste_joueurs = [PLAYER1, PLAYER2, PLAYER3, PLAYER4]
#
#     # When
#     controller.ajouter_joueurs()
#
#     # Then
#     assert controller.state.tournoi.joueurs_en_jeux == liste_joueurs
#     assert controller.state.nombre_joueurs() == len(liste_joueurs)


def test_controller_creer_nouveau_round():
    """Function to test the controller.creation of new round"""

    # Given
    init_sate = state1()
    controller = Controller(vue=TEST_VUE, state=init_sate)

    # When
    # Round 3 creation
    controller.creer_nouveau_round()

    # Then
    assert controller.state.tournoi.rounds == [round1(), round2(), round3()]


def test_controller_generer_paires_joueurs():
    """Function to test the controller.creation of paires"""

    # Given
    init_sate = state1()
    print(f'init_sate.tournoi.joueurs_en_jeux : {init_sate.tournoi.joueurs_en_jeux}')
    controller = Controller(vue=TEST_VUE, state=init_sate)
    print(f' state.tournoi.joueurs_en_jeux : {controller.state.tournoi.joueurs_en_jeux}')

    # When
    controller.generer_paires_joueurs()

    # Then
    assert controller.state.tournoi.rounds[-1].match_liste == [((PLAYER1, None), (PLAYER2, None)),
                                                               ((PLAYER3, None), (PLAYER4, None))]


def test_controller_mettre_a_jour_joueurs():
    """Function to test the update of players when creating new Round"""

    # Given
    init_sate2 = state2()
    controller = Controller(vue=TEST_VUE, state=init_sate2)

    # When
    controller.mettre_a_jour_joueurs()

    # Then
    assert controller.state.tournoi.joueurs_en_jeux == [PLAYER1, PLAYER3]
    assert controller.state.tournoi.joueurs_du_tournoi == [PLAYER1, PLAYER2, PLAYER3, PLAYER4]


def test_controller_entrer_scores():
    """Function that test the controller.entrer_scores"""

    # Given
    init_sate2 = state2()
    controller = Controller(vue=TEST_VUE, state=init_sate2)

    # When
    controller.entrer_scores()

    # Then
    assert controller.state.tournoi.rounds[-1].match_liste == SCORES


def test_modifier_classement():
    """Function that test the controller.modifier_classement_tournoi"""

    # Given
    init_sate = state1()
    controller = Controller(vue=TEST_VUE, state=init_sate)

    # When
    controller.modifier_classement_tournoi()

    # Then
    assert controller.state.tournoi.joueurs_du_tournoi == [PLAYER_NOUVEAU_CLASSEMENT1,
                                                           PLAYER_NOUVEAU_CLASSEMENT2,
                                                           PLAYER_NOUVEAU_CLASSEMENT3,
                                                           PLAYER_NOUVEAU_CLASSEMENT4]


def test_controller_terminer_tournoi():
    """Function to test closing a tournament"""

    # Given
    controller = Controller(state=state2())
    init_controller = Controller(state=state5())

    # Then
    controller.terminer_tournoi()

    # Then
    assert controller.state == init_controller.state


if __name__ == '__main__':
    pass
