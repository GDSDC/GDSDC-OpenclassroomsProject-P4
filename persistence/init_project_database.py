import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tinydb import TinyDB, Query, table
from core.model import Joueur, State, Tournoi
from tests.test_script import state1
from core import sorters
from typing import Dict, List


def init_database():
    """Function to initialize database of the project"""
    db = TinyDB('persistence/db.json')
    db.table('players')
    db.table('tournament')


def load_players() -> Dict[int, Joueur]:
    """Function to load players from database into actual state"""

    # Initalisation
    players_table = db.table('players')
    players: List[Dict[str, Any]]
    # TODO : find a way to iterate over db.table('players') and get doc_id and document.from.json to fill acteurs dict


def save(state: State):
    """Function to save actual state to database"""

    # Initialisation
    db = TinyDB('persistence/db.json')

    # Save players
    for player_id, player_instance in state.acteurs.items():
        db.table('players').insert(table.Document(player_instance.to_json(), doc_id=player_id))

        # # Save tournaments
        # tournaments = state.tournois
        # if state.tournoi:
        #     tournaments.append(state.tournoi)
        # tournaments.sort(key=sorters.tournament_chronological)

if __name__ == '__main__':
    init_database()
    state_to_save = state1()
    save(state=state_to_save)
