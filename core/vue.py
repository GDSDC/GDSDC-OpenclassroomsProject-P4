from typing import List, Optional, Any, Dict
from datetime import datetime

from core.model import Joueur, Tournoi, Score, Round, RoundName, Match, NOMBRE_DE_JOUEURS
from core import parse_validate_tools as pvt

# GLOBAL CONSTANTS
CHOIX_MENU_PRINCIPAL = {1: 'Gestion des Joueurs (ajouter/supprimer)',
                        2: 'Gestion du Tournoi',
                        3: 'Rapports',
                        4: 'Sauvegarde / Chargement des données',
                        0: 'Quitter le programme'}

CHOIX_MENU_JOUEURS = {1: 'Afficher la liste des Joueurs',
                      2: 'Ajouter un nouveau Joueur',
                      3: 'Supprimer un Joueur',
                      4: 'Mettre à jour le classement d\'un Joueur',
                      0: 'Quitter'}

CHOIX_MENU_TOURNOI = {1: 'Créer un nouveau Tournoi',
                      2: 'Démarrer nouveau Round',
                      3: 'Entrer/Modifier les résultats',
                      4: 'Mettre à jour le classement des Joueurs du Tournoi',
                      5: 'Terminer le tournoi',
                      0: 'Quitter'}

CHOIX_MENU_RAPPORTS = {1: 'Liste de tous les Acteurs par ordre alphabétique',
                       2: 'Liste de tous les Acteurs par classement',
                       3: 'Liste de tous les Joueurs d\'un Tournoi par ordre alphabétique',
                       4: 'Liste de tous les Joueurs d\'un Tournoi par classement',
                       5: 'Liste de tous les Tournois',
                       6: 'Liste de tous les Tours d\'un Tournoi',
                       7: 'Liste de tous les Matchs d\'un Tournoi',
                       0: 'Quitter'}

CHOIX_MENU_SAUVEGARDE_CHARGEMENT = {1: 'Sauvegarder l\'état du programme',
                                    2: 'Charger l\'état du programme',
                                    3: 'Réinitialiser la base donnée',
                                    0: 'Quitter'}


class Vue:
    """Class that manages the interface/menu of the program."""

    def afficher_menu(self, nom_menu: str, menu: Dict[int, str]) -> int:
        """Display of a menu and recovery of the user's choice."""

        # Header display
        affichage_menu = f"""
==============================
{nom_menu}
==============================
    """
        print(affichage_menu)

        # Display of the different choices
        for choix in menu.keys():
            print(choix, '--', menu[choix])

        # Menu choice
        choix_du_menu_texte = '\nRenseignez votre choix parmis les propositions ci-dessus (0 à ' + str(
            len(menu) - 1) + ') : '
        choix_utilisateur_menu = pvt.parse_and_validate(explanation=choix_du_menu_texte,
                                                        parse=pvt.parse_int,
                                                        validate=lambda x: pvt.validate_integer_interval(parsed_int=x,
                                                                                                         interval=(0,
                                                                                                                   len(menu) - 1)))

        return choix_utilisateur_menu

    def creer_nouveau_tournoi(self, acteurs: Dict[int, Joueur]) -> [Tournoi, List[Joueur]]:
        """Creation of a new tournament by filling in all the requested information."""

        # Initialization
        nouveau_tournoi = {
            'nom': '',
            'lieu': '',
            'date_debut': '',
            'date_fin': '',
            'controle_du_temps': '',
            'description': '',
            'rounds': [],
            'joueurs_du_tournoi': [],
        }
        nouveaux_joueurs_a_ajouter_aux_acteurs = []

        # Header display
        affichage_menu_creer_nouveau_tournoi = """
==============================
Créer un nouveau Tournoi
==============================
"""
        print(affichage_menu_creer_nouveau_tournoi)

        # Tournament name definition
        nouveau_tournoi_texte_nom = '\nRenseignez le Nom du tournoi : '
        nouveau_tournoi['nom'] = pvt.parse_and_validate(explanation=nouveau_tournoi_texte_nom,
                                                        parse=pvt.parse_string_not_empty,
                                                        validate=pvt.no_validation)

        # Tournament venue definition
        nouveau_tournoi_texte_lieu = '\nRenseignez le Lieu du tournoi : '
        nouveau_tournoi['lieu'] = pvt.parse_and_validate(explanation=nouveau_tournoi_texte_lieu,
                                                         parse=pvt.parse_string_not_empty,
                                                         validate=pvt.no_validation)

        # Tournament start date definition
        nouveau_tournoi['date_debut'] = datetime.today()

        # Definition of time control
        nouveau_tournoi_texte_controle_du_temps = '\nRenseignez le contrôle du temps ("bullet", "blitz" ou "coup rapide") : '
        nouveau_tournoi['controle_du_temps'] = pvt.parse_and_validate(
            explanation=nouveau_tournoi_texte_controle_du_temps, parse=pvt.parse_string_not_empty,
            validate=pvt.validate_controle_du_temps)

        # Description
        nouveau_tournoi_texte_description = '\nRensignez les remarques générales du directeur du tournoi : '
        nouveau_tournoi['description'] = pvt.parse_and_validate(explanation=nouveau_tournoi_texte_description,
                                                                parse=pvt.parse_string_not_empty,
                                                                validate=pvt.no_validation)

        # Choice of players
        joueurs_du_tournoi, nouveaux_joueurs = self.ajouter_joueurs(nb_joueurs=NOMBRE_DE_JOUEURS, acteurs=acteurs)
        nouveau_tournoi['joueurs_du_tournoi'] = joueurs_du_tournoi
        nouveaux_joueurs_a_ajouter_aux_acteurs = nouveaux_joueurs

        # Formatting the result in Tournoi format
        nouveau_tournoi = Tournoi(**nouveau_tournoi)

        print(f'\nNouveau Tournoi {nouveau_tournoi.nom} créé avec succès !')

        return nouveau_tournoi, nouveaux_joueurs_a_ajouter_aux_acteurs

    def selectionner_tournoi(self, tournois: List[Tournoi]) -> Tournoi:
        """Function to select a Tournament among a list"""

        # Show Tournament list
        self.afficher_rapport_tournois(donnees_rapport=tournois)

        # Select One in list
        selectionner_tournoi_texte = f'\nSélectionnez un Tournoi dans la liste ci-dessus (1 à {len(tournois)}) : '
        tournoi_selectionne = pvt.parse_and_validate(explanation=selectionner_tournoi_texte, parse=pvt.parse_int,
                                                     validate=lambda x: pvt.validate_integer_interval(parsed_int=x,
                                                                                                      interval=(1,
                                                                                                                len(tournois))))
        # Return
        print(f'\nTournoi {tournois[tournoi_selectionne - 1].nom} sélectionné avec succès !')
        return tournois[tournoi_selectionne - 1]

    def ajouter_joueurs(self, nb_joueurs: Optional[int], acteurs: Optional[Dict[int, Joueur]] = None) -> [List[Joueur],
                                                                                                          List[
                                                                                                              Joueur]]:
        """Function to select players among acteurs's list and create new players for the tournament"""

        # Initialization
        choix_acteurs = []
        nouveaux_joueurs = []
        joueurs_du_tournoi = []

        # Header display
        affichage_menu_ajouter_joueurs = f"""
==============================
Ajouter joueurs
==============================
"""
        print(affichage_menu_ajouter_joueurs)

        if acteurs:
            # Choice of players among the acteurs
            acteurs_affichage = '''\nChoix des joueurs parmis les acteurs : '''
            for (key, acteur) in acteurs.items():
                acteurs_affichage += f'''\n{key} - {acteur.prenom} {acteur.nom_de_famille}'''
            print(acteurs_affichage)

            choix_acteurs_texte = '\nChoisissez un acteur parmis la liste en entrant son numéro ou entrez \'terminer\' lorsque vous avez terminé la selection : '
            exit_condition = False
            while not exit_condition:
                acteur_key = pvt.parse_and_validate(explanation=choix_acteurs_texte, parse=pvt.parse_string_not_empty,
                                                    validate=pvt.validate_actor_key)
                if acteur_key == 'terminer':
                    exit_condition = True
                    print(f'{len(choix_acteurs)} acteurs sélectionnés !')
                elif acteur_key not in acteurs.keys():
                    print(f'Veuillez choisir le numéro d\'un acteur présent dans la liste {acteurs.keys()}')
                else:
                    if acteurs[acteur_key] in choix_acteurs:
                        print(
                            f'Joueur {acteurs[acteur_key].prenom} {acteurs[acteur_key].nom_de_famille} déjà sélectionné XX')
                        print('\nVeuillez choisir un autre joueur.')
                    else:
                        choix_acteurs.append(acteurs[acteur_key])
                        print(
                            f'Joueur {acteurs[acteur_key].prenom} {acteurs[acteur_key].nom_de_famille} sélectionné !')
                        if len(choix_acteurs) == nb_joueurs:
                            print(f'\nNombre maximum de joueurs ({nb_joueurs}) atteint.')
                            exit_condition = True
        else:
            pass

        if len(choix_acteurs) == nb_joueurs:
            pass
        else:
            # Choice new players
            nb_joueurs = nb_joueurs - len(choix_acteurs)
            affichage_menu_ajouter_nouveaux_joueurs = f"""
==============================
Ajouter {nb_joueurs} nouveaux joueurs
==============================
"""
            print(affichage_menu_ajouter_nouveaux_joueurs)

            # Loop on remaining players to be created
            for joueur in range(1, nb_joueurs + 1):
                # Standard dictionary containing player information
                information_nouveau_joueur = {
                    'nom_de_famille': '',
                    'prenom': '',
                    'date_de_naissance': '',
                    'sexe': '',
                    'classement': ''
                }

                # Added standard dictionary to new players list
                nouveaux_joueurs.append(information_nouveau_joueur)

                # Header display pour chaque nouveau joueur
                affichage_nouveau_joueur = f"""
Renseigner les informations du joueur n°{joueur}
==========================================
                """
                print(affichage_nouveau_joueur)

                # Definition of surname
                nouveau_joueur_texte_nom = f'\nRenseignez le Nom de famille du joueur n°{joueur} : '
                nouveaux_joueurs[joueur - 1]['nom_de_famille'] = pvt.parse_and_validate(
                    explanation=nouveau_joueur_texte_nom, parse=pvt.parse_string_not_empty, validate=pvt.no_validation)

                # First name definition
                nouveau_joueur_texte_prenom = f'\nRenseignez le Prénom du joueur n°{joueur} : '
                nouveaux_joueurs[joueur - 1]['prenom'] = pvt.parse_and_validate(
                    explanation=nouveau_joueur_texte_prenom,
                    parse=pvt.parse_string_not_empty,
                    validate=pvt.no_validation)

                # Definition of date of birth
                nouveau_joueur_texte_date_naissance = f'\nRenseignez la Date de naissance du joueur n°{joueur} au format "jj/mm/aaaa" : '
                nouveaux_joueurs[joueur - 1]['date_de_naissance'] = pvt.parse_and_validate(
                    explanation=nouveau_joueur_texte_date_naissance, parse=pvt.parse_date,
                    validate=pvt.validate_date_format)

                # Definition of sex
                nouveau_joueur_texte_sexe = f'\nRenseignez le sexe du joueur n°{joueur} ("m"/"f") :'
                nouveaux_joueurs[joueur - 1]['sexe'] = pvt.parse_and_validate(explanation=nouveau_joueur_texte_sexe,
                                                                              parse=pvt.parse_string_not_empty,
                                                                              validate=pvt.validate_sexe)

                # Rank definition
                nouveau_joueur_texte_classement = f'\nRenseignez le classement du joueur n°{joueur} : '
                nouveaux_joueurs[joueur - 1]['classement'] = pvt.parse_and_validate(
                    explanation=nouveau_joueur_texte_classement, parse=pvt.parse_int,
                    validate=pvt.validate_integer_positive)

                # Formatting Player Information in Joueur Format
                nouveaux_joueurs[joueur - 1] = Joueur(**nouveaux_joueurs[joueur - 1])

                # Message
                print(
                    f'\nNouveau Joueur {nouveaux_joueurs[joueur - 1].prenom} {nouveaux_joueurs[joueur - 1].nom_de_famille} ajouté avec succès !')

        # Concatenation of acteurs and players
        joueurs_du_tournoi.extend(choix_acteurs)
        joueurs_du_tournoi.extend(nouveaux_joueurs)

        return joueurs_du_tournoi, nouveaux_joueurs

    def supprimer_joueur(self, acteurs_liste: List[Joueur]) -> Joueur:
        """Function to select a player to remove from acteurs."""

        joueur_a_supprimer = []

        if acteurs_liste:
            # Header display
            affichage_supprimer_joueur = f"""
==============================
Supprimer un Joueur
==============================
            """
            print(affichage_supprimer_joueur)

            # Choice of a player among the acteurs
            acteurs_affichage = '''\nChoix d'un joueur à supprimer parmis les acteurs : '''
            for (key, acteur) in enumerate(acteurs_liste, 1):
                acteurs_affichage += f'''\n{key} - {acteur.prenom} {acteur.nom_de_famille}'''
            print(acteurs_affichage)

            choix_acteurs_texte = '\nChoisissez un acteur parmis la liste en entrant son numéro : '
            acteur_key = pvt.parse_and_validate(explanation=choix_acteurs_texte,
                                                parse=pvt.parse_int,
                                                validate=lambda x: pvt.validate_integer_interval(parsed_int=x,
                                                                                                 interval=(
                                                                                                     1,
                                                                                                     len(acteurs_liste))))
            joueur_a_supprimer = acteurs_liste[acteur_key - 1]
            # Message
            print(
                f'\nJoueur {joueur_a_supprimer.prenom} {joueur_a_supprimer.nom_de_famille} supprimé de la liste des acteurs avec succès !')

        else:
            pass

        return joueur_a_supprimer

    def afficher_paires_joueurs(self, round_param: Round):

        nombre_de_paires = len(round_param.match_liste)

        # Header display
        affichage_paires_joueurs_entete = f"""
==========================================================
{nombre_de_paires} nouvelles paires de joueurs générées avec succès !
==========================================================
"""
        print(affichage_paires_joueurs_entete)

        # Loop to show all player pairs
        paires = 1
        for ((joueur1, score1), (joueur2, score2)) in round_param.match_liste:
            print(
                f'Paire n°{paires} : {joueur1.prenom} {joueur1.nom_de_famille} / {joueur2.prenom} {joueur2.nom_de_famille}')
            paires += 1

    def creer_nouveau_round(self, numero_round: int) -> Round:
        """Display menu creer_nouveau_round"""

        # Initialization
        nouveau_round = {
            'nom': '',
            'match_liste': [],
            'date_debut': '',
            'date_fin': ''
        }

        # Setting the Round name
        nouveau_round['nom'] = RoundName('Round ' + str(numero_round))

        # Display
        affichage_creer_nouveau_round = f'''
==============================
Création du {nouveau_round['nom'].value} avec succès !
==============================
'''
        print(affichage_creer_nouveau_round)

        # Round start date definition
        nouveau_round['date_debut'] = datetime.now()

        # Formatting the result in Round format
        nouveau_round = Round(**nouveau_round)

        return nouveau_round

    def entrer_scores(self, round_param: Round) -> List[Match]:

        # Initialization
        match_liste_scores = round_param.match_liste
        nombre_de_paires = len(match_liste_scores)

        # Diplay menu entrer scores
        affichage_menu_entrer_scores = f'''
==========================================================
Entrez/Modifiez les scores des {nombre_de_paires} matchs :  
==========================================================        
'''
        print(affichage_menu_entrer_scores)

        # Loop on matches
        for idx, ((joueur1, _), (joueur2, _)) in enumerate(match_liste_scores):
            print(f'Match n°{idx + 1} : ')
            print('Qui est le vainqueur ?')
            print(f'1. {joueur1.prenom} {joueur1.nom_de_famille}')
            print(f'2. {joueur2.prenom} {joueur2.nom_de_famille}')
            print('0. Match-Nul')
            match_texte = f'Veuillez choisir le résultat du match n°{idx + 1} (1, 2, ou 0) : '
            resultat_match = pvt.parse_and_validate(explanation=match_texte, parse=pvt.parse_int,
                                                    validate=lambda x: pvt.validate_integer_interval(parsed_int=x,
                                                                                                     interval=(0, 2)))
            # Scoring
            if resultat_match == 1:
                score_joueur1 = Score.GAGNANT
                score_joueur2 = Score.PERDANT
            elif resultat_match == 2:
                score_joueur1 = Score.PERDANT
                score_joueur2 = Score.GAGNANT
            elif resultat_match == 0:
                score_joueur1 = Score.MATCH_NUL
                score_joueur2 = Score.MATCH_NUL
            match_liste_scores[idx] = ((joueur1, score_joueur1), (joueur2, score_joueur2))

        return match_liste_scores

    def afficher_resultats(self, scores_results: List[Round]):
        """Function that shows all scores of the Tournament"""

        # Header display
        affichage_scores_entete = """
==========================================================
Affichage des scores
==========================================================
"""
        print(affichage_scores_entete)

        # Iteration on the rounds
        for round_variable in scores_results:
            # Header display per round
            affichage_round = f"""
==========================================================
Scores du round : {round_variable.nom.value}
==========================================================
"""
            print(affichage_round)

            # Iteration on all the matches of the rounds
            for ((joueur1, score_joueur1), (joueur2, score_joueur2)) in round_variable.match_liste:
                # Display scores per match
                affichage_scores_match = f"""
----------------------------------------------------------
{joueur1.prenom} {joueur1.nom_de_famille} : {score_joueur1.value} points
{joueur2.prenom} {joueur2.nom_de_famille} : {score_joueur2.value} points
"""
                print(affichage_scores_match)

    def modifier_classement(self, joueurs_classement: List[Joueur]) -> List[Joueur]:
        """Function to update players ranking"""

        # Initialization
        joueurs_ancien_classement = joueurs_classement
        joueurs_nouveau_classement = []

        # Header display
        affichage_classement_entete = """
==========================================================
Mise à jour des classements
==========================================================
Mettez à jour le classement des joueurs suivant :
"""
        print(affichage_classement_entete)

        # Tournament Player Iteration
        for joueur in joueurs_ancien_classement:
            joueur_classement_texte = f'{joueur.prenom} {joueur.nom_de_famille} / Classement actuel = {joueur.classement} --> Nouveau classement : '
            nouveau_classement = pvt.parse_and_validate(explanation=joueur_classement_texte, parse=pvt.parse_int,
                                                        validate=pvt.validate_integer_positive)
            joueur_classement_a_ajour = Joueur(nom_de_famille=joueur.nom_de_famille, prenom=joueur.prenom,
                                               date_de_naissance=joueur.date_de_naissance, sexe=joueur.sexe,
                                               classement=nouveau_classement)
            joueurs_nouveau_classement.append(joueur_classement_a_ajour)

        # Validation message
        affichage_classement_validation = """
----------------------------------------------------------
Classements mis à jour avec succès !
"""
        print(affichage_classement_validation)

        return joueurs_nouveau_classement

    def afficher_rapports(self, nom_rapport: str, donnees_rapport: List[Any]):
        """Function that shows a report"""

        # Header display
        affichage_rapport_entete = f"""
==========================================================
Affichage de la liste des {nom_rapport}
==========================================================
"""
        print(affichage_rapport_entete)

        # List display
        for idx, element in enumerate(donnees_rapport):
            print(f'{idx + 1}. {element}')

        # End of list display
        print("""
----------------------------------------------------------
""")

    def selectionner_acteur(self, acteurs_liste: List[Joueur]) -> Joueur:
        """Function to select and return a player among acteurs"""

        self.afficher_rapport_acteur_alphabetique(donnees_rapport=acteurs_liste)

        selectionner_acteur_texte = 'Sélectionnez un joueur de la liste d\'acteurs ci-dessus : '
        indice_acteur_selectionne = pvt.parse_and_validate(explanation=selectionner_acteur_texte, parse=pvt.parse_int,
                                                           validate=lambda x: pvt.validate_integer_interval(
                                                               parsed_int=x, interval=(1, len(acteurs_liste))))

        acteur_selectionne = acteurs_liste[indice_acteur_selectionne - 1]

        # Message
        print(f'\nJoueur {acteur_selectionne.prenom} {acteur_selectionne.nom_de_famille} sélectionné avec susscès !')

        return acteur_selectionne

    def format_players_data(self, data: List[Joueur]) -> List[str]:
        """Function that format players list into str list for printing in reports"""

        formatted_data = [f'{joueur.prenom} {joueur.nom_de_famille} / classement : {joueur.classement}' for
                          joueur in data]
        return formatted_data

    def afficher_rapport_acteur_alphabetique(self, donnees_rapport: List[Joueur]):
        """Function that shows an alphabetic ordered report of all actors"""

        formatted_data = self.format_players_data(data=donnees_rapport)
        self.afficher_rapports(nom_rapport='acteurs par ordre alphabétique', donnees_rapport=formatted_data)

    def afficher_rapport_acteur_classement(self, donnees_rapport: List[Joueur]):
        """Function that shows a ranking ordered report of all actors"""

        formatted_data = self.format_players_data(data=donnees_rapport)
        self.afficher_rapports(nom_rapport='acteurs par ordre de classement', donnees_rapport=formatted_data)

    def afficher_rapport_joueurs_alphabetique(self, tournoi: Tournoi, donnees_rapport: List[Joueur]) -> [str,
                                                                                                         List[str]]:
        """Function that shows a ranking ordered report of the players of a tournament"""

        formatted_data = self.format_players_data(data=donnees_rapport)
        self.afficher_rapports(nom_rapport=f'joueurs du tournoi {tournoi.nom} par ordre alphabétique',
                               donnees_rapport=formatted_data)

    def afficher_rapport_joueurs_classement(self, tournoi: Tournoi, donnees_rapport: List[Joueur]):
        """Function that shows a ranking ordered report of the players of a tournament"""

        formatted_data = self.format_players_data(data=donnees_rapport)
        self.afficher_rapports(nom_rapport=f'joueurs du tournoi {tournoi.nom} par ordre de classement',
                               donnees_rapport=formatted_data)

    def afficher_rapport_tournois(self, donnees_rapport: List[Tournoi]):
        """Function that shows a descending chronological order report or tournaments"""

        formatted_data = [
            f"Tournoi {tournoi.nom} de {tournoi.lieu} qui a débuté le : {tournoi.date_debut.strftime('%d-%m-%Y')}" for
            tournoi in donnees_rapport]
        self.afficher_rapports(nom_rapport='tournois', donnees_rapport=formatted_data)

    def afficher_rapport_tours_tournoi(self, tournoi: Tournoi, donnees_rapport: List[Round]):
        """Function that shows a report or all rounds of a tournament"""
        if not donnees_rapport:
            print(f'\nAuncun Round créé dans le Tournoi {tournoi.nom} !')
        else:
            formatted_data = [
                f"Tour {round_variable.nom.value} qui a débuté le : {round_variable.date_debut.strftime('%d-%m-%Y')}"
                for
                round_variable in donnees_rapport]
            self.afficher_rapports(nom_rapport=f'tours du tournoi {tournoi.nom}', donnees_rapport=formatted_data)

    def afficher_rapport_matchs_tournoi(self, tournoi: Tournoi, donnees_rapport: List[Match]):
        """Function that shows a report or all matchs of a tournament"""
        if not donnees_rapport:
            print(f'\nAucun match joué dans le Tournoi {tournoi.nom} !')
        else:
            formatted_data = [
                f'Match : {joueur_1.prenom} {joueur_1.nom_de_famille} // {joueur_2.prenom} {joueur_2.nom_de_famille}'
                for
                ((joueur_1, _), (joueur_2, _)) in donnees_rapport]
            self.afficher_rapports(nom_rapport=f'matchs du tournoi {tournoi.nom}', donnees_rapport=formatted_data)

    def affichage_warning(self, message: str):
        """Function to print warning messages"""
        print(f'''
x x x x x x x x x x x x x x xx
{message}
x x x x x x x x x x x x x x xx''')
