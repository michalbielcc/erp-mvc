# everything you'll need is imported:
from view import terminal_view
from model.hr import hr
from controller import common


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    options = ["Show HR",
               "Add",
               "Update",
               "Delete",
               "Oldest person",
               "Person closest to average age"]

    table = hr.read_hr_data()
    choice = None
    while choice != "0":
        choice = terminal_view.get_submenu_choice(options)
        if choice == "1":
            terminal_view.print_table(table, ["Id", "Name", "Birth year"])
        elif choice == "2":
            inputs = terminal_view.get_inputs(["Name", "Birth year"], "Add new HR record:")
            new_record = hr.add_id(table, inputs)
            table = hr.add(table, new_record)
        elif choice == "3":
            id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
            inputs = terminal_view.get_inputs(["Name", "Birth Year"], "Edit Fields")
            table = hr.update(table, id_, inputs)
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        else:
            terminal_view.print_error_message("There is no such choice.")
