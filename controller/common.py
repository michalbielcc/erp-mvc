""" Common functions for controllers
implement commonly used functions here
"""


def check_input(inputs, types):
    '''Checks if inputs have expected format'''
    for i in range(len(inputs)):
        try:
            types[i](inputs[i])
        except ValueError:
            return False
    return True


def check_id_presence(table, id_):
    id_index = 0
    is_in = False
    for record in table:
        if record[id_index] == id_:
            is_in = True

    return is_in
