import Vue
import Model

class Controller:
    """Contrôleur principal."""

    def __init__(self):
        """Initialise les modèles et les vues."""
        self.state = Model.State()
        self.vue = Vue.Vue()

    def creer_nouveau_tournoi(self):
        nouveau_tournoi = self.vue.menu_creer_nouveau_tournoi()
        nouveau_tournoi = Model.Tournoi(**nouveau_tournoi)
        self.state.creer_nouveau_tournoi(nouveau_tournoi)

    def ajouter_joueurs(self):
        joueurs = self.vue.ajouter_huit_joueurs()
        for indice_joueur in range(len(joueurs)):
            joueurs[indice_joueur] = Model.Joueur(**joueurs[indice_joueur])
        self.state.ajouter_joueurs(joueurs)

    def generer_paires_joueurs(self):
        paires_joueurs_data = self.state.generer_paires_joueurs(self.state.joueurs)
        print(paires_joueurs_data)
        paires_joueurs = []
        for data in paires_joueurs_data:
            paires_joueurs.append((str(data[0]['prenom'] + ' ' + data[0]['nom']),str(data[1]['prenom'] + ' ' + data[1]['nom'])))
        self.vue.afficher_paires_joueurs(paires_joueurs)


if __name__ == '__main__':

    initiation_controller = Controller()
    initiation_controller.ajouter_joueurs()
    print(initiation_controller.state.joueurs)
    initiation_controller.generer_paires_joueurs()