""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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
    table = data_manager.get_table_from_file("crm/customers.csv")
    return table


def add_id(table, inputs):
    '''Creates new id and add it to incomplete record(inputs)'''
    new_id = common.generate_random(table)
    record = [new_id] + inputs
    return record


###################################


def get_name_by_id(id):
    """
    Reads the table with the help of the data_manager module.
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the customer

    Returns:
        str the name of the customer
    """

    id_index = 0
    name_index = 1

    table = read_crm_data()
    for record in table:
        if id == record[id_index]:
            return record[name_index]
    return None


def get_name_by_id_from_table(table, id):
    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the customer table
        id (str): the id of the customer

    Returns:
        str the name of the customer
    """
    id_index = 0
    name_index = 1

    for record in table:
        if id == record[id_index]:
            return record[name_index]
    return None
