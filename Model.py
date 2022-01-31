


class Tournoi:
    '''Classe Tournoi'''



    # Initialisation du Tournoi à l'aide du dictionnaire nouveau_tournoi
    tournoi_vide = {
            'nom' : '',
            'lieu': '',
            'date_debut': '',
            'date_fin': '',
            'nombre_tours' : '',
            'controle_du_temps': '',
            'description': '',
        }
    def __init__(self, nouveau_tournoi: Dict[str, str]=tournoi_vide):
        # Itération sur les clés du dictionnaire
        for data in nouveau_tournoi.keys:
            self.data = nouveau_tournoi[data]

class Joueur:
    pass

class Match:
    pass

class Ronde:
    pass


if __name__ == '__main__':

    tournoi_test = {'nom': 'Tournoi TEst', 'lieu': 'TEST VILLE', 'date_debut': datetime.date(2022, 1, 31), 'date_fin': '', 'nombre_tours': '4', 'controle_du_temps': 'bullet', 'description': 'ok description'}

    vide= Tournoi()
    print(vide)
    test = Tournoi(tournoi_test)
    print(test)