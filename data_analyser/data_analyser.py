# This module creates reports for marketing department.
# This module can run independently from other modules.
# Has no own datastructure but uses other modules.
# Avoud using the database (ie. .csv files) of other modules directly.
# Use the functions of the modules instead.

# todo: importing everything you need

# importing everything you need
import os
import common
from sales import sales
from crm import crm
from sales import sales
from store import store


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        Customer name of the last buyer
    """
    return crm.get_name_by_id(get_the_last_buyer_id())
  

def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        Customer id of the last buyer
    """

    dates_list = []
    index = 0

    for item in sales.read_sales_data():
        dates_list.append(item)

    for i in dates_list:
        if int(''.join(i[5]+i[3]+i[4])) > index:
            index = int(''.join(i[5]+i[3]+i[4]))
    
    for i in dates_list:
        if int(''.join(i[5]+i[3]+i[4])) == index:
            return i[6]


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.
    Returns a tuple of customer name and the sum the customer spent.
    eg.: (aH34Jq#&, 42)

   Returns:
        Tuple of customer name and the sum the customer spent
    """   
    curent_amount = 0
    highest_amount = 0
    name = ''

    for record in crm.read_crm_data():
        for item in sales.read_sales_data():
            if record[0] == item[6]:
                curent_amount += int(item[2])
        if curent_amount > highest_amount:
            highest_amount = curent_amount
            name = record[1]
            curent_amount = 0 
    return (name, highest_amount)


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.
    Returns a tuple of customer id and the sum the customer spent.
    eg.: (aH34Jq#&, 42)

   Returns:
        Tuple of customer id and the sum the customer spent
    """

    curent_amount = 0
    highest_amount = 0
    customer_id = ''

    for record in crm.read_crm_data():
        for item in sales.read_sales_data():
            if record[0] == item[6]:
                curent_amount += int(item[2])
        if curent_amount > highest_amount:
            highest_amount = curent_amount
            customer_id = record[0]
            curent_amount = 0 
    return (customer_id, highest_amount)


def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customers' name) who bought most frequently.
    Returns an ordered list of tuples of customer names and the number of their sales.
    (The first one bought the most frequent.)
    eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]

    Args:
        num: the number of the customers to return.

    Returns:
        Ordered list of tuples of customer names and num of sales
    """
    amount = 0
    data = []
    output = []

    for record in crm.read_crm_data():
        for item in sales.read_sales_data():
            if record[0] == item[6]:
                amount += 1
        data.append([record[1], amount])
        amount = 0

    for i in range(num):
        for item in data:
            if item[1] > amount:
                amount = item[1]
        for item in data:
            if amount == item[1]:
                output.append(tuple(item))
                data.remove(item)
        amount = 0

    return output[0:num]


def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent.
    Returns an ordered list of tuples of customer id and the number their sales.
    (The first one bought the most frequent.)
    eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]

    Args:
        num: the number of the customers to return.

    Returns:
        Ordered list of tuples of customer ids and num of sales
    """
    amount = 0
    data = []
    output = []

    for record in crm.read_crm_data():
        for item in sales.read_sales_data():
            if record[0] == item[6]:
                amount += 1
        data.append([record[0], amount])
        amount = 0

    for i in range(num):
        for item in data:
            if item[1] > amount:
                amount = item[1]
        for item in data:
            if amount == item[1]:
                output.append(tuple(item))
                data.remove(item)
        amount = 0

    return output[0:num]