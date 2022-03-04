from core.vue import Vue, CHOIX_MENU_PRINCIPAL, CHOIX_MENU_TOURNOI, CHOIX_MENU_RAPPORTS, CHOIX_MENU_JOUEURS
from core.model import State, Joueur, Tournoi, Score, Round, NOMBRE_DE_JOUEURS
from typing import List, Optional
from core import sorters


class Controller:
    """Contrôleur principal."""

    def __init__(self, state: Optional[State] = None, vue: Optional[Vue] = None):
        """Initialise les modèles et les vues."""
        self.state = state or State()
        self.vue = vue or Vue()

    def start(self):
        must_exit = False
        while not must_exit:

            # Menu Principal
            choix_menu_principal = self.vue.afficher_menu(nom_menu='Menu Principal', menu=CHOIX_MENU_PRINCIPAL)

            # Gestion des Joueurs
            if choix_menu_principal == 1:
                must_exit_players = False
                while not must_exit_players:
                    choix_menu_joueurs = self.vue.afficher_menu(nom_menu=CHOIX_MENU_PRINCIPAL[1],
                                                                menu=CHOIX_MENU_JOUEURS)
                    # Afficher liste des Joueurs
                    if choix_menu_joueurs == 1:
                        self.afficher_rapport_acteur_alphabetique()
                    # Ajouter nouveau Joueur
                    elif choix_menu_joueurs == 2:
                        self.ajouter_nouveau_joueur()
                    # Supprimer Joueur
                    elif choix_menu_joueurs == 3:
                        self.supprimer_joueur()
                    # MAJ classement d'un Joueur
                    elif choix_menu_joueurs == 4:
                        self.modifier_classement()
                    # Quitter
                    elif choix_menu_joueurs == 0:
                        must_exit_players = True


            # Gestion du Tournoi
            elif choix_menu_principal == 2:
                must_exit_tournament = False
                while not must_exit_tournament:
                    choix_menu_tournoi = self.vue.afficher_menu(nom_menu=CHOIX_MENU_PRINCIPAL[2],
                                                                menu=CHOIX_MENU_TOURNOI)
                    # Créer un nouveau tournoi
                    if choix_menu_tournoi == 1:
                        self.creer_nouveau_tournoi()
                    # Démarrer nouveau Round
                    elif choix_menu_tournoi == 2:
                        if self.state.tournoi:
                            self.creer_nouveau_round()
                        else:
                            print('\nVeuillez créer un Tournoi avant de démarrer un nouveau Round.')
                    # Entrer les résultats
                    elif choix_menu_tournoi == 3:
                        if self.state.tournoi:
                            if self.state.tournoi.rounds:
                                self.entrer_scores()
                            else:
                                print('\nVeuillez démarrer un nouveau Round avant d\'entrer les scores.')
                        else:
                            print(
                                '\nVeuillez créer un Tournoi et démarrer un nouveau Round avant d\'entrer les scores.')

                    # MAJ classement des Joueurs du Tournoi
                    elif choix_menu_tournoi == 4:
                        if self.state.tournoi:
                            self.modifier_classement_tournoi()
                        else:
                            print('\nVeuillez créer un Tournoi avant de modifier le classement de ses Joueurs.')
                    # Terminer Tournoi
                    elif choix_menu_tournoi == 5:
                        if self.state.tournoi:
                            self.terminer_tournoi()
                        else:
                            print('\nVeuillez créer un Tournoi avant de le terminer.')
                    # Quitter
                    elif choix_menu_tournoi == 0:
                        must_exit_tournament = True

            # Rapports
            elif choix_menu_principal == 3:
                must_exit_rapports = False
                while not must_exit_rapports:
                    choix_menu_rapports = self.vue.afficher_menu(nom_menu=CHOIX_MENU_PRINCIPAL[3],
                                                                 menu=CHOIX_MENU_RAPPORTS)
                    # Acteurs par ordre alphabétique
                    if choix_menu_rapports == 1:
                        self.afficher_rapport_acteur_alphabetique()
                    # Acteurs par par classement
                    elif choix_menu_rapports == 2:
                        self.afficher_rapport_acteur_classement()
                    # Joueurs d'un Tournoi par ordre alphabétique
                    elif choix_menu_rapports == 3:
                        tournoi_selectionne = self.selectionner_tournoi()
                        self.afficher_rapport_joueurs_alphabetique(tournoi=tournoi_selectionne)
                    # Joueurs d'un Tournoi par classement
                    elif choix_menu_rapports == 4:
                        tournoi_selectionne = self.selectionner_tournoi()
                        self.afficher_rapport_joueurs_classement(tournoi=tournoi_selectionne)
                    # Tournois
                    elif choix_menu_rapports == 5:
                        self.afficher_rapport_tournois()
                    # Tours d'un Tournoi
                    elif choix_menu_rapports == 6:
                        tournoi_selectionne = self.selectionner_tournoi()
                        self.afficher_rapport_tours_tournoi(tournoi=tournoi_selectionne)
                    # Matchs d'un Tournoi
                    elif choix_menu_rapports == 7:
                        tournoi_selectionne = self.selectionner_tournoi()
                        self.afficher_rapport_matchs_tournoi(tournoi=tournoi_selectionne)
                    # Quitter
                    elif choix_menu_rapports == 0:
                        must_exit_rapports = True

            elif choix_menu_principal == 4:
                pass
            # Quitter
            elif choix_menu_principal == 0:
                must_exit = True

    # Gestion des joueurs

    def ajouter_nouveau_joueur(self):
        """Function to add a player to acteurs"""
        nouveau_joueur = self.vue.ajouter_joueurs(nb_joueurs=1)
        self.state.ajouter_nouveau_joueur(nouveau_joueur[0])

    def supprimer_joueur(self):
        """Function to remove a player from acteurs"""
        # Order data
        acteurs_liste = list(self.state.acteurs.values())
        acteurs_liste_ordered = sorted(acteurs_liste, key=sorters.player_alphabetical_by_lastname)
        joueur_a_supprimer = self.vue.supprimer_joueur(acteurs_liste=acteurs_liste_ordered)
        self.state.supprimer_joueur(joueur_a_supprimer=joueur_a_supprimer)

        # Gestion du tournoi

    def creer_nouveau_tournoi(self):
        nouveau_tournoi = self.vue.menu_creer_nouveau_tournoi(acteurs=self.state.acteurs)
        self.state.creer_nouveau_tournoi(nouveau_tournoi)

    def selectionner_tournoi(self) -> Tournoi:
        """Function to select a Tournament among old Tournament and the actual"""
        # Order data
        ordered_tournois = sorted(self.obtenir_liste_tournois(), key=sorters.tournament_chronological, reverse=True)
        # Select Tournament in list
        tournoi_selectionne = self.vue.selectionner_tournoi(tournois=ordered_tournois)
        return tournoi_selectionne

    def obtenir_liste_tournois(self) -> List[Tournoi]:
        """Function to get all Tournaments (old and actual) in one list"""
        # Get Tournaments list
        tournois = []
        # Old Tournaments
        tournois.extend(self.state.tournois)
        # Actual Tournament
        if self.state.tournoi:
            tournois.append(self.state.tournoi)
        return tournois

    def mettre_a_jour_joueurs(self):
        """ Generation of new state.tournoi.joueurs_en_jeux list"""
        # Initialisation
        joueurs_qui_passent_au_prochain_tour = []
        # In case it is the very first round of Tournament
        if not self.state.tournoi.rounds:
            joueurs_qui_passent_au_prochain_tour.extend(self.state.tournoi.joueurs_du_tournoi)
        else:
            # Iteration sur tous les résultats de tous les matchs du précédent Round
            for match in self.state.tournoi.rounds[-1].match_liste:
                for (joueur, score) in match:
                    if score != Score.PERDANT:
                        joueurs_qui_passent_au_prochain_tour.append(joueur)
        self.state.tournoi.joueurs_en_jeux = joueurs_qui_passent_au_prochain_tour

    def creer_nouveau_round(self):
        self.mettre_a_jour_joueurs()
        numero_round = len(self.state.tournoi.rounds) + 1
        nouveau_round = self.vue.creer_nouveau_round(numero_round=numero_round)
        self.state.creer_nouveau_round(nouveau_round)
        self.generer_paires_joueurs()

    def generer_paires_joueurs(self):
        self.state.generer_paires_joueurs(self.state.tournoi.joueurs_en_jeux)
        self.vue.afficher_paires_joueurs(self.state.tournoi.rounds[-1])

    def entrer_scores(self):
        scores = self.vue.entrer_scores(round_param=self.state.tournoi.rounds[-1])
        self.state.entrer_scores(scores)

    def afficher_resultats_tournoi(self):
        """Function that shows all scores of the Tournament"""
        # Initialisation
        scores_results = []
        # Appending round_list if not empty
        if not self.state.tournoi.rounds:
            pass
        else:
            # In case actual round is the Round 1
            if len(self.state.tournoi.rounds) == 1:
                pass
            else:
                scores_results.extend(self.state.tournoi.rounds[:-1])
            # Updating scores with actual round
            for ((joueur1, score_joueur1), (joueur2, score_joueur2)) in self.state.tournoi.rounds[-1].match_liste:
                if (score_joueur1 is None) and (score_joueur2 is None):
                    pass
                else:
                    scores_results.append(self.state.tournoi.rounds[-1])
                    break
        self.vue.afficher_resultats(scores_results)

    def modifier_classement_tournoi(self):
        """Function to update players ranking in a Tournament"""
        self.afficher_resultats_tournoi()
        joueurs_classement = self.vue.modifier_classement(joueurs_classement=self.state.tournoi.joueurs_du_tournoi)
        self.state.modifier_classement_tournoi(joueurs_classement)

    def modifier_classement(self):
        """Function to update players ranking in acteurs"""
        acteurs_ordered_liste = sorted(list(self.state.acteurs.values()), key=sorters.player_alphabetical_by_lastname)
        joueur_classement = self.vue.selectionner_acteur(acteurs_liste=acteurs_ordered_liste)
        joueur_nouveau_classement = self.vue.modifier_classement(joueurs_classement=[joueur_classement])[0]
        self.state.modifier_classement(joueur_classement=joueur_nouveau_classement)

    def terminer_tournoi(self):
        """Function to close tournament"""

        # Send Sate to database

        # Message
        print(f'\nTournoi {self.state.tournoi.nom} terminé avec succès !')

        # Init the actual instance
        self.__init__()

    # Rapports
    def afficher_rapport_acteur_alphabetique(self):
        """Function that shows an alphabetic ordered report of all actors"""
        # Order data
        ordered_data = sorted(self.state.acteurs.values(), key=sorters.player_alphabetical_by_lastname)
        # Showing report
        self.vue.afficher_rapport_acteur_alphabetique(donnees_rapport=ordered_data)

    def afficher_rapport_acteur_classement(self):
        """Function that shows a ranking ordered report of all actors"""
        # Order data
        ordered_data = sorted(self.state.acteurs.values(), key=sorters.player_by_ranking)
        # Showing report
        self.vue.afficher_rapport_acteur_classement(donnees_rapport=ordered_data)

    def afficher_rapport_joueurs_alphabetique(self, tournoi: Tournoi):
        """Function that shows an alphabetic ordered report of the players of a tournament"""
        # Ordering data
        ordered_data = sorted(tournoi.joueurs_du_tournoi, key=sorters.player_alphabetical_by_lastname)
        # Showing report
        self.vue.afficher_rapport_joueurs_alphabetique(tournoi=tournoi, donnees_rapport=ordered_data)

    def afficher_rapport_joueurs_classement(self, tournoi: Tournoi):
        """Function that shows a ranking ordered report of the players of a tournament"""
        # Order data
        ordered_data = sorted(tournoi.joueurs_du_tournoi, key=sorters.player_by_ranking)
        # Showing report
        self.vue.afficher_rapport_joueurs_classement(tournoi=tournoi, donnees_rapport=ordered_data)

    def afficher_rapport_tournois(self):
        """Function that shows a descending chronological order report or tournaments"""
        # Order data
        ordered_data = sorted(self.obtenir_liste_tournois(), key=sorters.tournament_chronological, reverse=True)
        # Showing report
        self.vue.afficher_rapport_tournois(donnees_rapport=ordered_data)

    def afficher_rapport_tours_tournoi(self, tournoi: Tournoi):
        """Function that shows a report or all rounds of a tournament"""
        # Order data
        ordered_data = tournoi.rounds
        # Showing report
        self.vue.afficher_rapport_tours_tournoi(tournoi=tournoi, donnees_rapport=ordered_data)

    def afficher_rapport_matchs_tournoi(self, tournoi: Tournoi):
        """Function that shows a report or all matchs of a tournament"""
        # Order data
        ordered_data = []
        for round_variable in tournoi.rounds:
            for match in round_variable.match_liste:
                ordered_data.append(match)
        # Showing report
        self.vue.afficher_rapport_matchs_tournoi(tournoi=tournoi, donnees_rapport=ordered_data)

    # Gestion de la base de données


if __name__ == '__main__':
    pass
