# everything you'll need is imported:
from model.store import store
from view import terminal_view
from controller import common


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    options = ["Show Store",
               "Add",
               "Update",
               "Delete",
               "Game count by manufacturer",
               "Average count in stock by manufacturer"]

    table = store.read_store_data()

    choice = None
    while choice != "0":
        choice = terminal_view.get_submenu_choice(options, "Store menu")
        if choice == "1":
            show_accounting(table)
        elif choice == "2":
            add_new_record(table)
        elif choice == "3":
            edit_record(table)
        elif choice == "4":
            delete_record(table)
        elif choice == "5":
            game_count_by_manufacturer(table)
        elif choice == "6":
            average_by_manufacturer(table)
        elif choice != '0':
            terminal_view.print_error_message("There is no such choice.")


def show_accounting(table):
    terminal_view.print_table(table, ["Id", "Title", "Manufacturer", 'Price', 'In stock'])


def add_new_record(table):
    inputs = terminal_view.get_inputs(["Title", "Manufacturer", 'Price', 'In stock'], "Add new Store record:")
    types = [str, str, int, int]
    if common.check_input(inputs, types) and check_fields(inputs):
        new_record = store.add_id(table, inputs)
        table = store.add(table, new_record)
        common.export_to_file(table, 'model/store/games.csv')


def edit_record(table):
    id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
    if common.is_id_in_table(id_, table):
        inputs = terminal_view.get_inputs(["Title", "Manufacturer", 'Price', 'In stock'], "Edit Fields")
        common.find_record_and_fill_blanks(table, id_, inputs)
        types = [str, str, int, int]
        if common.check_input(inputs, types) and check_fields(inputs):
            table = store.update(table, id_, inputs)
            common.export_to_file(table, 'model/store/games.csv')
    else:
        terminal_view.print_error_message("Record of the given id has not been found.")


def delete_record(table):
    id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to delete:")[0]
    if common.is_id_in_table(id_, table):
        table = store.remove(table, id_)
        common.export_to_file(table, 'model/store/games.csv')
    else:
        terminal_view.print_error_message("Record of the given id has not been found.")


def game_count_by_manufacturer(table):
    counts_by_manufacturers = store.get_counts_by_manufacturers(table)
    terminal_view.print_result(counts_by_manufacturers, "Game count by manufacturer: ")


def average_by_manufacturer(table):
    manufacturer = terminal_view.get_inputs(["Manufacturer"], "Enter name of manufacturer: ")[0]
    try:
        average_by_manufacturer = store.get_average_by_manufacturer(table, manufacturer)
    except ZeroDivisionError:
        terminal_view.print_error_message('No such manufacturer, try again')
    else:
        terminal_view.print_result(average_by_manufacturer, "Averge amount of games: ")


def check_fields(inputs):
    '''Checks if inputs have expected values'''
    price_index = 2
    in_stock_index = 3
    try:
        common.check_amount(inputs[price_index])
        common.check_amount(inputs[in_stock_index])
    except ValueError as e:
        terminal_view.print_error_message(str(e))
        return False
    else:
        return True
