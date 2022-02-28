from core.vue import Vue
from core.model import State, Joueur, Tournoi, Score, Round, NOMBRE_DE_JOUEURS
from core import persistence, sorters
from typing import List, Optional


class Controller:
    """Contrôleur principal."""

    def __init__(self, state: Optional[State] = None, vue: Optional[Vue] = None):
        """Initialise les modèles et les vues."""
        self.state = state or State()
        self.vue = vue or Vue()

    def start(self):
        must_exit = False
        while not must_exit:
            choix = self.vue.menu_principal()
            if choix == 1:
                self.afficher_menu_de_gestion_des_joueurs()
            elif choix == 2:
                self.afficher_menu_de_gestion_des_joueurs()
            elif choix == 3:
                self.afficher_menu_de_gestion_des_joueurs()
            elif choix == 4:
                self.afficher_menu_de_gestion_des_joueurs()
            elif choix == 5:
                must_exit = True

        print("Au revoir")

    # Gestion des joueurs

    # Gestion du tournoi en cours
    def create_new_tournament(self):
        nouveau_tournoi = self.vue.menu_creer_nouveau_tournoi(acteurs=self.state.acteurs)
        self.state.creer_nouveau_tournoi(nouveau_tournoi)

    def ajouter_joueurs(self, nb_joueurs: int = NOMBRE_DE_JOUEURS):
        joueurs = self.vue.ajouter_joueurs(nb_joueurs=nb_joueurs)  # en local
        self.state.ajouter_joueurs(joueurs)

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

    # Rapports
    def afficher_resultats(self):
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

    # TODO DELETE ME
    def joueurs_ordre_alphabetique(data: List[Joueur]) -> List[Joueur]:
        """Function that output a list of players ordered aalphabeticaly"""

        result = []
        result.extend(data)
        result.sort(key=lambda x: x.nom_de_famille.lower())

        return result

    # TODO DELETE ME
    def joueurs_ordre_classement(self, data: List[Joueur]) -> List[Joueur]:
        """Function that output a list of players ordered by ranking"""

        result = []
        result.extend(data)
        result.sort(key=lambda x: x.classement)

        return result

    # TODO DELETE ME
    def tournois_ordre_chronologique_descendant(self, data: List[Tournoi]) -> List[Tournoi]:
        """Function that output a list of tournaments descending chronological ordered"""

        result = []
        result.extend(data)
        result.sort(key=lambda x: x.date_debut, reverse=True)

        return result

    def rapport_acteur_alphabetique(self):
        """Function that shows an alphabetic ordered report of all actors"""
        # Report Name
        nom_rapport = 'acteurs par ordre alphabétique'

        # Ordering data
        ordered_data = sorted(self.state.acteurs.values(), key=sorters.player_alphabetical_by_lastname)

        # Formatting ordered data
        formatted_ordered_data = [f'{acteur.prenom} {acteur.nom_de_famille} / classement : {acteur.classement}' for
                                  acteur in ordered_data]
        # Showing report
        self.vue.afficher_rapport(nom_rapport=nom_rapport, donnees_rapport=formatted_ordered_data)

    def rapport_acteur_classement(self):
        """Function that shows a ranking ordered report of all actors"""
        # Report Name
        nom_rapport = 'acteurs par ordre de classement'
        # Ordering data
        ordered_data = sorted(self.state.acteurs.values(), key=sorters.player_by_ranking, reverse=True)
        # Formatting ordered data
        formatted_ordered_data = [f'{acteur.prenom} {acteur.nom_de_famille} / classement : {acteur.classement}' for
                                  acteur in ordered_data]
        # Showing report
        self.vue.afficher_rapport(nom_rapport=nom_rapport, donnees_rapport=formatted_ordered_data)

    def rapport_joueurs_alphabetique(self, tournoi: Tournoi):
        """Function that shows an alphabetic ordered report of the players of a tournament"""
        # Report Name
        nom_rapport = f'joueurs du tournoi {tournoi.nom} par ordre alphabétique'
        # Ordering data
        ordered_data = self.joueurs_ordre_alphabetique(tournoi.joueurs_du_tournoi)
        # Formatting ordered data
        formatted_ordered_data = [f'{joueur.prenom} {joueur.nom_de_famille} / classement : {joueur.classement}' for
                                  joueur in ordered_data]
        # Showing report
        self.vue.afficher_rapport(nom_rapport=nom_rapport, donnees_rapport=formatted_ordered_data)

    def rapport_joueurs_classement(self, tournoi: Tournoi):
        """Function that shows a ranking ordered report of the players of a tournament"""
        # Report Name
        nom_rapport = f'joueurs du tournoi {tournoi.nom} par ordre de classement'
        # Ordering data
        ordered_data = self.joueurs_ordre_classement(tournoi.joueurs_du_tournoi)
        # Formatting ordered data
        formatted_ordered_data = [f'{joueur.prenom} {joueur.nom_de_famille} / classement : {joueur.classement}' for
                                  joueur in ordered_data]
        # Showing report
        self.vue.afficher_rapport(nom_rapport=nom_rapport, donnees_rapport=formatted_ordered_data)

    def exporter_rapport_tournois(self):
        """Function that shows a descending chronological order report or tournaments"""
        # Order data
        ordered_data = self.tournois_ordre_chronologique_descendant(self.state.tournois)

        self.vue.display_tournaments_report(ordered_data)

    def rapport_tours_tournoi(self, tournoi: Tournoi):
        """Function that shows a report or all rounds of a tournament"""
        # Report Name
        nom_rapport = f'tours du tournoi {tournoi.nom}'
        # Ordering data
        ordered_data = tournoi.rounds
        # Formatting ordered data
        formatted_ordered_data = [f'Tour {round.nom.value} qui a débuté le : {round.date_debut}' for
                                  round in ordered_data]
        # Showing report
        self.vue.afficher_rapport(nom_rapport=nom_rapport, donnees_rapport=formatted_ordered_data)

    def rapport_matchs_tournoi(self, tournoi: Tournoi):
        """Function that shows a report or all matchs of a tournament"""
        # Report Name
        nom_rapport = f'matchs du tournoi {tournoi.nom}'
        # Ordering data
        ordered_data = []
        for round in tournoi.rounds:
            for match in round.match_liste:
                ordered_data.append(match)
        # ordered_data = [match in round.match_liste for round in tournoi.rounds]
        # Formatting ordered data
        formatted_ordered_data = [
            f'Match : {joueur_1.prenom} {joueur_1.nom_de_famille} // {joueur_2.prenom} {joueur_2.nom_de_famille}' for
            ((joueur_1, _), (joueur_2, _)) in ordered_data]
        # Showing report
        self.vue.afficher_rapport(nom_rapport=nom_rapport, donnees_rapport=formatted_ordered_data)

    # Gestion de la base de données
    def load(self):
        players = persistence.load_players()
        tournaments = persistence.load_tournaments()

        state = State(acteurs=players, tournois=tournaments)
        self.state = state

    def save(self):
        persistence.save(self.state)


if __name__ == '__main__':
    pass
