import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tinydb import TinyDB, Query, table
from core.model import Joueur, State, Tournoi
from tests.test_script import state1, state4
from core import sorters
from typing import Dict, List


def init_database():
    """Function to initialize database of the project"""
    db = TinyDB('persistence/db.json')
    db.table('players')
    db.table('tournament')


def clear_database():
    """Function to clear database"""
    try:
        db_path = 'persistence/db.json'
        os.remove(db_path)
    except FileNotFoundError:
        pass
    init_database()


def load_players() -> Dict[int, Joueur]:
    """Function to load players from database into actual state"""

    # Initalisation
    acteurs_from_db = {}
    db = TinyDB('persistence/db.json')
    # Iteration over players in db
    for element in db.table('players'):
        acteurs_from_db[element.doc_id] = Joueur.from_json(element)

    return acteurs_from_db


def save(state: State):
    """Function to save actual state to database"""

    # Initialisation
    db = TinyDB('persistence/db.json')

    # Save players
    for player_id, player_instance in state.acteurs.items():
        db.table('players').insert(table.Document(player_instance.to_json(), doc_id=player_id))

    # Save tournaments
    tournaments = state.tournois
    if state.tournoi:
        tournaments.append(state.tournoi)
    tournaments.sort(key=sorters.tournament_chronological)

    for tournoi in tournaments:
        db.table('tournaments').insert(tournoi.to_json())


if __name__ == '__main__':
    clear_database()
    init_database()
    state_to_save = state4()
    save(state=state_to_save)
