import controller

init_controller = controller.Controller()
init_controller.test_creer_nouveau_tournoi()
init_controller.test_ajouter_joueurs(nombre_joueur=4)
init_controller.creer_nouveau_round()
init_controller.generer_paires_joueurs()
init_controller.entrer_scores()
print(init_controller.state.actual_round.match_liste)

# for match in init_controller.state.actual_round.match_liste:
#     fields = list(match.__dict__.keys())
#     # print(atr)
#     # fields = match.__dataclass_fields__
#     # print(fields)
#     for result in fields:
#         value = getattr(match, result)
#         print(value.score)