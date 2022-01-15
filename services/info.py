def print_info_about_total_calories(weight, sex, height, age):
    """Print total calo according formule
        1.2 coefficient of daily activity
    """
    print("Минимум согласно формуле (без учета дневной активности)")

    result_calories = 10*weight + 6.25*height - 5*age + 5 if sex == 'm' else 10*weight + 6.25*height - 5*age - 161
    if result_calories <= 0:
        print("Check inputs data")
    print(f'Согласно формуле Жерона (дневная активность не учтена): {result_calories * 1.2}')



def pretty_print_for_human(total: tuple) -> None:
    """Print data more readebly for human"""
    if total:
        print(f"Proteins: {total[0]}, Fat: {total[1]}, Carbs: {total[-1]} ")
