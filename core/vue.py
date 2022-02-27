from typing import List, Optional, Any, Dict
from datetime import date, datetime

from core.model import Joueur, Tournoi, Score, Round, RoundName, Match
from core import parse_validate_tools as pvt

# Constantes Globales
CHOIX_MENU_PRINCIPAL = {1: 'Créer un nouveau tournoi',
                        2: 'Ajouter huit joueurs',
                        3: 'Démarrer nouveau Round',
                        4: 'Entrer les résultats',
                        5: 'Terminer le tournoi',
                        6: 'Quitter'}


class Vue:
    """Classe qui gère l'interface/menu du programme."""

    def menu_principal(self) -> int:
        """Affichage du menu principal et récupération du choix de l'utilisateur."""

        # Affichage de l'entête
        affichage_menu_principal = """
==============================
Menu Principal
==============================
"""
        print(affichage_menu_principal)

        # Affichage des différents choix
        for choix in CHOIX_MENU_PRINCIPAL.keys():
            print(choix, '--', CHOIX_MENU_PRINCIPAL[choix])

        # Choix du menu
        choix_du_menu_texte = '\nRenseignez votre choix parmis les propositions ci-dessus (1 à ' + str(
            len(CHOIX_MENU_PRINCIPAL)) + ') : '
        choix_utilisateur_menu_principal = pvt.parse_and_validate(explanation=choix_du_menu_texte, parse=pvt.parse_int,
                                                                  validate=pvt.validate_integer_interval)

        return choix_utilisateur_menu_principal

    def menu_creer_nouveau_tournoi(self, acteurs: Dict[int, Joueur]) -> Tournoi:
        """Création d'un nouveau tournoi en renseignant toutes les informations demandées."""

        # Initialisation
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

        # Affichage de l'entête
        affichage_menu_creer_nouveau_tournoi = """
==============================
Créer un nouveau Tournoi
==============================
"""
        print(affichage_menu_creer_nouveau_tournoi)

        # Définition du nom du tournoi
        nouveau_tournoi_texte_nom = '\nRenseignez le Nom du tournoi : '
        nouveau_tournoi['nom'] = pvt.parse_and_validate(explanation=nouveau_tournoi_texte_nom,
                                                        parse=pvt.parse_string_not_empty,
                                                        validate=pvt.no_validation)

        # Définition du le lieu du tournoi
        nouveau_tournoi_texte_lieu = '\nRenseignez le Lieu du tournoi : '
        nouveau_tournoi['lieu'] = pvt.parse_and_validate(explanation=nouveau_tournoi_texte_lieu,
                                                         parse=pvt.parse_string_not_empty,
                                                         validate=pvt.no_validation)

        # Définition date de début de tournoi
        nouveau_tournoi['date_debut'] = date.today()

        # Définition date de fin de tournoi par defaut
        # nouveau_tournoi['date_fin'] = date.today()

        # Définition le contrôle du temps
        nouveau_tournoi_texte_controle_du_temps = '\nRenseignez le contrôle du temps ("bullet", "blitz" ou "coup rapide") : '
        nouveau_tournoi['controle_du_temps'] = pvt.parse_and_validate(
            explanation=nouveau_tournoi_texte_controle_du_temps, parse=pvt.parse_string_not_empty,
            validate=pvt.validate_controle_du_temps)

        # Description
        nouveau_tournoi_texte_description = '\nRensignez les remarques générales du directeur du tournoi : '
        nouveau_tournoi['description'] = pvt.parse_and_validate(explanation=nouveau_tournoi_texte_description,
                                                                parse=pvt.parse_string_not_empty,
                                                                validate=pvt.no_validation)

        # Choix des joueurs parmis les acteurs
        acteurs_affichage = '''\n Choix des joueurs parmis les acteurs : '''
        for (key, acteur) in acteurs.items():
            acteurs_affichage += f'''\n{key} - {acteur.prenom} {acteur.nom_de_famille}'''
        print(acteurs_affichage)

        choix_acteurs_texte = '\nChoisissez un acteur parmis la liste en entrant son numéro ou entrez \'terminer\' lorsque vous avez terminé la la selection : '
        exit_condition = False
        while not exit_condition:
            acteur_key = pvt.parse_and_validate(explanation=choix_acteurs_texte, parse=pvt.parse_string_not_empty, validate=pvt.validate_actor_key)
            if acteur_key == 'terminer':
                exit_condition = True
            elif acteur_key not in acteurs.keys():
                print(f'Veuillez choisir le numéro d\'un acteur présent dans la liste {acteurs.keys()}')
            else:
                nouveau_tournoi['joueurs_du_tournoi'].append(acteurs[acteur_key])

        # Ajout de nouveaux joueurs
        # TODO : ajouter ici la possibilité d'appeler la fonction ajouter_joueurs pour ajouter un joueur à la fois


        # Formatage du resultat au format Tournoi
        nouveau_tournoi = Tournoi(**nouveau_tournoi)

        return nouveau_tournoi

    def ajouter_joueurs(self, nb_joueurs: Optional[int]) -> List[Joueur]:
        """AJout des informations de huit joueurs dans une liste de dictionnaires à destination du Controller."""

        # Initialisation
        # liste retournée contenant les informations des huit joueurs
        nouveaux_joueurs = []

        # Affichage de l'entête
        affichage_menu_ajouter_joueurs = f"""
==============================
Ajouter {nb_joueurs} joueurs
==============================
"""
        print(affichage_menu_ajouter_joueurs)

        # Boucle sur les huits joueurs
        for joueur in range(1, nb_joueurs + 1):
            # dictionnaire type contenant les informations d'un joueur
            information_nouveau_joueur = {
                'nom_de_famille': '',
                'prenom': '',
                'date_de_naissance': '',
                'sexe': '',
                'classement': ''
            }

            # ajout du dictionnaire type à la liste de nouveaux joueurs
            nouveaux_joueurs.append(information_nouveau_joueur)

            # Affichage de l'entête pour chaque nouveau joueur
            affichage_nouveau_joueur = f"""
Renseigner les informations du joueur n°{joueur}
==========================================
            """
            print(affichage_nouveau_joueur)

            # Définition du nom de famille
            nouveau_joueur_texte_nom = f'\nRenseignez le Nom de famille du joueur n°{joueur} : '
            nouveaux_joueurs[joueur - 1]['nom_de_famille'] = pvt.parse_and_validate(
                explanation=nouveau_joueur_texte_nom, parse=pvt.parse_string_not_empty, validate=pvt.no_validation)

            # Définition le prénom
            nouveau_joueur_texte_prenom = f'\nRenseignez le Prénom du joueur n°{joueur} : '
            nouveaux_joueurs[joueur - 1]['prenom'] = pvt.parse_and_validate(
                explanation=nouveau_joueur_texte_prenom,
                parse=pvt.parse_string_not_empty,
                validate=pvt.no_validation)

            # Définition de la date de naissance
            nouveau_joueur_texte_date_naissance = f'\nRenseignez la Date de naissance du joueur n°{joueur} au format "jj/mm/aaaa" : '
            nouveaux_joueurs[joueur - 1]['date_de_naissance'] = pvt.parse_and_validate(
                explanation=nouveau_joueur_texte_date_naissance, parse=pvt.parse_date,
                validate=pvt.validate_date_format)

            # Définition du sexe
            nouveau_joueur_texte_sexe = f'\nRenseignez le sexe du joueur n°{joueur} ("m"/"f") :'
            nouveaux_joueurs[joueur - 1]['sexe'] = pvt.parse_and_validate(explanation=nouveau_joueur_texte_sexe,
                                                                          parse=pvt.parse_string_not_empty,
                                                                          validate=pvt.validate_sexe)

            # Définition du classement
            nouveau_joueur_texte_classement = f'\nRenseignez le classement du joueur n°{joueur} : '
            nouveaux_joueurs[joueur - 1]['classement'] = pvt.parse_and_validate(
                explanation=nouveau_joueur_texte_classement, parse=pvt.parse_int,
                validate=pvt.validate_integer_positive)

            # Formatage des informations de joueurs au format Joueur
            nouveaux_joueurs[joueur - 1] = Joueur(**nouveaux_joueurs[joueur - 1])

        return nouveaux_joueurs

    def afficher_paires_joueurs(self, round: Round):

        nombre_de_paires = len(round.match_liste)

        # Affichage de l'entête
        affichage_paires_joueurs_entete = f"""
==========================================================
{nombre_de_paires} nouvelles paires de joueurs générées avec succès !
==========================================================
"""
        print(affichage_paires_joueurs_entete)

        # Boucle pour afficher toutes les paires de joueurs
        paires = 1
        for ((joueur1, score1), (joueur2, score2)) in round.match_liste:
            print(
                f'Paire n°{paires} : {joueur1.prenom} {joueur1.nom_de_famille} / {joueur2.prenom} {joueur2.nom_de_famille}')
            paires += 1

    def creer_nouveau_round(self, numero_round: int) -> Round:
        """Affichage menu creer_nouveau_round"""

        # Initialisation
        nouveau_round = {
            'nom': '',
            'match_liste': [],
            'date_debut': '',
            'date_fin': ''
        }

        # Définition du nom du Round
        nouveau_round['nom'] = RoundName('Round ' + str(numero_round))

        # Affichage
        affichage_creer_nouveau_round = f'''
==============================
Création du {nouveau_round['nom'].value} avec succès !
==============================
'''
        print(affichage_creer_nouveau_round)

        # Définition date de début de round
        nouveau_round['date_debut'] = datetime.today()

        # Formatage du resultat au format Round
        nouveau_round = Round(**nouveau_round)

        return nouveau_round

    def entrer_scores(self, round: Round) -> List[Match]:

        # Initialisation
        match_liste_scores = round.match_liste
        nombre_de_paires = len(match_liste_scores)

        # Affichage menu entrer scores
        affichage_menu_entrer_scores = f'''
==========================================================
Entrez les scores des {nombre_de_paires} matchs :  
==========================================================        
'''
        print(affichage_menu_entrer_scores)

        # Boucle sur les matchs
        for idx, ((joueur1, _), (joueur2, _)) in enumerate(match_liste_scores):
            print(f'Match n°{idx + 1} : ')
            print('Qui est le vainqueur ?')
            print(f'1. {joueur1.prenom} {joueur1.nom_de_famille}')
            print(f'2. {joueur2.prenom} {joueur2.nom_de_famille}')
            print('3. Match-Nul')
            match_texte = f'Veuillez choisir le résultat du match n°{idx + 1} (1, 2, ou 3) : '
            resultat_match = pvt.parse_and_validate(explanation=match_texte, parse=pvt.parse_int,
                                                    validate=pvt.validate_score)
            # Score attribution
            if resultat_match == 1:
                score_joueur1 = Score.GAGNANT
                score_joueur2 = Score.PERDANT
            elif resultat_match == 2:
                score_joueur1 = Score.PERDANT
                score_joueur2 = Score.GAGNANT
            else:
                score_joueur1 = Score.MATCH_NUL
                score_joueur2 = Score.MATCH_NUL
            match_liste_scores[idx] = ((joueur1, score_joueur1), (joueur2, score_joueur2))

        return match_liste_scores

    def afficher_resultats(self, scores_results: List[Round]):
        """Function that shows all scores of the Tournament"""

        # Affichage de l'entête
        affichage_scores_entete = """
==========================================================
Affichage des scores
==========================================================
"""
        print(affichage_scores_entete)

        # Iteration sur les rounds
        for round in scores_results:
            # Affichage entête par round
            affichage_round = f"""
==========================================================
Scores du round : {round.nom.value}
==========================================================
"""
            print(affichage_round)

            # Iteration sur tous les matchs du rounds
            for ((joueur1, score_joueur1), (joueur2, score_joueur2)) in round.match_liste:
                # Affichage scores par match
                affichage_scores_match = f"""
----------------------------------------------------------
{joueur1.prenom} {joueur1.nom_de_famille} : {score_joueur1.value} points
{joueur2.prenom} {joueur2.nom_de_famille} : {score_joueur2.value} points
"""
                print(affichage_scores_match)

    def modifier_classement(self, joueurs_classement: List[Joueur]) -> List[Joueur]:
        """Function to update players ranking"""

        # Initialisation
        joueurs_classement_updated = joueurs_classement

        # Affichage de l'entête
        affichage_classement_entete = """
==========================================================
Mise à jour des scores
==========================================================
Mettez à jour les scores des joueurs suivant :
"""
        print(affichage_classement_entete)

        # Iteration sur les joueurs du tournoi
        for joueur in joueurs_classement_updated:
            joueur_classement_texte = f'{joueur.prenom} {joueur.nom_de_famille} / Classement actuel = {joueur.classement} --> Nouveau classement : '
            nouveau_classement = pvt.parse_and_validate(explanation=joueur_classement_texte, parse=pvt.parse_int,
                                                        validate=pvt.validate_integer_positive)
            joueur.classement = nouveau_classement

        # Message Validation
        affichage_classement_validation = """
----------------------------------------------------------
Classements mis à jour avec succès !
"""
        print(affichage_classement_validation)

        return joueurs_classement_updated

    def afficher_rapports(self, nom_rapport: str, donnees_rapport: List[Any]):
        """Function that shows a report"""

        # Affichage de l'entête
        affichage_rapport_entete = f"""
==========================================================
Affichage de la liste des {nom_rapport}
==========================================================
"""
        print(affichage_rapport_entete)

        # Affichage de la liste
        for idx, element in enumerate(donnees_rapport):
            print(f'{idx + 1}. {element}')

        # Affichage fin de liste
        print("""
----------------------------------------------------------
""")


if __name__ == '__main__':
    pass
