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
        choice = terminal_view.get_submenu_choice(options, "CRM menu")
        if choice == "1":
            show_crm(table)
        elif choice == "2":
            add_new_record(table)
        elif choice == "3":
            edit_record(table)
        elif choice == "4":
            delete_record(table)
        elif choice == "5":
            id_of_longest_name(table)
        elif choice == "6":
            subscribers_info(table)
        elif choice != '0':
            terminal_view.print_error_message("There is no such choice.")


def show_crm(table):
    terminal_view.print_table(table, ["Id", "Name", "Email", "Subscribed"])


def add_new_record(table):
    inputs = terminal_view.get_inputs(["Name", "Email", "Subscribed"], "Add new item to crm:")
    types = [str, str, int]
    if common.check_input(inputs, types) and check_fields(inputs):
        new_record = crm.add_id(table, inputs)
        table = crm.add(table, new_record)
        common.export_to_file(table, 'model/crm/customers.csv')


def edit_record(table):
    id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
    inputs = terminal_view.get_inputs(["Name", "Email", "Subscribed"], "Edit Fields: ")
    common.find_record_and_fill_blanks(table, id_, inputs)
    types = [str, str, int]
    if common.check_input(inputs, types) and check_fields(inputs):
        table = crm.update(table, id_, inputs)
        common.export_to_file(table, 'model/crm/customers.csv')


def delete_record(table):
    id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to delete:")[0]
    table = crm.remove(table, id_)
    common.export_to_file(table, 'model/crm/customers.csv')


def id_of_longest_name(table):
    longest_name_id = crm.get_longest_name_id(table)
    terminal_view.print_result(longest_name_id, "Longest name id: ")


def subscribers_info(table):
    subscribers = crm.get_subscribed_emails(table)
    terminal_view.print_result(subscribers, "Subscribers: ")


def check_fields(inputs):
    '''Checks if inputs have expected values'''
    email_index = 1
    subscribed_index = 2
    try:
        check_email(inputs[email_index])
        check_subscribed(inputs[subscribed_index])
    except ValueError as e:
        terminal_view.print_error_message(str(e))
        return False
    else:
        return True


def check_email(email):
    if '@' not in email:
        raise ValueError("Wrong email value (@ not found)")


def check_subscribed(sub):
    if int(sub) == 0 or int(sub) == 1:
        return
    else:
        raise ValueError("Wrong subsribed value (0/1 allowed)")
