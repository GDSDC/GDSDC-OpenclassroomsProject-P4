from datetime import datetime

from controller import Controller
from model import ControleDuTemps, Joueur, Sex, State, Tournoi
from vue import Vue


# TODO look at pytest documentation at https://docs.pytest.org/en/7.0.x/

def test_dumb():
    # Given
    a = 1
    b = 2

    # when
    c = a + b

    # then
    assert c == 3


# tests/state_test.py

def test_ajouter_joueurs():
    state = State()
    player1 = Joueur('a', 'b', datetime.today().date(), Sex.FEMALE, 1)
    player2 = Joueur('a2', 'b2', datetime.today().date(), Sex.FEMALE, 1)

    state.ajouter_joueurs([player1, player2])

    assert state.joueurs == [player1, player2]
    assert state.nombre_joueurs == 2


def test_state_creer_nouveau_tournoi():
    state = State()
    tournoi = Tournoi(nom='Tournoi_TEST', lieu='lieu_test', date_debut=datetime.today(), date_fin=datetime.today(),
                      controle_du_temps=ControleDuTemps.BLITZ, description='Remarques', rounds=[])

    state.creer_nouveau_tournoi(tournoi)

    assert state.tournoi == tournoi


# in file tests/controller_test.py
class VueMock(Vue):
    TOURNOI = Tournoi(nom='Tournoi_TEST', lieu='lieu_test', date_debut=datetime.today(), date_fin=datetime.today(),
                      controle_du_temps=ControleDuTemps.BLITZ, description='Remarques', rounds=[])

    def menu_creer_nouveau_tournoi(self) -> Tournoi:
        return self.TOURNOI


def test_controller_creer_nouveau_tournoi():
    myvue = VueMock()
    controller = Controller(myvue)

    controller.creer_nouveau_tournoi()

    assert controller.state.tournoi.nom == 'TOURNOI PAS TEST'
