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