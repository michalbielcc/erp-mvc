""" Common functions for controllers
implement commonly used functions here
"""
from view import terminal_view
from model import data_manager


def check_input(inputs, types):
    '''Checks if inputs have expected format'''
    for i in range(len(inputs)):
        try:
            types[i](inputs[i])
        except ValueError:
            terminal_view.print_error_message("Use proper characters for input")
            return False
    return True


def check_id_presence(table, id_):
    id_index = 0
    is_in = False
    for record in table:
        if record[id_index] == id_:
            is_in = True

    return is_in


def export_to_file(table, filename):
    data_manager.write_table_to_file(filename, table)


def check_year(year):
    try:
        x = int(year) + 1
    except ValueError:
        raise ValueError('Use numbers only.')

    if int(year) < 1920 or int(year) > 2020:
        raise ValueError("Wrong year value.")


def check_month(month):
    if int(month) > 12 or int(month) < 1:
        raise ValueError("Wrong month value.")


def check_day(day):
    if int(day) > 30 or int(day) < 1:
        raise ValueError("Wrong day value.")


def check_amount(amount):
    if int(amount) < 0:
        raise ValueError("Use positive numbers for values")
