# une base de données avec
# - une table players -> { player_id: Joueur }
# - une table tournaments -> { tournament_id: Tournoi }
from typing import Dict, List

from core.model import Joueur, State, Tournoi


def load_players() -> Dict[int, Joueur]:
    # table = db.table('players')
    # players: List[Dict[???]] = table.get()
    # players_by_id = {player_id: player for player in players}
    #
    # return players_by_id
    return {}


def load_tournaments() -> List[Tournoi]:
    return []


def save(state: State):
    # db = TinyDB()

    # save players
    players = sorted(state.acteurs.values(), key=???)
    players_as_json = [player.to_json() for player in players]
    db.table('players').insert_many(players)

    # save tournaments

    print("State saved!")
