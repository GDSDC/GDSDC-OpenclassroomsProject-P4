from core.controller import Controller
from core.model import Score, Joueur, Sex
from datetime import date

PLAYER1 = Joueur(nom_de_famille='Nom de famille TEST1', prenom='prenom TEST1',
                 date_de_naissance=date.today(), sexe=Sex.MALE, classement=1)
PLAYER2 = Joueur(nom_de_famille='Nom de famille TEST2', prenom='prenom TEST2',
                 date_de_naissance=date.today(), sexe=Sex.FEMALE, classement=2)
PLAYER3 = Joueur(nom_de_famille='Nom de famille TEST3', prenom='prenom TEST3',
                 date_de_naissance=date.today(), sexe=Sex.MALE, classement=3)
PLAYER4 = Joueur(nom_de_famille='Nom de famille TEST4', prenom='prenom TEST4',
                 date_de_naissance=date.today(), sexe=Sex.FEMALE, classement=4)

MATCH_LISTE1 = [([PLAYER1, Score.GAGNANT], [PLAYER2, Score.PERDANT])]
MATCH_LISTE2 = [([PLAYER3, Score.GAGNANT], [PLAYER4, Score.PERDANT])]

init_controller = Controller()
init_controller.creer_nouveau_tournoi()
init_controller.ajouter_joueurs(nb_joueurs=2)
init_controller.creer_nouveau_round()
init_controller.generer_paires_joueurs()
init_controller.state.actual_round.match_liste = MATCH_LISTE1
init_controller.afficher_resultats()
