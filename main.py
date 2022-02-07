import controller

initiation_controller = controller.Controller()
initiation_controller.ajouter_joueurs()
resultat = initiation_controller.state.joueurs
print(resultat)
