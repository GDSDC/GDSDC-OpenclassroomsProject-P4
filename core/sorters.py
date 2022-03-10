from core.model import Joueur, Tournoi

# Functions to help sorting process

def player_alphabetical_by_lastname(player: Joueur):
    return player.nom_de_famille.lower()


def player_by_ranking(player: Joueur):
    return player.classement


def tournament_chronological(tournament: Tournoi):
    return tournament.date_debut
