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


def get_average(numbers: list) -> float:
    summed = 0
    for number in numbers:
        summed += number

    average = float(summed / len(numbers))
    return average


def order_alphabetically(to_sort: list):  # vurnelable to list with elements of type different from str
    '''Sorts (in place) elements in the given list in alphabetical order

    Uses simple bubble sort.
    '''

    for i in range(len(to_sort) - 1):
        for j in range(len(to_sort) - 1):
            if to_sort[j].lower() > to_sort[j + 1].lower():
                to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]


def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """
    table.append(record)

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    for i, record in enumerate(table):
        if record[0] == id_:
            table.pop(i)
            break

    return table


def update(table, id_, record):
    """
    Updates specified record in the table.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
        record (list): updated record

    Returns:
        list: table with updated record
    """

    for i, old_record in enumerate(table):
        if old_record[0] == id_:
            new_record = [id_] + record
            table[i] = new_record
            break

    return table
