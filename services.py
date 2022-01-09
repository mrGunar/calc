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


def pretty_print_for_human(total: tuple) -> None:
    """Print data more readebly for human"""
    if total:
        print(f"Proteins: {total[0]}, Fat: {total[1]}, Carbs: {total[-1]} ")



def print_info(weight, sex, height, age):
    """Print total calo according formules"""
    print("Минимум согласно формуле (без учета дневной активности)")

    result_calories = 10*weight + 6.25*height - 5*age + 5 if sex == 'm' else 10*weight + 6.25*height - 5*age - 161
    if result_calories <= 0:
        print("Check inputs data")
    print(f'Согласно формуле Жерона (дневная активность не учтена): {result_calories}')

