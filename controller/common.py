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
