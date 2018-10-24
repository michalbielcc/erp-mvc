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
        choice = terminal_view.get_submenu_choice(options)
        if choice == "1":
            terminal_view.print_table(table, ["Id", "Title", "Manufacturer", 'Price', 'In stock'])
        elif choice == "2":
            inputs = terminal_view.get_inputs(["Title", "Manufacturer", 'Price', 'In stock'], "Add new Store record:")
            new_record = store.add_id(table, inputs)
            table = store.add(table, new_record)
        elif choice == "3":
            id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
            inputs = terminal_view.get_inputs(["Title", "Manufacturer", 'Price', 'In stock'], "Edit Fields")
            table = store.update(table, id_, inputs)
        elif choice == "4":
            id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
            table = store.remove(table, id_)
        elif choice == "5":
            counts_by_manufacturers = store.get_counts_by_manufacturers(table)
            terminal_view.print_result(counts_by_manufacturers, "Game count by manufacturer: ")
        elif choice == "6":
            manufacturer = terminal_view.get_inputs(["Manufacturer"], "Enter name of manufacturer: ")[0]
            average_by_manufacturer = store.get_average_by_manufacturer(table, manufacturer)
            terminal_view.print_result(average_by_manufacturer, "Averge amount of games: ")
        else:
            terminal_view.print_error_message("There is no such choice.")
