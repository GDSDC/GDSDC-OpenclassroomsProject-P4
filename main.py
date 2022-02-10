import controller

initiation_controller = controller.Controller()
# initiation_controller.test_ajouter_joueurs(nombre_joueur=2)
initiation_controller.creer_nouveau_round()
resultat = initiation_controller.state.actual_round
print(resultat)
