import controller

initiation_controller = controller.Controller()
# initiation_controller.test_ajouter_joueurs(nombre_joueur=2)
initiation_controller.creer_nouveau_tournoi()
resultat = initiation_controller.state.tournoi
print(resultat)
