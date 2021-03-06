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
from model.crm import crm


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

    common.order_alphabetically(cheapest_names)
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
    month_index = 3
    day_index = 4
    year_index = 5

    from_date = f"{year_from:0>4}{month_from:0>2}{day_from:0>2}"
    to_date = f"{year_to:0>4}{month_to:0>2}{day_to:0>2}"

    sold_between = []
    for record in table:
        record = record.copy()
        month = record[month_index]
        day = record[day_index]
        year = record[year_index]
        date = f"{year:0>4}{month:0>2}{day:0>2}"
        if from_date < date < to_date:
            sold_between.append(record[:-1])
        x = 2
        while x <= 5:
            for i in sold_between:
                i[x] = int(i[x])
            x += 1

    return sold_between


def find_id_by_name(name, table):
    id_index = 0
    name_index = 1
    for record in table:
        if name == record[name_index]:
            return record[id_index]
    raise ValueError


def read_sales_data():
    table = data_manager.get_table_from_file("model/sales/sales.csv")
    return table


def add_id(table, inputs):
    '''Creates new id and add it to incomplete record(inputs)'''
    new_id = common.generate_random(table)
    record = [new_id] + inputs
    return record

# ======================================


def get_title_by_id(id):
    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str the title of the item
    """
    table = read_sales_data()
    return get_title_by_id_from_table(table, id)


def get_title_by_id_from_table(table, id):
    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str the title of the item
    """

    id_index = 0
    title_index = 1

    for record in table:
        if record[id_index] == id:
            return record[title_index]
    return None


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        (str) the _id_ of the item that was sold most recently.
    """
    table = read_sales_data()
    return get_item_id_sold_last_from_table(table)


def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        (str) the _id_ of the item that was sold most recently.
    """

    id_index = 0
    month_index = 3
    day_index = 4
    year_index = 5

    month = table[0][month_index]
    day = table[0][day_index]
    year = table[0][year_index]

    latest_date = f"{year:0>4}{month:0>2}{day:0>2}"
    latest_id = table[0][id_index]

    sold_between = []
    for record in table[1:]:
        month = record[month_index]
        day = record[day_index]
        year = record[year_index]
        date = f"{year:0>4}{month:0>2}{day:0>2}"
        if latest_date < date:
            latest_id = record[id_index]
            latest_date = date

    return latest_id


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        (str) the _title_ of the item that was sold most recently.
    """

    title_index = 1
    month_index = 3
    day_index = 4
    year_index = 5

    month = table[0][month_index]
    day = table[0][day_index]
    year = table[0][year_index]

    latest_date = f"{year:0>4}{month:0>2}{day:0>2}"
    latest_title = table[0][title_index]

    sold_between = []
    for record in table[1:]:
        month = record[month_index]
        day = record[day_index]
        year = record[year_index]
        date = f"{year:0>4}{month:0>2}{day:0>2}"
        if latest_date < date:
            latest_title = record[title_index]
            latest_date = date

    return latest_title


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        (number) the sum of the items' prices
    """
    table = read_sales_data()
    return get_the_sum_of_prices_from_table(table, item_ids)


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        (number) the sum of the items' prices
    """
    id_index = 0
    price_index = 2
    price_sum = 0

    for record in table:
        if record[id_index] in item_ids:
            price_sum += int(record[price_index])
    return price_sum


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.
    Args:
         sale_id (str): sale id to search for
    Returns:
         customer_id that belongs to the given sale id
    """
    table = read_sales_data()
    return get_customer_id_by_sale_id_from_table(table, sale_id)


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.
    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
         customer_id that belongs to the given sale id
    """
    id_index = 0
    customer_index = 6
    for record in table:
        if record[id_index] == sale_id:
            return record[customer_index]
    return None


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.
    Returns a set of customer_ids that are present in the table.
    Returns:
         set of customer_ids that are present in the table
    """

    table = read_sales_data()
    return get_all_customer_ids_from_table(table)


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.
    Args:
        table (list of list): the sales table
    Returns:
         set of customer_ids that are present in the table
    """
    customer_index = 6
    return set(list(zip(*table))[customer_index])


def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """
    table = crm.read_crm_data()
    return get_all_sales_ids_for_customer_ids_form_table(table)


def get_all_sales_ids_for_customer_ids_form_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """
    table = crm.read_crm_data()
    output = {}
    id = 0
    id2 = 6
    product_id = 0
    for record in table:
        customer_id = ''
        sales_ids = []
        for item in read_sales_data():
            if record[id] == item[id2]:
                customer_id = record[id]
                sales_ids.append(item[product_id])
        if sales_ids:
            output[customer_id] = sales_ids
    return output


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """
    table = read_sales_data()
    return get_num_of_sales_per_customer_ids_from_table(table)


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """
    amount = 0
    data = []
    output = {}
    id = 0
    id2 = 6
    product_id = 0
    how_many = 1
    for record in crm.read_crm_data():
        for item in table:
            if record[id] == item[id2]:
                amount += 1
        data.append([record[id], amount])
        amount = 0
    for item in data:
        if item[how_many] > 0:
            output[item[product_id]] = item[how_many]
    return output
