import os

from tinydb import TinyDB, Query, table
from core.model import Joueur, State, Tournoi
from tests.test_script import state1, state4
from core import sorters
from typing import Dict, List, Optional
from functools import wraps

_DB_PATH = 'resources/db.json'

DB: Optional[TinyDB] = None

PLAYERS_TABLE = 'players'
TOURNAMENTS_TABLE = 'tournaments'


def open_database(path: str = _DB_PATH) -> TinyDB:
    print("Opening connection to DB")
    return TinyDB(path)


def init_database(db: TinyDB):
    """Function to initialize database of the project"""
    print("Initializing DB tables")
    db.table(PLAYERS_TABLE)
    db.table(TOURNAMENTS_TABLE)
    print("Done!")


def clear_database():
    """Function to clear database"""
    try:
        print("Dropping DB")
        os.remove(_DB_PATH)
    except FileNotFoundError:
        pass
    global DB
    DB = open_database()
    init_database(DB)


def _ensure_db_is_loaded():
    global DB
    if DB is None:
        DB = open_database()
    else:
        print("DB is already opened")


def with_db(f):
    @wraps(f)
    def wrapper(**kargs):
        _ensure_db_is_loaded()
        return f(**kargs)

    return wrapper


@with_db
def load_players() -> Dict[int, Joueur]:
    """Function to load players from database into actual state"""

    # Initalisation
    acteurs_from_db = {}
    # Iteration over players in db
    for element in DB.table(PLAYERS_TABLE):
        acteurs_from_db[element.doc_id] = Joueur.from_json(element)

    return acteurs_from_db


def save_players(state: State):
    """Function to save players to database"""

    for player_id, player_instance in state.acteurs.items():
        DB.table(PLAYERS_TABLE.insert(table.Document(player_instance.to_json(), doc_id=player_id))


def save_tournaments(state: State):
    """Function to save tournaments to database"""

    tournaments = state.tournois
    if state.tournoi:
        tournaments.append(state.tournoi)
    tournaments.sort(key=sorters.tournament_chronological)

    for tournoi in tournaments:
        DB.table(TOURNAMENTS_TABLE).insert(tournoi.to_json())

@with_db
def save(state: State):
    """Function to save actual state to database"""

    # Save players
    save_players(state=state)

    # Save tournaments
    save_tournaments(state=state)


if __name__ == '__main__':
    clear_database()
    init_database(db=DB)
    state_to_save = state4()
    save(state=state_to_save)
