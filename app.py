from services import calculate_calories, pretty_print_for_human, print_info
import config


class App:
    def print_menu(self):
        menu = config.menu
        l = len(" ".join(menu))
        print("=" * (l + len(menu)))
        print(*menu, sep='||')

    def read_input_data(self):
        try:
            input_weight = int(input('Please input your weight: '))
            input_cal = int(input('Please input total calories you need: '))
        except ValueError as e:
            print(f'Not correct data type. {e}')
            input_weight = input_cal = 0
        ans = calculate_calories(input_cal, input_weight)
        pretty_print_for_human(ans)

    def run(self):
        application = True
        while application:
            self.print_menu()
            command = input('Please choose command: ')
            match command:
                case 'quit':
                    application = False
                    print('Good buy!')
                    break
                case 'calculation':
                    self.read_input_data()
                case 'info':
                    input_weight = int(input('Please input your weight: '))
                    height = int(input('Input your height: '))
                    while 1:
                        sex = input('Input your sex( m/w): ')
                        if sex in ('mw'):break
                        print('Not correct input!')
                    age = int(input('Input your age: '))
                    print_info(weight=input_weight, sex=sex, height=height, age=age)    

                case _:
                    print('Unknown command. Please check')
                    continue




    
