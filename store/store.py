""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
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

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """
    games = {}
    manufacturers = set()
    amount = 0

    for i in table:
        manufacturers.add(i[2])

    for i in table:
        if i[2] in games:
            amount = games.get(i[2])
            amount += 1
            games[i[2]] = amount
            amount = 0

        if i[2] not in games:
            if i[2] in manufacturers:
                games[i[2]] = 1
                amount = 0
    return games


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """
    amount = 0
    count = 0

    for i in table:
        if i[2].lower() == manufacturer.lower():
            amount += float(i[4])
            count += 1
    return amount / count


def read_store_data():
    table = data_manager.get_table_from_file("store/games.csv")
    return table


def add_id(table, inputs):
    '''Creates new id and add it to incomplete record(inputs)'''
    new_id = common.generate_random(table)
    record = [new_id] + inputs
    return record
