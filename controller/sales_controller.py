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
            if common.check_input(inputs, types):
                new_record = sales.add_id(table, inputs)
                table = sales.add(table, new_record)
            else:
                terminal_view.print_error_message("Use proper characters for input")
        elif choice == "3":
            id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
            inputs = terminal_view.get_inputs(["Title", "Price", "Month", "Day", "Year"], "Edit Fields: ")
            types = [str, int, int, int, int]
            if common.check_input(inputs, types):
                table = sales.update(table, id_, inputs)
            else:
                terminal_view.print_error_message("Use proper characters for input")
        elif choice == "4":
            id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
            table = sales.remove(table, id_)
        elif choice == "5":
            cheapest_items_id = sales.get_lowest_price_item_id(table)
            terminal_view.print_result(cheapest_items_id, "Cheapest item's id: ")
        elif choice == "6":
            sold_between(table)
        else:
            terminal_view.print_error_message("There is no such choice.")


def sold_between(table):
    inputs = terminal_view.get_inputs(["month_from", "day_from", "year_from",
                                       "month_to", "day_to", "year_to"], "Fill form: ")
    try:
        for elem in inputs:
            int(elem)
    except ValueError:
        terminal_view.print_error_message("Enter only number")
    else:
        sold_items = sales.get_items_sold_between(table, *inputs)
        terminal_view.print_result(sold_items, "Sold items: ")
