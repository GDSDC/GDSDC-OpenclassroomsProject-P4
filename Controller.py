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
        self.state.creer_nouveau_tournoi(nouveau_tournoi)

if __name__ == '__main__':

    initiation_controller = Controller()
    creer_nouveau_tournoi_test = initiation_controller.creer_nouveau_tournoi()
