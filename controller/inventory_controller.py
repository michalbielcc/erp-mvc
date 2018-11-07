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
        choice = terminal_view.get_submenu_choice(options)
        if choice == "1":
            terminal_view.print_table(table, ["Id", "Name", "Manufacturer", "Purchase year", "Durability"])
        elif choice == "2":
            inputs = terminal_view.get_inputs(["Name", "Manufacturer", "Purchase year",
                                               "Durability"], "Add new item to inventory:")
            types = [str, str, int, int]
            if common.check_input(inputs, types) and check_fields(inputs):
                new_record = inventory.add_id(table, inputs)
                table = inventory.add(table, new_record)
                common.export_to_file(table, 'model/inventory/inventory.csv')
        elif choice == "3":
            id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
            inputs = terminal_view.get_inputs(["Name", "Manufacturer", "Purchase year", "Durability"], "Edit Fields")
            types = [str, str, int, int]
            if common.check_input(inputs, types) and check_fields(inputs):
                table = inventory.update(table, id_, inputs)
                common.export_to_file(table, 'model/inventory/inventory.csv')
        elif choice == "4":
            id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to delete:")[0]
            table = inventory.remove(table, id_)
            common.export_to_file(table, 'model/inventory/inventory.csv')
        elif choice == "5":
            available_items = inventory.get_available_items(table)
            terminal_view.print_result(available_items, "Available items: ")
        elif choice == "6":
            durability_averages = inventory.get_average_durability_by_manufacturers(table)
            terminal_view.print_result(durability_averages, "Average durability by manufacturer: ")
        elif choice != '0':
            terminal_view.print_error_message("There is no such choice.")


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
