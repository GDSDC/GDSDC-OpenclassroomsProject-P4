from typing import Any, Dict, List
from datetime import date


# Constantes Globales
CHOIX_MENU_PRINCIPAL = {1 : 'Créer un nouveau tournoi',
                        2 : 'Ajouter huit joueurs',
                        3 : 'Génèrer des paires de joueurs pour le premier/prochain tour',
                        4 : 'Entrer les résultats',
                        5 : 'Terminer le tournoi',
                        6 : 'Quitter'}
# nombres de tours (Round) par tournoi
NOMBRE_DE_TOURS = 4

class Vue:
    '''Classe qui gère l'interface/menu du programme.'''

    def menu_principal(self) -> int:
        '''Affichage du menu principal et récupération du choix de l'utilisateur.'''

        # Affichage de l'entête
        affichage_menu_principal = '''
==============================
Menu Principal
==============================
'''
        print(affichage_menu_principal)

        # Affichage des différents choix
        for choix in CHOIX_MENU_PRINCIPAL.keys():
            print(choix,'--', CHOIX_MENU_PRINCIPAL[choix])



        return choix_utilisateur_menu_principal


    def menu_creer_nouveau_tournoi(self) -> Dict[str, str]:
        '''Création d'un nouveau tournoi en renseignant toutes les informations demandées.'''

        # Initialisation
        nouveau_tournoi = {
            'nom' : '',
            'lieu': '',
            'date_debut': '',
            'date_fin': '',
            'nombre_tours' : str(NOMBRE_DE_TOURS),
            'controle_du_temps': '',
            'description': '',
        }

        # Affichage de l'entête
        affichage_menu_creer_nouveau_tournoi = '''
==============================
Créer un nouveau Tournoi
==============================
'''
        print(affichage_menu_creer_nouveau_tournoi)

        # Boucle pour définir le nom du tournoi
        while(True):
            try:
                nouveau_tournoi['nom'] = str(input('\nRenseignez le Nom du tournoi : '))
                if len(nouveau_tournoi['nom']) > 0:
                    break
                else:
                    raise Exception
            except:
                print('Veuillez renseigner un nom de tournoi contenant au moins un charactère.')

        # Boucle pour définir le lieu du tournoi
        while(True):
            try:
                nouveau_tournoi['lieu'] = str(input('\nRenseignez le Lieu du tournoi : '))
                if len(nouveau_tournoi['lieu']) > 0:
                    break
                else:
                    raise Exception
            except:
                print('Veuillez renseigner un lieu de tournoi contenant au moins un charactère.')

        # définition date de début de tournoi
        nouveau_tournoi['date_debut'] = date.today()




        return nouveau_tournoi


if __name__ == '__main__':

    initiation_vue = Vue()
    resultat = initiation_vue.menu_creer_nouveau_tournoi()
    print(resultat)