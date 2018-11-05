from view import terminal_view
from data_analyser import data_analyser


def run():
    options = ['Get the last buyer name',
               'Get the last buyer id',
               'Get the name of a buyer that spent most money',
               'Get the id of a buyer that spent most money',
               'Get the names of most frequent buyers',
               'Get the ids of most frequent buyers',
               'Get names of buyers that did not buy anything']
    choice = None

    while choice != '0':
        choice = terminal_view.get_submenu_choice(options)
        if choice == '1':
            get_the_last_buyer_name()
        elif choice == '2':
            get_the_last_buyer_id()
        elif choice == '3':
            get_the_buyer_name_spent_most_and_the_money_spent()
        elif choice == '4':
            get_the_buyer_id_spent_most_and_the_money_spent()
        elif choice == '5':
            get_the_most_frequent_buyers_names(num=1)
        elif choice == '6':
            get_the_most_frequent_buyers_ids(num=1)
        elif choice == '7':
            get_customers_who_did_not_buy_anything()
        elif choice != '0':
            terminal_view.print_error_message("There is no such choice.")