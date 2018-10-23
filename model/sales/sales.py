""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """
    id_index = 0
    name_index = 1
    price_index = 2
    lowest_price = int(table[0][price_index])
    cheapest_names = [table[0][name_index]]
    for i in range(1, len(table)):
        price = int(table[i][price_index])
        name = table[i][name_index]
        if price < lowest_price:
            cheapest_names = [name]
            lowest_price = price
        elif price == lowest_price:
            cheapest_names.append(name)

    order_alphabetically(cheapest_names)
    last_name = cheapest_names[-1]
    id_ = find_id_by_name(last_name, table)
    return id_


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code


def find_id_by_name(name, table):
    id_index = 0
    name_index = 1
    for record in table:
        if name == record[name_index]:
            return record[id_index]
    raise ValueError


def order_alphabetically(to_sort: list):  # vurnelable to list with elements of type different from str
    '''Sorts (in place) elements in the given list in alphabetical order

    Uses simple bubble sort.
    '''

    for i in range(len(to_sort) - 1):
        for j in range(len(to_sort) - 1):
            if to_sort[j].lower() > to_sort[j + 1].lower():
                to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]


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
