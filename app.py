from services import calculate_calories, pretty_print_for_human


def app():
    try:
        input_weight = int(input('Please input your weight'))
        input_cal = int(input('Please input total calories you need'))
    except ValueError as e:
        print(f'Not correct data type. {e}')
        input_weight = input_cal = 0
    ans = calculate_calories(input_cal, input_weight)
    pretty_print_for_human(ans)
