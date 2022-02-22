a = [(['joueur1', None], ['joueur2', None]), (['joueur3', None], ['joueur4', None])]

for ([joueur_1, score_1], [joueur_2, score_2]) in a:
    print(f'Premier Joueur : {joueur_1} , {score_1}')
    print(f'Deuxième Joueur : {joueur_2} , {score_2}')
    # test comment
    # TODO exemple
    if True:
        score_1 = 'Nouveau Score 1'
        score_2 = 'Nouveau Score 2'
    print(f'Premier Joueur : {joueur_1} , {score_1}')
    print(f'Deuxième Joueur : {joueur_2} , {score_2}')
