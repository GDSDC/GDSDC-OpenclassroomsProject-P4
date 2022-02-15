from core import model, controller, vue
from datetime import datetime, date
import random
from typing import List
import pytest

# Global Constants
TOURNOI = model.Tournoi(nom='Tournoi_TEST',
                        lieu='lieu_TEST',
                        date_debut=date.today(),
                        date_fin=date.today(),
                        controle_du_temps=model.ControleDuTemps.BLITZ,
                        description='Remarques_TEST',
                        rounds=[], )

ROUND = model.Round(nom=model.RoundName.ROUND1, match_liste=[], date_debut=datetime.today(),
                                date_fin=datetime.today())

PLAYER1 = model.Joueur(nom_de_famille='Nom de famille TEST1', prenom='prenom TEST1',
                       date_de_naissance=date.today(), sexe=model.Sex.MALE, classement=1)
PLAYER2 = model.Joueur(nom_de_famille='Nom de famille TEST2', prenom='prenom TEST2',
                       date_de_naissance=date.today(), sexe=model.Sex.FEMALE, classement=2)
PLAYER3 = model.Joueur(nom_de_famille='Nom de famille TEST3', prenom='prenom TEST3',
                       date_de_naissance=date.today(), sexe=model.Sex.MALE, classement=3)
PLAYER4 = model.Joueur(nom_de_famille='Nom de famille TEST4', prenom='prenom TEST4',
                       date_de_naissance=date.today(), sexe=model.Sex.FEMALE, classement=4)

def test_model_creer_nouveau_tournoi():
    """Function to test the state.creation of tournament"""

    # Given
    state = model.State()
    nouveau_tournoi = TOURNOI

    # When
    state.creer_nouveau_tournoi(nouveau_tournoi)

    # Then
    assert state.tournoi == nouveau_tournoi


def test_model_ajouter_joueurs():
    """Function to test the state.creation of players"""

    # Given
    state = model.State()
    player1 = PLAYER1
    player2 = PLAYER2
    # When
    state.ajouter_joueurs([player1, player2])

    # Then
    assert state.joueurs == [player1, player2]
    assert state.nombre_joueurs == 2


def test_model_creer_nouveau_round():
    """Function to test the state.creation of new round"""

    # Given
    state = model.State()

    nouveau_round = ROUND

    # When
    state.creer_nouveau_round(nouveau_round)

    # Then
    assert state.actual_round == nouveau_round


def test_model_generer_paires_joueurs():
    """Function to test the state.creation of pairs of players"""

    # Given
    state = model.State()
    player1 = PLAYER1
    player2 = PLAYER2
    player3 = PLAYER3
    player4 = PLAYER4

    # When
    state.creer_nouveau_round(ROUND)
    state.generer_paires_joueurs([player1, player2, player3, player4])

    # Then
    assert state.actual_round.match_liste == [([player1, None], [player2, None]), ([player3, None], [player4, None])]


# class TestVue(vue.Vue):
#     """Class Vue with test functions"""
#
#     def test_ajouter_joueurs(self, nombre_joueur: int):
#         """Function that add nombre_joueur players"""
#         joueurs = []
#         for i in range(1, nombre_joueur + 1):
#             joueurs.append(model.Joueur(nom_de_famille='Nom de Famille Joueur ' + str(i),
#                                         prenom='Prenom Joueur ' + str(i),
#                                         date_de_naissance=date.today(),
#                                         sexe=model.Sex.MALE,
#                                         classement=i * 13
#                                         ))
#         return joueurs
#
#     def test_entrer_scores(self, round_input: model.Round) -> List[model.Match]:
#         """Function that generate random scores from model.Score values"""
#         # Initialisation
#         match_liste_scores = round_input.match_liste
#         nombre_de_paires = len(match_liste_scores)
#         scores_liste = [score.value for score in model.Score]
#
#         # Boucle sur les matchs
#         for paires in range(1, nombre_de_paires + 1):
#             # Boucle sur les résultats du match
#             for result_field in list(match_liste_scores[paires - 1].__dict__.keys()):
#                 resultat = getattr(match_liste_scores[paires - 1], result_field)
#                 score = random.choice(scores_liste)
#                 resultat.score = model.Score(score)
#
#         return match_liste_scores
#
#
# class TestController(controller.Controller):
#     """Class Controller with test functions"""
#
#     def __init__(self):
#         """Initialise les modèles et les vues test."""
#         self.state = model.State()
#         self.vue = TestVue()
#
#     def test_creer_nouveau_tournoi(self):
#         """Function that create new tournament for testing"""
#         nouveau_tournoi = model.Tournoi(nom='Tournoi_TEST',
#                                         lieu='lieu_test',
#                                         date_debut=datetime.today(),
#                                         date_fin=datetime.today(),
#                                         controle_du_temps=model.ControleDuTemps.BLITZ,
#                                         description='Remarques',
#                                         rounds=[],
#                                         )
#         self.state.creer_nouveau_tournoi(nouveau_tournoi)
#
#     def test_ajouter_joueurs(self, nombre_joueur: int):
#         """Function that add nombre_joueur players"""
#
#         joueurs = self.vue.test_ajouter_joueurs(nombre_joueur)
#         self.state.ajouter_joueurs(joueurs)
#
#     def test_entrer_scores(self):
#         """Function that generate random scores from model.Score values"""
#
#         scores = self.vue.test_entrer_scores(round_input=self.state.actual_round)
#         self.state.actual_round.match_liste = scores
#
#
if __name__ == '__main__':
    pass
#
#     init_controller = TestController()
#     init_controller.test_creer_nouveau_tournoi()
#     init_controller.test_ajouter_joueurs(nombre_joueur=4)
#     # print(init_controller.state.joueurs)
#     # print('acutal_round = ' + str(init_controller.state.actual_round))
#     # print('round_liste = ' + str(init_controller.state.round_list))
#     init_controller.creer_nouveau_round()
#     init_controller.generer_paires_joueurs()
#     init_controller.test_entrer_scores()
#     # print(init_controller.state.actual_round.match_liste)
#     # print('acutal_round = ' + str(init_controller.state.actual_round))
#     # print('round_liste = ' + str(init_controller.state.round_list))
#     init_controller.creer_nouveau_round()
#     # print(init_controller.state.joueurs)
#     # print('acutal_round = ' + str(init_controller.state.actual_round))
#     # print('round_liste = ' + str(init_controller.state.round_list))
#     init_controller.generer_paires_joueurs()
#     # print(init_controller.state.joueurs)
