from typing import Any, Dict, List
from datetime import date

# Constantes Globales
CHOIX_MENU_PRINCIPAL = {1: 'Créer un nouveau tournoi',
                        2: 'Ajouter huit joueurs',
                        3: 'Génèrer des paires de joueurs pour le premier/prochain tour',
                        4: 'Entrer les résultats',
                        5: 'Terminer le tournoi',
                        6: 'Quitter'}
# nombres de tours (Round) par tournoi
NOMBRE_DE_TOURS = 4

# nombre de joueurs par tournoi
NOMBRE_DE_JOUEURS = 8


#### model.py
class Sex(Enum):
    Male = 'm'
    Female = 'f'

@dataclass
class Player:
    nom_de_famille: str
    prenom: str
    date_de_naissance: datetime = datetime.now()
    sexe: Sex = Sex.Female
    classement: int = 1


player = Player(nom_de_famille='da costa', prenom='gabriel', sexe=Sex.Male, classement=1)


class Tournament:
    pass

class Match:
    pass

class Round:
    pass


class State:
    def __init__(self):
        self.players = []
        self.players_count = 0
        self.tournament = None

    def add_players(self, players: List[Player]):
        self.players = players
        self.players_count = len(players)



class Vue2:
    def __init__(self):
        pass

    def input_new_players(self):
        res = input()
        players: List[Player] = parse_and_validate_players(res)
        return players

    def display_players(self, players: List[Player], player_count: int):
        print(players)
        print(player_count)


class Controller2:
    def __init__(self):
        self.state = State()
        self.vue = Vue2()

    def add_players(self):
        players = self.vue.input_new_players()
        self.state.add_players(players)


    def get_players(self):
        # get from state
        players = self.state.players
        player_count = self.state.players_count

        # send to vue
        self.vue.display_players(players, player_count)

    def display_menu(self):
        exit = False
        menu_input = input()
        if menu_input == 1:
            self.add_players()
        elif menu_input == 2:
            self.get_players()
        elif menu_input == 0:
            exit = True
        return exit

    def init(self):
        must_exit = False
        while not must_exit:
            must_exit = self.display_menu()


### in main.py
controller = Controller2()
controller.init()

def parse_string_not_empty(user_input: str) -> Tuple[Optional[Any], bool, str]:
    if len(user_input) > 0:
        return user_input, True, ''
    else:
        return None, False, 'String length must be > 0'

def parse_int(user_input: str):
    try:
        res = int(user_input)
        return res, True, ''
    except ValueError:
        return None, False, f'{user_input} is not a valid integer'


def validate_small_string(string: str) -> Tuple[Any, bool, str]:
    if  0 < len(string) < 10:
        result = {
            'string': string,
            'lowercased': string.lower()
        }
        return result, True, ''
    else:
        return None, False, 'string length should be less than 10 chars'


def parse_and_validate(explanation: str,
                       parse: Callable[[str], Tuple[Optional[Any], bool, str]],
                       validate: Callable[[Any], Tuple[Any, bool, str]]):
    is_valid, error_message = False, None
    final_result = None
    while not is_valid:
        user_input = input(explanation)
        validatable_result, is_valid, error_message = parse(user_input)
        if is_valid:
            final_result, is_valid, error_message = validate(validatable_result)

        if not is_valid:
            print(error_message)

    return final_result

parse_and_validate(parse=parse_string_not_empty, validate=validate_small_string, explanation='Input the users name')

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
            print(choix, '--', CHOIX_MENU_PRINCIPAL[choix])

        # Boucle pour définir le Choix du menu
        while (True):
            try:
                choix_utilisateur_menu_principal = int(input(
                    '\nRenseignez votre choix parmis les propositions ci-dessus (1 à ' + str(
                        len(CHOIX_MENU_PRINCIPAL)) + ') : '))
                if (choix_utilisateur_menu_principal > 0 and choix_utilisateur_menu_principal <= int(
                        len(CHOIX_MENU_PRINCIPAL))):
                    break
                else:
                    raise Exception
            except:
                print('Veuillez renseigner un entier compris entre 1 et ' + str(len(CHOIX_MENU_PRINCIPAL)) + ' .')

        return choix_utilisateur_menu_principal

    def menu_creer_nouveau_tournoi(self) -> Dict[str, str]:
        '''Création d'un nouveau tournoi en renseignant toutes les informations demandées.'''

        # Initialisation
        nouveau_tournoi = {
            'nom': '',
            'lieu': '',
            'date_debut': '',
            'date_fin': '',
            'nombre_tours': str(NOMBRE_DE_TOURS),
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
        nom_du_tournoi = parse_and_validate(parse=parse_string_not_empty, validate=validate_small_string, explanation='\nRenseignez le Nom du tournoi : ')

        # Boucle pour définir le lieu du tournoi
        lieu = parse_and_validate(parse=parse_string_not_empty, validate=validate_small_string, explanation='\nRenseignez le Nom du tournoi : ')


        # définition date de début de tournoi
        nouveau_tournoi['date_debut'] = date.today()

        # Boucle pour définir le contrôle du temps
        while (True):
            try:
                nouveau_tournoi['controle_du_temps'] = str(
                    input('\nRenseignez le contrôle du temps ("bullet", "blitz" ou "coup rapide") : '))
                if nouveau_tournoi['controle_du_temps'] == 'bullet':
                    break
                elif nouveau_tournoi['controle_du_temps'] == 'blitz':
                    break
                elif nouveau_tournoi['controle_du_temps'] == 'coup rapide':
                    break
                else:
                    raise Exception
            except:
                print('Choisissez le contrôle du temps en écrivant "bullet", "blitz" ou "coup rapide".')

        # Description
        nouveau_tournoi['description'] = input('Rensignez les remarques générales du directeur du tournoi : ')

        return nouveau_tournoi

    def ajouter_huit_joueurs(self) -> List[Dict[str, str]]:
        '''AJout des informations de huit joueurs dans une liste de dictionnaires à destination du Controller.'''

        # Initialisation
        # liste retournée contenant les informations des huit joueurs
        nouveaux_joueurs = []
        # dictionnaire type contenant les informations d'un joueur
        information_nouveau_joueur = {
            'nom_de_famille': '',
            'prénom': '',
            'date_de_naissance': '',
            'sexe': '',
            'classement': '',
        }

        # Affichage de l'entête
        affichage_menu_ajouter_huit_joueurs = '''
==============================
Ajouter ''' + str(NOMBRE_DE_JOUEURS) + ''' joueurs
==============================
'''
        print(affichage_menu_ajouter_huit_joueurs)

        # Boucle sur les huits joueurs
        for joueur in range(1, 9):
            # ajout du dictionnaire type à la liste de nouveaux joueurs
            nouveaux_joueurs.append(information_nouveau_joueur)

            # Affichage de l'entête pour chaque nouveau joueur
            affichage_nouveau_joueur = '''
    Renseigner les informations du joueur n°''' + str(joueur) + '''
    ==========================================
            '''
            print(affichage_nouveau_joueur)

            # Boucle pour définir le nom de famille
            while (True):
                try:
                    nouveaux_joueurs[joueur - 1]['nom_de_famille'] = str(
                        input('\nRenseignez le Nom de famille du joueur n°' + str(joueur) + ' : '))
                    if len(nouveaux_joueurs[joueur - 1]['nom_de_famille']) > 0:
                        break
                    else:
                        raise Exception
                except:
                    print('Veuillez renseigner un Nom de famille contenant au moins un charactère.')

            # Boucle pour définir le prénom
            while (True):
                try:
                    nouveaux_joueurs[joueur - 1]['prénom'] = str(
                        input('\nRenseignez le Prénom du joueur n°' + str(joueur) + ' : '))
                    if len(nouveaux_joueurs[joueur - 1]['prénom']) > 0:
                        break
                    else:
                        raise Exception
                except:
                    print('Veuillez renseigner un Prénom contenant au moins un charactère.')

            # Boucle pour définir la date de naissance
            while (True):
                try:
                    entree_date = str(input(
                        '\nRenseignez la Date de naissance du joueur n°' + str(joueur) + ' au format "jj/mm/aaaa" : '))
                    jour_test, mois_test, annee_test = entree_date.split('/')
                    if len(annee_test) != 4:
                        raise Exception
                    else:
                        nouveaux_joueurs[joueur - 1]['date_de_naissance'] = date(int(annee_test), int(mois_test),
                                                                                 int(jour_test))
                        break
                except:
                    print('Veuillez renseigner une date valide au format "jj/mm/aaaa".')

            # Boucle pour définir le sexe
            while (True):
                try:
                    nouveaux_joueurs[joueur - 1]['sexe'] = str(
                        input('\nRenseignez le sexe du joueur n°' + str(joueur) + ' (M/F) : '))
                    if nouveaux_joueurs[joueur - 1]['sexe'] == 'M':
                        break
                    elif nouveaux_joueurs[joueur - 1]['sexe'] == 'F':
                        break
                    else:
                        raise Exception
                except:
                    print('Veuillez renseigner le sexe du joueur sous la forme "M" pour masculin ou "F" pour féminin.')

            # Boucle pour définir le classement
            while (True):
                try:
                    nouveaux_joueurs[joueur - 1]['classement'] = int(
                        input('\nRenseignez le classement du joueur n°' + str(joueur) + ' : '))
                    if nouveaux_joueurs[joueur - 1]['classement'] > 0:
                        break
                    else:
                        raise Exception
                except:
                    print('Veuillez renseigner un entier positif.')

        return nouveaux_joueurs

    def afficher_paires_joueurs(self, paires_joueurs: List[tuple[str, str]]):

        # Affichage de l'entête
        affichage_paires_joueurs_entête = '''
==========================================================
''' + str(len(paires_joueurs)) + ''' nouvelles paires de joueurs générées avec succès !
==========================================================
'''
        print(affichage_paires_joueurs_entête)

        # Boucle pour afficher toutes les paires de joueurs
        for paires in range(1, len(paires_joueurs) + 1):
            print('Paire n°' + str(paires) + ' : ' + paires_joueurs[paires - 1][0] + ' / ' + paires_joueurs[paires - 1][
                1])

    def entrer_scores(self, ):
        pass


if __name__ == '__main__':
    initiation_vue = Vue()
    # paires_6_joueurs = [('Gabriel1', 'Stephane1'), ('Gabriel2', 'Stephane2'), ('Gabriel3', 'Stephane3'), ('Gabriel4', 'Stephane4'), ('Gabriel5', 'Stephane5'), ('Gabriel6', 'Stephane6')]
    # paires_8_joueurs = [('Gabriel1', 'Stephane1'), ('Gabriel2', 'Stephane2'), ('Gabriel3', 'Stephane3'), ('Gabriel4', 'Stephane4'), ('Gabriel5', 'Stephane5'), ('Gabriel6', 'Stephane6'), ('Gabriel7', 'Stephane7'), ('Gabriel8', 'Stephane8')]
    # resultat = initiation_vue.afficher_paires_joueurs(paires_6_joueurs)
    # print(resultat)
    # resultat = initiation_vue.afficher_paires_joueurs(paires_8_joueurs)
    # print(resultat)

    resultat = initiation_vue.menu_creer_nouveau_tournoi()
    print(resultat)
