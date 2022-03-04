# une base de données avec
# - une table players -> { player_id: Joueur }
# - une table tournaments -> { tournament_id: Tournoi }
from typing import Dict, List
from core.model import Joueur, State, Tournoi
from tinydb import TinyDB, Query


def load_players() -> Dict[int, Joueur]:
    # table = db.table('players')
    # players: List[Dict[???]] = table.get()
    # players_by_id = {player_id: player for player in players}
    #
    # return players_by_id
    return {}
