from enum import Enum
import json


class Composition(Enum):
    protein = 'protein'
    fat = 'fat'
    carbonate = 'carbonate'


class Constant(Enum):
    with open('config.json') as f:
        ans = json.load(f)
        PROTEIN = ans['protein_rates']
        FAT = ans['fat_rates']


class Rate(Enum):
    PROTEIN = 4
    FAT = 9
    ALC = 7
    CARBS = 4

