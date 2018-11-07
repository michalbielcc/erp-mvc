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
        choice = terminal_view.get_submenu_choice(options, "HR menu")
        if choice == "1":
            terminal_view.print_table(table, ["Id", "Name", "Birth year"])
        elif choice == "2":
            inputs = terminal_view.get_inputs(["Name", "Birth year"], "Add new HR record:")
            types = [str, int]
            if common.check_input(inputs, types) and check_fields(inputs):
                new_record = hr.add_id(table, inputs)
                table = hr.add(table, new_record)
                common.export_to_file(table, 'model/hr/persons.csv')
        elif choice == "3":
            id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to edit:")[0]
            inputs = terminal_view.get_inputs(["Name", "Birth Year"], "Edit Fields")
            types = [str, int]
            if common.check_input(inputs, types) and check_fields(inputs):
                table = hr.update(table, id_, inputs)
                common.export_to_file(table, 'model/hr/persons.csv')
        elif choice == "4":
            id_ = terminal_view.get_inputs(["Id"], "Enter id of the record you want to delete:")[0]
            table = hr.remove(table, id_)
            common.export_to_file(table, 'model/hr/persons.csv')
        elif choice == "5":
            oldest_person = hr.get_oldest_person(table)
            terminal_view.print_result(oldest_person, "Oldest person: ")
        elif choice == "6":
            near_average = hr.get_persons_closest_to_average(table)
            terminal_view.print_result(near_average, "Closest to average age: ")
        elif choice != '0':
            terminal_view.print_error_message("There is no such choice.")


def check_fields(inputs):
    '''Checks if inputs have expected values'''
    year_index = 1
    try:
        common.check_year(inputs[year_index])
    except ValueError as e:
        terminal_view.print_error_message(str(e))
        return False
    else:
        return True
