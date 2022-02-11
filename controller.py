import vue
import model
from datetime import datetime


class Controller:
    """Contrôleur principal."""

    def __init__(self):
        """Initialise les modèles et les vues."""
        self.state = model.State()
        self.vue = vue.Vue()

    def creer_nouveau_tournoi(self):
        nouveau_tournoi = self.vue.menu_creer_nouveau_tournoi()
        self.state.creer_nouveau_tournoi(nouveau_tournoi)

    def ajouter_joueurs(self):
        joueurs = self.vue.ajouter_joueurs()
        self.state.ajouter_joueurs(joueurs)

    def creer_nouveau_round(self):
        numero_round = len(self.state.round_list) + 1
        nouveau_round = self.vue.creer_nouveau_round(numero_round)
        self.state.creer_nouveau_round(nouveau_round)

    def generer_paires_joueurs(self):
        self.state.generer_paires_joueurs(self.state.joueurs)
        self.vue.afficher_paires_joueurs(self.state.actual_round)

    def entrer_scores(self):
        scores = self.vue.entrer_scores(round=self.state.actual_round)
        self.state.actual_round.match_liste = scores


if __name__ == '__main__':
    pass
