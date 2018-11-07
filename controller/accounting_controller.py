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
            if common.check_input(inputs, types) and check_fields(inputs):
                new_record = accounting.add_id(table, inputs)
                table = accounting.add(table, new_record)
                common.export_to_file(table, 'model/accounting/items.csv')
        elif choice == "3":
            id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
            inputs = terminal_view.get_inputs(["Month", "Day", "Year", "Type", "Amount"], "Edit Fields")
            types = [int, int, int, str, int]
            if common.check_input(inputs, types) and check_fields(inputs):
                table = accounting.update(table, id_, inputs)
                common.export_to_file(table, 'model/accounting/items.csv')
        elif choice == "4":
            id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to delete:")[0]
            table = accounting.remove(table, id_)
            common.export_to_file(table, 'model/accounting/items.csv')
        elif choice == "5":
            highest_profit_year = accounting.which_year_max(table)
            terminal_view.print_result(highest_profit_year, "Most profitable year: ")
        elif choice == "6":
            average_profit_for_year(table)
        elif choice != '0':
            terminal_view.print_error_message("There is no such choice.")


def average_profit_for_year(table):
    try:
        year = terminal_view.get_inputs(["Year"], "Enter a year:")[0]
        check_year(year)
        average_profit = accounting.avg_amount(table, year)
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
        check_month(inputs[month_index])
        check_day(inputs[day_index])
        check_year(inputs[year_index])
        check_type(inputs[type_index])
        check_amount(inputs[amount_index])
    except ValueError as e:
        terminal_view.print_error_message(str(e))
        return False
    else:
        return True


def check_amount(amount):
    if int(amount) < 0:
        raise ValueError("Wrong amount value.")


def check_day(day):
    if int(day) > 30 or int(day) < 1:
        raise ValueError("Wrong day value.")


def check_month(month):
    if int(month) > 12 or int(month) < 1:
        raise ValueError("Wrong month value.")


def check_year(year):
    if type(year) == str:
        raise ValueError("Input have to be number")
    if int(year) < 0:
        raise ValueError("Wrong year value.")


def check_type(type_):
    if type_ == "in" or type_ == "out":
        return
    else:
        raise ValueError("Wrong type value (in/out allowed)")