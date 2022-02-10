import model
from datetime import datetime

actual_round = model.Round(nom = 'Round 1', match_liste = '', date_debut = datetime.today(), date_fin = datetime.today())

actual_round.match_liste = 'test'
print(actual_round)


