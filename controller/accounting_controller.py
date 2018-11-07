# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
from controller import common


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    options = ["Show Accounting",
               "Add",
               "Update",
               "Delete",
               "The most profitable year",
               "Average profit for year"]

    table = accounting.read_accounting_data()
    choice = None
    while choice != "0":
        choice = terminal_view.get_submenu_choice(options, "Accounting menu")
        if choice == "1":
            show_accounting(table)
        elif choice == "2":
            add_new_record(table)
        elif choice == "3":
            edit_record(table)
        elif choice == "4":
            delete_record(table)
        elif choice == "5":
            most_profitable_year(table)
        elif choice == "6":
            average_profit_for_year(table)
        elif choice != '0':
            terminal_view.print_error_message("There is no such choice.")


def show_accounting(table):
    terminal_view.print_table(table, ["Id", "Month", "Day", "Year", "Type", "Amount"])


def add_new_record(table):
    inputs = terminal_view.get_inputs(
        ["Month", "Day", "Year", "Type", "Amount"], "Add new record to accounting:")
    types = [int, int, int, str, int]
    if common.check_input(inputs, types) and check_fields(inputs):
        new_record = accounting.add_id(table, inputs)
        accounting.add(table, new_record)
        common.export_to_file(table, 'model/accounting/items.csv')


def edit_record(table):
    id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
    inputs = terminal_view.get_inputs(["Month", "Day", "Year", "Type", "Amount"], "Edit Fields")
    types = [int, int, int, str, int]
    if common.check_input(inputs, types) and check_fields(inputs):
        accounting.update(table, id_, inputs)
        common.export_to_file(table, 'model/accounting/items.csv')


def delete_record(table):
    id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to delete:")[0]
    accounting.remove(table, id_)
    common.export_to_file(table, 'model/accounting/items.csv')


def most_profitable_year(table):
    highest_profit_year = accounting.which_year_max(table)
    terminal_view.print_result(highest_profit_year, "Most profitable year: ")


def average_profit_for_year(table):
    try:
        year = terminal_view.get_inputs(["Year"], "Enter a year:")[0]
        common.check_year(year)
        average_profit = accounting.avg_amount(table, int(year))
    except ZeroDivisionError:
        terminal_view.print_error_message("There is no such year")
    except ValueError as e:
        terminal_view.print_error_message(str(e))
    else:
        terminal_view.print_result(average_profit, f"Average profit for year {year}: ")


def check_fields(inputs):
    '''Checks if inputs have expected values'''
    month_index = 0
    day_index = 1
    year_index = 2
    type_index = 3
    amount_index = 4
    try:
        common.check_month(inputs[month_index])
        common.check_day(inputs[day_index])
        common.check_year(inputs[year_index])
        check_type(inputs[type_index])
        common.check_amount(inputs[amount_index])
    except ValueError as e:
        terminal_view.print_error_message(str(e))
        return False
    else:
        return True


def check_type(type_):
    if type_ == "in" or type_ == "out":
        return
    else:
        raise ValueError("Wrong type value (in/out allowed)")
