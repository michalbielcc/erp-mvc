""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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
            common.fill_blanks(new_record, old_record)
            table[i] = new_record
            break

    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
    Question: What is the id of the customer with the longest name?

    Args:
        table (list): data table to work on

    Returns:
        string: id of the longest name (if there are more than one, return
            the last by alphabetical order of the names)
    """
    id_index = 0
    name_index = 1
    longest_name = table[0][name_index]
    names = []

    for i in range(1, len(table)):
        name = table[i][name_index]
        if len(name) > len(longest_name):
            names = [name]
            longest_name = name
        elif len(name) == len(longest_name):
            names.append(name)

    common.order_alphabetically(names)
    last_name = names[-1]
    for record in table:
        name = record[name_index]
        if name == last_name:
            return record[id_index]
    raise ValueError


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
    Question: Which customers has subscribed to the newsletter?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (where a string is like "email;name")
    """

    name_index = 1
    email_index = 2
    subscribed_index = 3
    subscribers = []
    for record in table:
        if record[subscribed_index] == '1':
            name = record[name_index]
            email = record[email_index]
            email_name = ';'.join([email, name])
            subscribers.append(email_name)

    return subscribers


def read_crm_data():
    table = data_manager.get_table_from_file("model/crm/customers.csv")
    return table


def add_id(table, inputs):
    '''Creates new id and add it to incomplete record(inputs)'''
    new_id = common.generate_random(table)
    record = [new_id] + inputs
    return record
