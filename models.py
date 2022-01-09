from enum import Enum
import settings

class Composition(Enum):
    protein = 'protein'
    fat = 'fat'
    carbonate = 'carbonate'


class Constant(Enum):
    PROTEIN = settings.protein_rates
    FAT = settings.fat_rates


class Rate(Enum):
    PROTEIN = 4
    FAT = 9
    ALC = 7
    CARBS = 4

