from core.vue import Vue
from core.model import State, Joueur, Tournoi, Score, Round, NOMBRE_DE_JOUEURS
from typing import List, Optional, Tuple


class Controller:
    """Contrôleur principal."""

    def __init__(self, state: Optional[State] = None, vue: Optional[Vue] = None):
        """Initialise les modèles et les vues."""
        self.state = state or State()
        self.vue = vue or Vue()

    def creer_nouveau_tournoi(self):
        nouveau_tournoi = self.vue.menu_creer_nouveau_tournoi()
        self.state.creer_nouveau_tournoi(nouveau_tournoi)

    def ajouter_joueurs(self, nb_joueurs: Optional[int] = NOMBRE_DE_JOUEURS):
        joueurs = self.vue.ajouter_joueurs(nb_joueurs=nb_joueurs)
        self.state.ajouter_joueurs(joueurs)

    def mettre_a_jour_joueurs(self):
        """ Generation of new state.joueurs_en_jeux list"""
        # Initialisation
        self.state.joueurs_en_jeux = []
        last_round = self.state.round_list[-1]
        # Iteration sur tous les résultats de tous les matchs du précédent Round
        joueurs_qui_passent_au_prochain_tour = []
        for match in last_round.match_liste:
            for (joueur, score) in match:
                if score != Score.PERDANT:
                    joueurs_qui_passent_au_prochain_tour.append(joueur)

        self.state.joueurs_en_jeux = joueurs_qui_passent_au_prochain_tour

    def mettre_a_jour_round_list(self):
        # In case it is the very first round of Tournament
        if self.state.actual_round is None:
            pass
        # If it is the second, third or fourth round
        else:
            self.state.round_list.append(self.state.actual_round)
            self.mettre_a_jour_joueurs()

    def creer_nouveau_round(self):
        self.mettre_a_jour_round_list()
        numero_round = len(self.state.round_list) + 1
        nouveau_round = self.vue.creer_nouveau_round(numero_round=numero_round)
        self.state.creer_nouveau_round(nouveau_round)

    def generer_paires_joueurs(self):
        self.state.generer_paires_joueurs(self.state.joueurs_en_jeux)
        self.vue.afficher_paires_joueurs(self.state.actual_round)

    def entrer_scores(self):
        scores = self.vue.entrer_scores(round=self.state.actual_round)
        self.state.entrer_scores(scores)

    def afficher_resultats(self):
        """Function that shows all scores of the Tournament"""
        # Initialisation
        scores_results = []
        # Appending round_list if not empty
        if not self.state.round_list:
            pass
        else:
            scores_results.append(self.state.round_list)
        # Updating scores with actual_round
        for ((joueur1, score_joueur1), (joueur2, score_joueur2)) in self.state.actual_round.match_liste:
            if (score_joueur1 is None) and (score_joueur2 is None):
                pass
            else:
                scores_results.append(self.state.actual_round)
                break
        self.vue.afficher_resultats(scores_results)

    def modifier_classement(self):
        """Function to update players ranking"""
        joueurs_classement = self.vue.modifier_classement(joueurs_classement=self.state.joueurs_du_tournoi)
        self.state.modifier_classement(joueurs_classement)

    def terminer_tournoi(self):
        """Function to close tournament"""

        # Send Sate to database
        self.mettre_a_jour_round_list()

        # Init the actual instance
        self.__init__()


if __name__ == '__main__':
    pass
