import Vue

class Controller:
    """Contrôleur principal."""

    def __init__(self):
        """Initialise les modèles et les vues."""

        self.ui = Vue.Vue()


if __name__ == '__main__':

    initiation_controller = Controller()
    choix_utilisateur = initiation_controller.ui.menu_principal()
    print(choix_utilisateur)