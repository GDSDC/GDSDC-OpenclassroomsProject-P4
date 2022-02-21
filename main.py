from core.controller import Controller


init_controller = Controller()
init_controller.creer_nouveau_tournoi()
init_controller.ajouter_joueurs(nb_joueurs=4)
init_controller.modifier_classement()
print(init_controller.state.joueurs_du_tournoi)

