from core import model, vue
from typing import List, Optional, Tuple


class Controller:
    """Contrôleur principal."""

    def __init__(self):
        """Initialise les modèles et les vues."""
        self.state = model.State()
        self.vue = vue.Vue()

    def creer_nouveau_tournoi(self, test_tournoi: Optional[model.Tournoi] = None):
        nouveau_tournoi = self.vue.menu_creer_nouveau_tournoi(test_tournoi=test_tournoi)
        self.state.creer_nouveau_tournoi(nouveau_tournoi)

    def ajouter_joueurs(self, test_liste_joueurs: Optional[List[model.Joueur]] = None,
                        nb_joueurs: Optional[int] = model.NOMBRE_DE_JOUEURS):
        joueurs = self.vue.ajouter_joueurs(test_liste_joueurs=test_liste_joueurs, nb_joueurs=nb_joueurs)
        self.state.ajouter_joueurs(joueurs)

    def mettre_a_jour_joueurs(self):
        """ Generation of new state.joueurs_en_jeux list"""
        # Initialisation
        self.state.joueurs_en_jeux = []
        last_round = self.state.round_list[-1]
        # Iteration sur tous les résultats de tous les matchs du précédent Round
        for match in last_round.match_liste:
            for resultat in match:
                if resultat[1] != model.Score.PERDANT:
                    self.state.joueurs_en_jeux.append(resultat[0])

    def mettre_a_jour_round_list(self):
        # In case it is the very first round of Tournament
        if self.state.actual_round is None:
            pass
        # If it is the second, third or fourth round
        else:
            self.state.round_list.append(self.state.actual_round)
            self.mettre_a_jour_joueurs()

    def creer_nouveau_round(self, test_nouveau_round: Optional[model.Round] = None):
        self.mettre_a_jour_round_list()
        numero_round = len(self.state.round_list) + 1
        nouveau_round = self.vue.creer_nouveau_round(numero_round=numero_round, test_nouveau_round=test_nouveau_round)
        self.state.creer_nouveau_round(nouveau_round)

    def generer_paires_joueurs(self):
        self.state.generer_paires_joueurs(self.state.joueurs_en_jeux)
        self.vue.afficher_paires_joueurs(self.state.actual_round)

    def entrer_scores(self, test_scores: Optional[List[Tuple[model.Joueur, model.Score]]] = None):
        scores = self.vue.entrer_scores(round=self.state.actual_round, test_scores=test_scores)
        self.state.entrer_scores(scores)

    def afficher_resultats(self):
        """Function that shows all scores of the Tournament"""
        # Initialisation
        scores_results = []
        # Appending round_list if not empty
        if self.state.round_list == []:
            pass
        else:
            scores_results.append(self.state.round_list)
        # Updating scores with actual_round
        if self.state.actual_round.match_liste[0][0][1] is None:
            pass
        else:
            scores_results.append(self.state.actual_round)
        self.vue.afficher_resultats(scores_results)

    def modifier_classement(self, test_classement: Optional[List[model.Joueur]] = None):
        """Function to update players ranking"""
        joueurs_classement = self.vue.modifier_classement(joueurs_classement=self.state.joueurs_du_tournoi,test_classement=test_classement)
        self.state.modifier_classement(joueurs_classement)

    def terminer_tournoi(self):
        """Function to close tournament"""

        # Send Sate to database
        self.mettre_a_jour_round_list()

        # Init the actual instance
        self.__init__()


if __name__ == '__main__':
    pass
