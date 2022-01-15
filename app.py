import sqlite3
import pandas as pd
from services import info, products, calculate, menu
import config
from FDataBase import DBProduct, DBUser


class App:
    def __init__(self, application=None):
        self.application = True
        self.db_users = DBUser()
        self.db_product = DBProduct()

    def read_input_data_for_calculate(self):
        try:
            input_weight = int(input('Please input your weight: '))
            input_cal = int(input('Please input total calories you need: '))
        except ValueError as e:
            print(f'Not correct data type. {e}')
            input_weight = input_cal = 0
        ans = calculate.calculate_calories(input_cal, input_weight)
        info.pretty_print_for_human(ans)

    def info_command(self):
        """Command if user chooce `info`"""
        input_weight = int(input('Please input your weight: '))
        height = int(input('Input your height: '))
        while 1:
            sex = input('Input your sex( m/w): ')
            if sex in ('mw'):break
            print('Not correct input!')
        age = int(input('Input your age: '))
        info.print_info_about_total_calories(weight=input_weight, sex=sex, height=height, age=age)


    def check_commands(self, command):
        match command:
                case 'quit':
                    print('Good buy!')
                    return False
                case 'calculation':
                    self.read_input_data_for_calculate()
                case 'info':
                    self.info_command()
                case 'read':
                    all_products = self.db_product.show_all_products()
                    products.print_all_product(all_products)
                case _:
                    print('Unknown command. Please check')
        return True

    def run(self):        

        while self.application:
            menu.print_main_menu(config.menu)
            command = input('Please choose command: ')
            if not self.check_commands(command):
                self.application = False
                break
            
        self.db_product.close_connect()
        self.db_users.close_connect()




    
