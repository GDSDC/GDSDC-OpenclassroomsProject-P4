from core import controller


init_controller = controller.Controller()
init_controller.creer_nouveau_tournoi()
init_controller.ajouter_joueurs(nb_joueurs=2)
init_controller.creer_nouveau_round()
init_controller.generer_paires_joueurs()
init_controller.entrer_scores()
print(init_controller.state.actual_round.match_liste)