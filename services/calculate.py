from models import Constant, Composition, Rate


def calculate_calories(total: int, weight: int) -> tuple:
    """Calculate total calories for human's weight"""
    p =  int(Constant.PROTEIN.value * weight)
    f  = int(Constant.FAT.value * weight)
    c = total - (p * Rate.PROTEIN.value + f * Rate.FAT.value)
    c = c // Rate.CARBS.value

    if p < 0 or f < 0 or c < 0:
        print('PLS checks settings beacause results not correct')
    try:    
        return (p, f, c)
    except ValueError as e:
        print(f'Not corect input data. {e}')

