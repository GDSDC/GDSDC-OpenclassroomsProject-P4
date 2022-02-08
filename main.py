import controller

initiation_controller = controller.Controller()
initiation_controller.test_ajouter_joueurs(nombre_joueur=3)
resultat = initiation_controller.state.joueurs
print(resultat)
