from core.vue import Vue, CHOIX_MENU_PRINCIPAL, CHOIX_MENU_TOURNOI
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
                pass
                # TODO : créer menu Joueurs

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
                        self.creer_nouveau_round()
                    # Entrer les résultats
                    elif choix_menu_tournoi == 3:
                        self.entrer_scores()
                    # Terminer Tournoi
                    elif choix_menu_tournoi == 4:
                        self.terminer_tournoi()
                    # Quitter
                    elif choix_menu_tournoi == 5:
                        must_exit_tournament = True
            elif choix_menu_principal == 3:
                pass
            elif choix_menu_principal == 4:
                pass
            elif choix_menu_principal == 5:
                must_exit = True

    # Gestion des joueurs

    # Gestion du tournoi

    def creer_nouveau_tournoi(self):
        nouveau_tournoi = self.vue.menu_creer_nouveau_tournoi(acteurs=self.state.acteurs)
        self.state.creer_nouveau_tournoi(nouveau_tournoi)

    # def ajouter_joueurs(self, nb_joueurs: Optional[int] = NOMBRE_DE_JOUEURS):
    #     joueurs = self.vue.ajouter_joueurs(nb_joueurs=nb_joueurs)
    #     self.state.ajouter_joueurs(joueurs)

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

    def generer_paires_joueurs(self):
        self.state.generer_paires_joueurs(self.state.tournoi.joueurs_en_jeux)
        self.vue.afficher_paires_joueurs(self.state.tournoi.rounds[-1])

    def entrer_scores(self):
        scores = self.vue.entrer_scores(round=self.state.tournoi.rounds[-1])
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

    def modifier_classement(self):
        """Function to update players ranking"""
        joueurs_classement = self.vue.modifier_classement(joueurs_classement=self.state.tournoi.joueurs_du_tournoi)
        self.state.modifier_classement(joueurs_classement)

    def terminer_tournoi(self):
        """Function to close tournament"""

        # Send Sate to database

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
        ordered_data = sorted(self.state.tournois, key=sorters.tournament_chronological, reverse=True)
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
        for round in tournoi.rounds:
            for match in round.match_liste:
                ordered_data.append(match)
        # Showing report
        self.vue.afficher_rapport_matchs_tournoi(tournoi=tournoi, donnees_rapport=ordered_data)

    # Gestion de la base de données


if __name__ == '__main__':
    pass
