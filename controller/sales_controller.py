# everything you'll need is imported:
from view import terminal_view
from model.sales import sales
from controller import common


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    options = ["Show sales",
               "Add",
               "Update",
               "Delete",
               "Id of the cheapest item",
               "Sold between dates",
               "Title by Id",
               "Last sold game id",
               "Last sold game title",
               "Sum price by id's (not implemented)",
               "Customer id by sale id",
               "All customer id's",
               "Sales id's by customer id",
               "Number of sales per customer"
               ]

    table = sales.read_sales_data()
    choice = None
    while choice != "0":
        choice = terminal_view.get_submenu_choice(options, "Sales menu")
        if choice == "1":
            show_inventory(table)
        elif choice == "2":
            add_new_record(table)
        elif choice == "3":
            edit_record(table)
        elif choice == "4":
            delete_record(table)
        elif choice == "5":
            show_cheapest_id(table)
        elif choice == "6":
            sold_between(table)
        elif choice == '7':
            game_titles_by_id(table)
        elif choice == '8':
            last_sold_game_id(table)
        elif choice == '9':
            last_sold_game_title(table)
        elif choice == '10':
            sum_price_by_id(table)
        elif choice == '11':
            cusomer_id_by_sale_id(table)
        elif choice == '12':
            show_all_customers_ids(table)
        elif choice == '13':
            sale_ids_by_customer_ids(table)
        elif choice == '14':
            number_of_sales_per_customer(table)
        elif choice != '0':
            terminal_view.print_error_message("There is no such choice.")


def show_inventory(table):
    terminal_view.print_table(table, ["Id", "Title", "Price", "Month", "Day", "Year", "Customer Id"])


def add_new_record(table):
    inputs = terminal_view.get_inputs(["Title", "Price", "Month", "Day", "Year",
                                       "Customer Id"], "Add new item to sales:")
    types = [str, int, int, int, int, str]
    if common.check_input(inputs, types) and check_fields(inputs):
        new_record = sales.add_id(table, inputs)
        table = sales.add(table, new_record)
        common.export_to_file(table, 'model/sales/sales.csv')


def edit_record(table):
    id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
    inputs = terminal_view.get_inputs(
        ["Title", "Price", "Month", "Day", "Year", "Customer Id"], "Edit Fields: ")
    common.find_record_and_fill_blanks(table, id_, inputs)
    types = [str, int, int, int, int, str]
    if common.check_input(inputs, types) and check_fields(inputs):
        table = sales.update(table, id_, inputs)
        common.export_to_file(table, 'model/sales/sales.csv')


def delete_record(table):
    id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to delete:")[0]
    table = sales.remove(table, id_)
    common.export_to_file(table, 'model/sales/sales.csv')


def show_cheapest_id(table):
    cheapest_items_id = sales.get_lowest_price_item_id(table)
    terminal_view.print_result(cheapest_items_id, "Cheapest item's id: ")


def sold_between(table):
    inputs = terminal_view.get_inputs(["month_from", "day_from", "year_from",
                                       "month_to", "day_to", "year_to"], "Fill form: ")

    month_from_index = 0
    month_to_index = 3
    day_from_index = 1
    day_to_index = 4
    year_from_index = 2
    year_to_index = 5
    try:
        has_ints(inputs)
        common.check_day(inputs[day_from_index])
        common.check_day(inputs[day_to_index])
        common.check_month(inputs[month_from_index])
        common.check_month(inputs[month_to_index])
        common.check_year(inputs[year_from_index])
        common.check_year(inputs[year_to_index])
    except ValueError as e:
        terminal_view.print_error_message(str(e))
    else:
        sold_items = sales.get_items_sold_between(table, *inputs)
        terminal_view.print_result(sold_items, "Sold items: ")


def game_titles_by_id(table):
    id_ = terminal_view.get_inputs(["Id"], "Enter id of the record: ")[0]
    item_title = sales.get_title_by_id_from_table(table, id_)
    terminal_view.print_result(item_title, f"Title of game with id {id_}:")


def last_sold_game_id(table):
    sold_last_id = sales.get_item_id_sold_last_from_table(table)
    terminal_view.print_result(sold_last_id, "Id of game sold last: ")


def last_sold_game_title(table):
    sold_last_title = sales.get_item_title_sold_last_from_table(table)
    terminal_view.print_result(sold_last_title, "Title of game sold last: ")


def sum_price_by_id(table):
    # get_the_sum_of_prices_from_table(table, item_ids)
    pass


def cusomer_id_by_sale_id(table):
    sale_id = terminal_view.get_inputs(["Id"], "Enter id of the record: ")[0]
    customer_id = sales.get_customer_id_by_sale_id_from_table(table, sale_id)
    terminal_view.print_result(customer_id, "Customer id: ")


def show_all_customers_ids(table):
    all_customer_ids = sales.get_all_customer_ids_from_table(table)
    terminal_view.print_result(all_customer_ids, "All customer id's: ")


def sale_ids_by_customer_ids(table):
    all_sales_ids = sales.get_all_sales_ids_for_customer_ids_form_table(table)
    terminal_view.print_result(all_sales_ids, "All sales id's by customer id's: ")


def number_of_sales_per_customer(table):
    num_of_sales = sales.get_num_of_sales_per_customer_ids_from_table(table)
    terminal_view.print_result(num_of_sales, "Number of sales per customer id: ")


def check_fields(inputs):
    '''Checks if inputs have expected values'''
    price_index = 1
    month_index = 2
    day_index = 3
    year_index = 4
    try:
        common.check_ammount(inputs[price_index])
        common.check_month(inputs[month_index])
        common.check_day(inputs[day_index])
        common.check_year(inputs[year_index])
    except ValueError as e:
        terminal_view.print_error_message(str(e))
        return False
    else:
        return True


def has_ints(table):
    for element in table:
        if element.isalpha():
            raise ValueError("Inputs have to be numbers")
