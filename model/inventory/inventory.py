""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
from model import data_manager
from model import common


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
            fill_blanks(new_record, old_record)
            table[i] = new_record
            break

    return table


# special functions:
# ------------------

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """
    year_index = 3
    durability_index = 4
    current_year = 2015
    available_items = []
    for record in table:
        record_year = int(record[year_index])
        record_durability = int(record[durability_index])
        validity_date = record_year + record_durability
        if validity_date >= current_year:
            available_items.append(record)

    return available_items


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """
    manufacturer_index = 2
    durability_index = 4
    durability_times = {}
    durability_averages = {}
    for record in table:
        durability = int(record[durability_index])
        manufacturer = record[manufacturer_index]
        durability_times[manufacturer] = durability_times.get(manufacturer, []) + [durability]

    for manufacturer in durability_times:
        durability_averages[manufacturer] = get_average(durability_times[manufacturer])

    return durability_averages


# add to commons
def get_average(numbers: list) -> float:
    summed = 0
    for number in numbers:
        summed += number

    average = float(summed / len(numbers))
    return average


def read_inventory_data():
    table = data_manager.get_table_from_file("model/inventory/inventory.csv")
    return table


def add_id(table, inputs):
    '''Creates new id and add it to incomplete record(inputs)'''
    new_id = common.generate_random(table)
    record = [new_id] + inputs
    return record


def fill_blanks(new, old):
    '''updates blank places in new with old info'''
    for i in range(len(old)):
        if not new[i]:
            new[i] = old[i]
