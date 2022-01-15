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



def print_info_about_total_calories(weight, sex, height, age):
    """Print total calo according formule
        1.2 coefficient of daily activity
    """
    print("Минимум согласно формуле (без учета дневной активности)")

    result_calories = 10*weight + 6.25*height - 5*age + 5 if sex == 'm' else 10*weight + 6.25*height - 5*age - 161
    if result_calories <= 0:
        print("Check inputs data")
    print(f'Согласно формуле Жерона (дневная активность не учтена): {result_calories * 1.2}')


def print_main_menu(menu: list) -> None:
    """ Correctly draw menu 
    4 simb cus we added 2 probels and 2 '|'
    and 4 prev simbols added in the end
"""
    print('=' * (len("1234".join(menu)) + 4 ))
    for el in menu:
        print(f" {el} ||", end='')
    print()
    print('=' * (len("1234".join(menu)) + 4 ))


def print_all_product(array):
    for row in array:
        print(f"{row['id']}: {row['name']}:=> б - {row['proteins']} || ж - {row['fat']} || у - {row['carbs']} ")