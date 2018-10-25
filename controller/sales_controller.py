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
               "Sold between dates"]

    table = sales.read_sales_data()
    choice = None
    while choice != "0":
        choice = terminal_view.get_submenu_choice(options)
        if choice == "1":
            terminal_view.print_table(table, ["Id", "Title", "Price", "Month", "Day", "Year"])
        elif choice == "2":
            inputs = terminal_view.get_inputs(["Title", "Price", "Month", "Day", "Year"], "Add new item to sales:")
            types = [str, int, int, int, int]
            if common.check_input(inputs, types) and check_fields(inputs):
                new_record = sales.add_id(table, inputs)
                table = sales.add(table, new_record)
        elif choice == "3":
            id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
            inputs = terminal_view.get_inputs(["Title", "Price", "Month", "Day", "Year"], "Edit Fields: ")
            types = [str, int, int, int, int]
            if common.check_input(inputs, types) and check_fields(inputs):
                table = sales.update(table, id_, inputs)
        elif choice == "4":
            id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to delete:")[0]
            table = sales.remove(table, id_)
        elif choice == "5":
            cheapest_items_id = sales.get_lowest_price_item_id(table)
            terminal_view.print_result(cheapest_items_id, "Cheapest item's id: ")
        elif choice == "6":
            sold_between(table)
        elif choice != 0:
            terminal_view.print_error_message("There is no such choice.")


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
        check_day(inputs[day_from_index])
        check_day(inputs[day_to_index])
        check_month(inputs[month_from_index])
        check_month(inputs[month_to_index])
        check_year(inputs[year_from_index])
        check_year(inputs[year_to_index])
    except ValueError as e:
        terminal_view.print_error_message(str(e))
    else:
        sold_items = sales.get_items_sold_between(table, *inputs)
        terminal_view.print_result(sold_items, "Sold items: ")


def check_fields(inputs):
    '''Checks if inputs have expected values'''
    price_index = 1
    month_index = 2
    day_index = 3
    year_index = 4
    try:
        check_price(inputs[price_index])
        check_month(inputs[month_index])
        check_day(inputs[day_index])
        check_year(inputs[year_index])
    except ValueError as e:
        terminal_view.print_error_message(str(e))
        return False
    else:
        return True


def check_price(price):
    if int(price) < 0:
        raise ValueError("Wrong price input")


def check_day(day):
    if int(day) > 30 or int(day) < 1:
        raise ValueError("Wrong day value.")


def check_month(month):
    if int(month) > 12 or int(month) < 1:
        raise ValueError("Wrong month value.")


def check_year(year):
    if int(year) < 0:
        raise ValueError("Wrong year value.")


def has_ints(table):
    for element in table:
        if element.isalpha():
            raise ValueError("Inputs have to be numbers")
