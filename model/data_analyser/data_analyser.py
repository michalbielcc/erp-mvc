# This module creates reports for marketing department.
# This module can run independently from other modules.
# Has no own datastructure but uses other modules.
# Avoud using the database (ie. .csv files) of other modules directly.
# Use the functions of the modules instead.
# todo: importing everything you need
# importing everything you need
import os
from model import common
from model.sales import sales
from model.crm import crm
from model.sales import sales
from model.store import store


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

    int(''.join(i[5]+i[3]+i[4])) ===> is integer of date in format: YYYYMMDD
    """
    index = 0
    for i in sales.read_sales_data():
        if int(''.join(i[5]+i[3]+i[4])) > index:
            index = int(''.join(i[5]+i[3]+i[4]))

    for i in sales.read_sales_data():
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
    amount_spent = 0
    name = ''
    id = 0
    id2 = 6
    price = 2
    customer_name = 1
    for record in crm.read_crm_data():
        amount = 0
        for item in sales.read_sales_data():
            if record[id] == item[id2]:
                amount += int(item[price])
        if amount > amount_spent:
            amount_spent = amount
            name = record[customer_name]
    return (name, amount_spent)


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.
    Returns a tuple of customer id and the sum the customer spent.
    eg.: (aH34Jq#&, 42)

   Returns:
        Tuple of customer id and the sum the customer spent
    """
    amount_spent = 0
    name = ''
    id = 0
    id2 = 6
    price = 2
    for record in crm.read_crm_data():
        amount = 0
        for item in sales.read_sales_data():
            if record[id] == item[id2]:
                amount += int(item[2])
        if amount > amount_spent:
            amount_spent = amount
            customer_id = record[id]
    return (customer_id, amount_spent)


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
    data = []
    output = []
    id = 0
    id2 = 6
    name = 1
    how_many = 1
    for record in crm.read_crm_data():
        amount = 0
        for item in sales.read_sales_data():
            if record[id] == item[id2]:
                amount += 1
        data.append([record[name], amount])

    for i in range(num):
        amount = 0
        for item in data:
            if item[how_many] > amount:
                amount = item[how_many]
        for item in data:
            if amount == item[how_many]:
                output.append(tuple(item))
                data.remove(item)
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
    data = []
    output = []
    id = 0
    id2 = 6
    how_many = 1
    for record in crm.read_crm_data():
        amount = 0
        for item in sales.read_sales_data():
            if record[id] == item[id2]:
                amount += 1
        data.append([record[id], amount])

    for i in range(num):
        amount = 0
        for item in data:
            if item[how_many] > amount:
                amount = item[how_many]
        for item in data:
            if amount == item[how_many]:
                output.append(tuple(item))
                data.remove(item)
    return output[0:num]


def get_customers_who_did_not_buy_anything():
    data = []
    output = []
    id = 0
    id2 = 6
    name = 1
    name2 = 0
    how_many = 1
    for record in crm.read_crm_data():
        amount = 0
        for item in sales.read_sales_data():
            if record[id] == item[id2]:
                amount += 1
        data.append([record[name], amount])

    for item in data:
        if item[how_many] == 0:
            output.append(item[name2])
    return output
