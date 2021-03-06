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

    prGreen('┌' + '-' * x + '┐')

    for j, record in enumerate(table):
        prGreen('|', end='')
        for i, element in enumerate(record):
            prGreen(f'{element:^{lengths[i]}}|', end='')
        print()
        if j < len(table) - 1:
            prGreen('|' + x * '-' + '|')
    prGreen('└' + x * '-' + '┘')


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
    type_ = type(result)
    if type_ is int or type_ is str or type_ is float:
        special_print(f'{label} {result}')

    if type_ is list or type_ is set or type_ is tuple:
        special_print(label)
        for i in result:
            special_print(i)

    if type_ is dict:
        for key, value in result.items():
            special_print(f'{key}: {value}')


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
    print_blue_underscore(title)
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
        inputs.append(input(element + ': ').strip())
    return inputs


def get_choice(options):
    print_menu("\nMain menu", options, "Exit program")
    inputs = get_inputs(["Please enter a number"], "")
    print()
    return inputs[0]


def get_submenu_choice(options, submenu_name):
    print_menu(f"\n{submenu_name}", options, "Return to main menu")
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
    prRed('\n' + message + '\n')


def prRed(skk):
    print("\033[91m {}\033[00m" .format(skk))


def prGreen(skk, sep=' ', end='\n'):
    print("\033[38:2:1:125:21m\033[1m{}\033[00m" .format(skk), sep=sep, end=end)


def print_blue_underscore(text):
    print(f'\033[4m\033[38:2:0:7:112m{text}\033[00m')


def special_print(text, sep=' ', end='\n'):
    print(f'\033[38:2:131:20:8m{text}\033[0m')
