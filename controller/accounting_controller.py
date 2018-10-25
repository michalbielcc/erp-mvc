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
        choice = terminal_view.get_submenu_choice(options)
        if choice == "1":
            terminal_view.print_table(table, ["Id", "Month", "Day", "Year", "Type", "Amount"])
        elif choice == "2":
            inputs = terminal_view.get_inputs(
                ["Month", "Day", "Year", "Type", "Amount"], "Add new record to accounting:")
            types = [int, int, int, str, int]
            if common.check_input(inputs, types) == True:
                new_record = accounting.add_id(table, inputs)
                table = accounting.add(table, new_record)
            else:
                terminal_view.print_error_message("Use proper characters for input")
        elif choice == "3":
            id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
            inputs = terminal_view.get_inputs(["Month", "Day", "Year", "Type", "Amount"], "Edit Fields")
            types = [int, int, int, str, int]
            if common.check_input(inputs, types) == True:
                table = accounting.update(table, id_, inputs)
            else:
                terminal_view.print_error_message("Use proper characters for input")
        elif choice == "4":
            id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
            table = accounting.remove(table, id_)
        elif choice == "5":
            highest_profit_year = accounting.which_year_max(table)
            terminal_view.print_result(highest_profit_year, "Most profitable year: ")
        elif choice == "6":
            average_profit_for_year(table)
        elif choice != 0:
            terminal_view.print_error_message("There is no such choice.")


def average_profit_for_year(table):
    year = int(terminal_view.get_inputs(["Year"], "Enter a year:")[0])
    try:
        average_profit = accounting.avg_amount(table, year)
    except ZeroDivisionError:
        terminal_view.print_error_message("There is no such year")
    else:
        terminal_view.print_result(average_profit, f"Average profit for year {year}: ")
