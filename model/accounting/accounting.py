""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
from model import data_manager
from model import common


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

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    year_index = 3
    type_index = 4
    amount_index = 5
    profits = {}

    for record in table:
        year = record[year_index]
        type_ = record[type_index]
        amount = int(record[amount_index])
        if type_ == "in":
            profits[year] = profits.get(year, 0) + amount
        elif type_ == "out":
            profits[year] = profits.get(year, 0) - amount

    listed_profits = profits.items()
    max_year = max(listed_profits, key=lambda tup: tup[1])[0]
    return int(max_year)


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    year_index = 3
    type_index = 4
    amount_index = 5
    profits = 0
    table = [record for record in table if int(record[year_index]) == year]
    items_count = len(table)
    for record in table:
        year = record[year_index]
        type_ = record[type_index]
        amount = int(record[amount_index])
        if type_ == "in":
            profits += amount
        elif type_ == "out":
            profits -= amount
    return profits / items_count


def read_accounting_data():
    table = data_manager.get_table_from_file("model/accounting/items.csv")
    return table


def add_id(table, inputs):
    '''Creates new id and add it to incomplete record(inputs)'''
    new_id = common.generate_random(table)
    record = [new_id] + inputs
    return record
