""" Terminal view module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    table = table[:]
    table.insert(0, title_list)
    lengths = []

    for element in title_list:
        lengths.append(len(element) + 2)

    get_longest(lengths, table)

    x = 0

    for element in lengths:
        x += element

    x += len(title_list) - 1

    print('|' + '-' * x + '|')

    for record in table:
        print('|', end='')
        for i, element in enumerate(record):
            print(f'{element:^{lengths[i]}}|', end='')
        print()
        print('|' + x * '-' + '|')


def get_longest(lengths, table):
    for record in table:
        for i, element in enumerate(record):
            element = str(element)
            if len(element) > lengths[i]:
                lengths[i] = len(element) + 2


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    if type(result) is int:
        print(label, result)

    if type(result) is str:
        print(label, result)

    if type(result) is float:
        print(label, result)

    if type(result) is list:
        for i in result:
            print(i)

    if type(result) is dict:
        for key, value in result.items():
            print(f'{key}: {value}')


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(title)
    for i, element in enumerate(list_options):
        print(f'\t({i+1}) {element}')
    print((f'\t(0) {exit_message}'))


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    print(title)

    for element in list_labels:
        inputs.append(input(element + ': '))
    return inputs


def get_choice(options):
    print_menu("\nMain menu", options, "Exit program")
    inputs = get_inputs(["Please enter a number"], "")
    print()
    return inputs[0]


def get_submenu_choice(options):
    print_menu("\nSubmenu", options, "Return to main menu")
    inputs = get_inputs(["Please enter a number"], "")
    print()
    return inputs[0]


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print('\n' + message + '\n')
