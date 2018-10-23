""" Common functions for models
implement commonly used functions here
"""
import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''

    ids = [record[0] for record in table]
    upper_letters = "ABCDEFGHIJKLMNOPRSTUWXYZ"
    lower_letters = "abcdefghijklmnoprstuwxyz"
    special_characters = "@#$%^&*"
    numbers = "1234567890"

    not_new = True
    while not_new:
        two_lower = random.choices(lower_letters, k=2)
        two_upper = random.choices(upper_letters, k=2)
        two_special = random.choices(special_characters, k=2)
        two_numbers = random.choices(numbers, k=2)

        new_id = two_lower + two_upper + two_numbers + two_special

        generated = ''.join(new_id)
        if generated not in ids:
            not_new = False

    return generated
