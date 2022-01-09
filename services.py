from models import Constant, Composition, Rate


def calculate_calories(total: int, weight: int) -> tuple:
    """Calculate total calories for human's weight"""
    p =  int(Constant.PROTEIN.value * weight)
    f  = int(Constant.FAT.value * weight)
    c = total - (p * Rate.PROTEIN.value + f * Rate.FAT.value)
    c = c // Rate.CARBS.value

    if p < 0 or f < 0 or c < 0:
        print('PLS checks settings beacause results not correct')
    return (p, f, c)


def pretty_print_for_human(total: tuple) -> None:
    """Print data more readebly for human"""
    if total:
        print(f"Proteins: {total[0]}, Fat: {total[1]}, Carbs: {total[-1]} ")
