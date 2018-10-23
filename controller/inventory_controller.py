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
            new_record = inventory.add_id(table, inputs)
            table = inventory.add(table, new_record)
        elif choice == "3":
            id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
            inputs = terminal_view.get_inputs(["Name", "Manufacturer", "Purchase year", "Durability"], "Edit Fields")
            table = inventory.update(table, id_, inputs)
        elif choice == "4":
            id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
            table = inventory.remove(table, id_)
        elif choice == "5":
            available_items = inventory.get_available_items(table)
            terminal_view.print_result(available_items, "Available items: ")
        elif choice == "6":
            durability_averages = inventory.get_average_durability_by_manufacturers(table)
            terminal_view.print_result(durability_averages, "Average durability by manufacturer: ")
        else:
            terminal_view.print_error_message("There is no such choice.")
