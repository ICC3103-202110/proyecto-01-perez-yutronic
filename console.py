import os
import time

class Console:

    @staticmethod
    def get_int_input(message):
        return int(input(message))

    @staticmethod
    def get_str_input(message):
        return input(message)

    @staticmethod
    def get_str_input_with_args(message, args):
        return input(message.format(*args))

    @staticmethod
    def print_str_with_args(message, args):
        print(message.format(*args))    

    @staticmethod
    def print_str(message):
        print(message)
      
    @staticmethod
    def clear():
        time.sleep(2)
        os.system('cls||clear')

    @staticmethod
    def print_list(list):  
        str_list = ''
        elements = [ ]
        for element in list:
            elements.append(element)
            
        str_list += ' | '.join(elements) + '\n'
        print(str_list)

    @staticmethod
    def show_table(table):
        Console.print_str("Table: \n")
        Console.print_list(table)
        time.sleep(2)
        os.system('cls||clear')

    @staticmethod
    def show_winner(player):
        Console.print_str_with_args(" \n The WINNER is {}! \n",[player])