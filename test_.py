from core import model, controller
from datetime import datetime, date


# Global Constants
TOURNOI = model.Tournoi(nom='Tournoi_TEST',
                        lieu='lieu_TEST',
                        date_debut=date.today(),
                        date_fin=date.today(),
                        controle_du_temps=model.ControleDuTemps.BLITZ,
                        description='Remarques_TEST',
                        rounds=[], )

PLAYER1 = model.Joueur(nom_de_famille='Nom de famille TEST1', prenom='prenom TEST1',
                       date_de_naissance=date.today(), sexe=model.Sex.MALE, classement=1)
PLAYER2 = model.Joueur(nom_de_famille='Nom de famille TEST2', prenom='prenom TEST2',
                       date_de_naissance=date.today(), sexe=model.Sex.FEMALE, classement=2)
PLAYER3 = model.Joueur(nom_de_famille='Nom de famille TEST3', prenom='prenom TEST3',
                       date_de_naissance=date.today(), sexe=model.Sex.MALE, classement=3)
PLAYER4 = model.Joueur(nom_de_famille='Nom de famille TEST4', prenom='prenom TEST4',
                       date_de_naissance=date.today(), sexe=model.Sex.FEMALE, classement=4)

MATCH_LISTE1 = [([PLAYER1, model.Score.GAGNANT], [PLAYER2, model.Score.PERDANT])]
MATCH_LISTE2 = [([PLAYER3, model.Score.GAGNANT], [PLAYER4, model.Score.PERDANT])]

ROUND1 = model.Round(nom=model.RoundName.ROUND1, match_liste=[], date_debut=datetime.today(),
                     date_fin=datetime.today())
ROUND2 = model.Round(nom=model.RoundName.ROUND2, match_liste=[], date_debut=datetime.today(),
                     date_fin=datetime.today())
ROUND3 = model.Round(nom=model.RoundName.ROUND3, match_liste=[], date_debut=datetime.today(),
                     date_fin=datetime.today())
ROUND4 = model.Round(nom=model.RoundName.ROUND4, match_liste=MATCH_LISTE1, date_debut=datetime.today(),
                     date_fin=datetime.today())


# MODEL TESTS

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

    nouveau_round = ROUND1

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
    state.creer_nouveau_round(ROUND1)
    state.generer_paires_joueurs([player1, player2, player3, player4])

    # Then
    assert state.actual_round.match_liste == [([player1, None], [player2, None]), ([player3, None], [player4, None])]


# CONTROLLER TESTS

def test_controller_creer_nouveau_tournoi():
    """Function to test the controller.creation of tournament"""

    # Given
    controller_tournoi = controller.Controller()
    nouveau_tournoi = TOURNOI

    # When
    controller_tournoi.creer_nouveau_tournoi(test_tournoi=nouveau_tournoi)

    # Then
    assert controller_tournoi.state.tournoi == nouveau_tournoi


def test_controller_ajouter_joueurs():
    """Function to test the controller.creation of players"""

    # Given
    controller_joueurs = controller.Controller()
    liste_joueurs = [PLAYER1, PLAYER2, PLAYER3, PLAYER4]

    # When
    controller_joueurs.ajouter_joueurs(test_liste_joueurs=liste_joueurs)

    # Then
    assert controller_joueurs.state.joueurs == liste_joueurs
    assert controller_joueurs.state.nombre_joueurs == len(liste_joueurs)


def test_controller_creer_nouveau_round():
    """Function to test the controller.creation of new round"""

    # Given
    controller_round = controller.Controller()
    [nouveau_round1, nouveau_round2, nouveau_round3, nouveau_round4] = [ROUND1, ROUND2, ROUND3, ROUND4]

    # When
    # Round 1 creation
    controller_round.creer_nouveau_round(test_nouveau_round=nouveau_round1)
    # Round 2 creation
    controller_round.creer_nouveau_round(test_nouveau_round=nouveau_round2)
    # Round 3 creation
    controller_round.creer_nouveau_round(test_nouveau_round=nouveau_round3)
    # Round 4 creation
    controller_round.creer_nouveau_round(test_nouveau_round=nouveau_round4)

    # Then
    assert controller_round.state.actual_round == ROUND4
    assert controller_round.state.round_list == [ROUND1, ROUND2, ROUND3]


def test_controller_generer_paires_joueurs():
    """Function to test the controller.creation of paires"""

    # Given
    controller_paires = controller.Controller()
    liste_joueurs = [PLAYER1, PLAYER2, PLAYER3, PLAYER4]
    nouveau_round1 = ROUND1

    # When
    controller_paires.ajouter_joueurs(test_liste_joueurs=liste_joueurs)
    controller_paires.creer_nouveau_round(test_nouveau_round=nouveau_round1)

    # Then
    assert controller_paires.state.actual_round.match_liste == [([PLAYER1, None], [PLAYER2, None]),
                                                                ([PLAYER3, None], [PLAYER4, None])]


def test_controller_mettre_a_jour_joueurs():
    """Function to test the update of players when creating new Round"""

    # Given
    controller_maj_joueurs = controller.Controller()
    liste_joueurs = [PLAYER1, PLAYER2, PLAYER3, PLAYER4]
    match_liste = [([PLAYER1, model.Score.GAGNANT], [PLAYER2, model.Score.PERDANT]),
                   ([PLAYER3, model.Score.MATCH_NUL], [PLAYER4, model.Score.MATCH_NUL])]
    last_round = model.Round(nom=model.RoundName.ROUND1, match_liste=match_liste, date_debut=datetime.today(),
                             date_fin=datetime.today())

    # When
    controller_maj_joueurs.ajouter_joueurs(test_liste_joueurs=liste_joueurs)
    controller_maj_joueurs.state.round_list = [last_round]
    controller_maj_joueurs.mettre_a_jour_joueurs()

    # Then
    assert controller_maj_joueurs.state.joueurs == [PLAYER1, PLAYER3, PLAYER4]


def test_controller_entrer_scores():
    """Function that test the controller.entrer_scores"""

    # Given
    controller_scores = controller.Controller()
    scores = [MATCH_LISTE1, MATCH_LISTE2]
    nouveau_round1 = ROUND1

    # When
    controller_scores.creer_nouveau_round(test_nouveau_round=nouveau_round1)
    controller_scores.entrer_scores(test_scores=scores)

    # Then
    assert controller_scores.state.actual_round.match_liste == scores


def test_controller_terminer_tournoi():
    """Function to test closing a tournament"""

    # Given
    initial_state = model.State()
    controller_terminer_tournoi = controller.Controller()
    nouveau_tournoi = TOURNOI
    liste_joueurs = [PLAYER1, PLAYER2, PLAYER3, PLAYER4]
    nouveau_round1 = ROUND1
    nouveau_round2 = ROUND2

    # When
    # Tournament creation
    controller_terminer_tournoi.creer_nouveau_tournoi(test_tournoi=nouveau_tournoi)
    # Adding players
    controller_terminer_tournoi.ajouter_joueurs(test_liste_joueurs=liste_joueurs)
    # Round 1 creation
    controller_terminer_tournoi.creer_nouveau_round(test_nouveau_round=nouveau_round1)
    # Round 2 creation
    controller_terminer_tournoi.creer_nouveau_round(test_nouveau_round=nouveau_round2)
    # Closing Tournament
    controller_terminer_tournoi.terminer_tournoi()

    # Then
    assert controller_terminer_tournoi.state == initial_state


if __name__ == '__main__':
    pass
