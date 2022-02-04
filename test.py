from enum import Enum

class Sex(Enum):
    MALE = 'm'
    FEMALE  = 'f'

res = [sexe_member.value for sexe_member in Sex]
print(res)
