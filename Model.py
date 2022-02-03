import dataclasses
from enum import Enum
from datetime import date

### Création des classes Enum

# Classe Enum du sexe
class Sex(Enum):
    MALE = 'm'
    FEMALE = 'f'

# Classe Enum du Contrôle du temps
class Controle_du_temps(Enum):
    BULLET = 'bullet'
    BLITZ = 'blitz'
    COUP_RAPIDE = 'coup rapide'

class Tournoi:
    '''Classe Tournoi'''
    pass

class Joueur:
    pass

class Match:
    pass

class Ronde:
    pass


if __name__ == '__main__':
    nouveau_sexe = Sex.MALE
    print(nouveau_sexe.value)
    print(type(nouveau_sexe.value))