# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
from controller import common


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    options = ["Show crm",
               "Add",
               "Update",
               "Delete",
               "Longest name id",
               "Subscribers"]

    table = crm.read_crm_data()
    choice = None
    while choice != "0":
        choice = terminal_view.get_submenu_choice(options)
        if choice == "1":
            terminal_view.print_table(table, ["Id", "Name", "Email", "Subscribed"])
        elif choice == "2":
            inputs = terminal_view.get_inputs(["Name", "Email", "Subscribed"], "Add new item to crm:")
            types = [str, str, int]
            if common.check_input(inputs, types) == True:
                new_record = crm.add_id(table, inputs)
                table = crm.add(table, new_record)
            else:
                terminal_view.print_error_message("Use proper characters for input")
        elif choice == "3":
            id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
            inputs = terminal_view.get_inputs(["Name", "Email", "Subscribed"], "Edit Fields: ")
            types = [str, str, int]
            if common.check_input(inputs, types) == True:
                table = crm.update(table, id_, inputs)
            else:
                terminal_view.print_error_message("Use proper characters for input")
        elif choice == "4":
            id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
            table = crm.remove(table, id_)
        elif choice == "5":
            longest_name_id = crm.get_longest_name_id(table)
            terminal_view.print_result(longest_name_id, "Longest name id: ")
        elif choice == "6":
            subscribers = crm.get_subscribed_emails(table)
            terminal_view.print_result(subscribers, "Subscribers: ")
        else:
            terminal_view.print_error_message("There is no such choice.")
