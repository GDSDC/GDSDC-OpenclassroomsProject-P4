
nouveaux_joueurs =[]

for joueur in range(1, 4):
    information_nouveau_joueur = {
        'info_1': '',
        'info_2': ''
    }
    # ajout du dictionnaire type à la liste de nouveaux joueurs
    nouveaux_joueurs.append(information_nouveau_joueur)
    print('information_nouveau_joueur : ' + str(information_nouveau_joueur))
    print('nouveaux_joueurs en début de boucle suite à .append' + str(nouveaux_joueurs))

    # Définition du nom de famille
    nouveau_joueur_info_1 = '\nRenseignez l\'info_1 : '
    nouveaux_joueurs[joueur - 1]['info_1'] = input(nouveau_joueur_info_1)
    # Définition le prénom
    nouveau_joueur_info_2 = '\nRenseignez l\'info_2 : '
    nouveaux_joueurs[joueur - 1]['info_2'] = input(nouveau_joueur_info_2)

    print('indice en fin de boucle : ' + str(joueur - 1))
    print('information_joueur  en fin de boucle' + str(nouveaux_joueurs[joueur - 1]))
    print('nouveaux_joueurs en fin de boucle' + str(nouveaux_joueurs))
    print('information_nouveau_joueur : ' + str(information_nouveau_joueur))



