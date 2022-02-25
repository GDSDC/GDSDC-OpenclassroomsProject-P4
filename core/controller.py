from core.vue import Vue
from core.model import State, Joueur, Tournoi, Score, Round, NOMBRE_DE_JOUEURS
from typing import List, Optional


class Controller:
    """Contrôleur principal."""

    def __init__(self, state: Optional[State] = None, vue: Optional[Vue] = None):
        """Initialise les modèles et les vues."""
        self.state = state or State()
        self.vue = vue or Vue()

    def creer_nouveau_tournoi(self):
        nouveau_tournoi = self.vue.menu_creer_nouveau_tournoi()
        self.state.creer_nouveau_tournoi(nouveau_tournoi)

    def ajouter_joueurs(self, nb_joueurs: Optional[int] = NOMBRE_DE_JOUEURS):
        joueurs = self.vue.ajouter_joueurs(nb_joueurs=nb_joueurs)
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

    def joueurs_ordre_alphabetique(self, data: List[Joueur]) -> List[Joueur]:
        """Function that output a list of players ordered aalphabeticaly"""

        result = []
        result.extend(data)
        result.sort(key=lambda x: x.nom_de_famille.lower())

        return result

    def joueurs_ordre_classement(self, data: List[Joueur]) -> List[Joueur]:
        """Function that output a list of players ordered by ranking"""

        result = []
        result.extend(data)
        result.sort(key=lambda x: x.classement)

        return result

    def rapport_acteur_alphabetique(self):
        """Function that shows an alphabetic ordered report of all actors"""

        # Report nam
        nom_rapport = 'acteurs par ordre alphabétique'
        ordered_data = self.joueurs_ordre_alphabetique(data=list(self.state.acteurs.values()))
        self.vue.afficher_rapports(nom_rapport=nom_rapport, donnees_rapport=ordered_data)

    def rapport_acteur_classement(self):
        """Function that shows a ranking ordered report of all actors"""

        # Report nam
        nom_rapport = 'acteurs par ordre de classement'
        ordered_data = self.joueurs_ordre_classement(data=list(self.state.acteurs.values()))
        self.vue.afficher_rapports(nom_rapport=nom_rapport, donnees_rapport=ordered_data)

    def rapport_joueurs_alphabetique(self):
        """Function that shows an alphabetic ordered report of players"""

        # Report nam
        nom_rapport = 'joueurs du tournoi par ordre alphabétique'
        ordered_data = self.joueurs_ordre_alphabetique(self.state.tournoi.joueurs_du_tournoi)
        self.vue.afficher_rapports(nom_rapport=nom_rapport, donnees_rapport=ordered_data)

    def rapport_joueurs_classement(self):
        """Function that shows a ranking ordered report of all actors"""

        # Report nam
        nom_rapport = 'joueurs par ordre de classement'
        ordered_data = self.joueurs_ordre_classement(self.state.tournoi.joueurs_du_tournoi)
        self.vue.afficher_rapports(nom_rapport=nom_rapport, donnees_rapport=ordered_data)


if __name__ == '__main__':
    pass
