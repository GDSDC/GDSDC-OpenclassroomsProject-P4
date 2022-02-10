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
        #self.vue.afficher_paires_joueurs(self.state.paires_joueurs)
        self.vue.afficher_paires_joueurs(self.state.actual_round)

    # Fonctions TEST

    def test_creer_nouveau_tournoi(self):
        nouveau_tournoi = model.Tournoi(nom='Tournoi_TEST',
                                        lieu = 'lieu_test',
                                        date_debut=datetime.today(),
                                        date_fin= datetime.today(),
                                        controle_du_temps = model.ControleDuTemps.BLITZ,
                                        description = 'Remarques',
                                        rounds = [],
                                        )
        self.state.creer_nouveau_tournoi(nouveau_tournoi)

    def test_ajouter_joueurs(self, nombre_joueur: int):
        joueurs = self.vue.test_ajouter_joueurs(nombre_joueur)
        self.state.ajouter_joueurs(joueurs)



if __name__ == '__main__':
    pass
