# everything you'll need is imported:
from view import terminal_view
from model.inventory import inventory
from controller import common


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    options = ["Show inventory",
               "Add",
               "Update",
               "Delete",
               "Available items",
               "Average durability"]

    table = inventory.read_inventory_data()
    choice = None
    while choice != "0":
        choice = terminal_view.get_submenu_choice(options, "Inventory menu")
        if choice == "1":
            show_inventory(table)
        elif choice == "2":
            add_new_record(table)
        elif choice == "3":
            edit_record(table)
        elif choice == "4":
            delete_record(table)
        elif choice == "5":
            available_items_info(table)
        elif choice == "6":
            show_average_durability(table)
        elif choice != '0':
            terminal_view.print_error_message("There is no such choice.")


def show_inventory(table):
    terminal_view.print_table(table, ["Id", "Name", "Manufacturer", "Purchase year", "Durability"])


def add_new_record(table):
    inputs = terminal_view.get_inputs(["Name", "Manufacturer", "Purchase year",
                                       "Durability"], "Add new item to inventory:")
    types = [str, str, int, int]
    if common.check_input(inputs, types) and check_fields(inputs):
        new_record = inventory.add_id(table, inputs)
        table = inventory.add(table, new_record)
        common.export_to_file(table, 'model/inventory/inventory.csv')


def edit_record(table):
    id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
    if common.is_id_in_table(id_, table):
        inputs = terminal_view.get_inputs(["Name", "Manufacturer", "Purchase year", "Durability"], "Edit Fields")
        common.find_record_and_fill_blanks(table, id_, inputs)
        types = [str, str, int, int]
        if common.check_input(inputs, types) and check_fields(inputs):
            table = inventory.update(table, id_, inputs)
            common.export_to_file(table, 'model/inventory/inventory.csv')
    else:
        terminal_view.print_error_message("Record of the given id has not been found.")


def delete_record(table):
    id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to delete:")[0]
    if common.is_id_in_table(id_, table):
        table = inventory.remove(table, id_)
        common.export_to_file(table, 'model/inventory/inventory.csv')
    else:
        terminal_view.print_error_message("Record of the given id has not been found.")


def available_items_info(table):
    available_items = inventory.get_available_items(table)
    terminal_view.print_result(available_items, "Available items: ")


def show_average_durability(table):
    durability_averages = inventory.get_average_durability_by_manufacturers(table)
    terminal_view.print_result(durability_averages, "Average durability by manufacturer: ")


def check_fields(inputs):
    '''Checks if inputs have expected values'''
    year_index = 2
    durability_index = 3
    try:
        common.check_year(inputs[year_index])
        common.check_amount(inputs[durability_index])
    except ValueError as e:
        terminal_view.print_error_message(str(e))
        return False
    else:
        return True
