""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
import data_manager
import common


def add(table, record):
    common.add(table, record)
    return table


def remove(table, id_):
    common.remove(table, id_)
    return table


def update(table, id_, record):
    common.update(table, id_, record)
    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """
    oldest_year = int(table[0][2])
    names = [table[0][1]]
    for i in range(1, len(table)):
        record_year = int(table[i][2])
        record_name = table[i][1]
        if record_year < oldest_year:
            names = [record_name]
            oldest_year = record_year
        elif record_year == oldest_year:
            names.append(record_name)
            oldest_year = record_year
    return names


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """
    closest = []
    name_index = 1
    year_index = 2

    years = [int(record[year_index]) for record in table]
    average = common.get_average(years)

    smallest_difference = abs(years[0] - average)
    closest = [table[0][name_index]]

    for i in range(1, len(table)):
        record_difference = abs(years[i] - average)
        if record_difference < smallest_difference:
            smallest_difference = record_difference
            closest = [table[i][name_index]]
        elif record_difference == smallest_difference:
            closest.append(table[i][name_index])
    return closest


def read_hr_data():
    table = data_manager.get_table_from_file("hr/persons.csv")
    return table


def add_id(table, inputs):
    '''Creates new id and add it to incomplete record(inputs)'''
    new_id = common.generate_random(table)
    record = [new_id] + inputs
    return record
