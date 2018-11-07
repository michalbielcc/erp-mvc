from view import terminal_view
from model.data_analyser import data_analyser


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
        choice = terminal_view.get_submenu_choice(options, "Data analyser menu")
        if choice == '1':
            last_buyer_name = data_analyser.get_the_last_buyer_name()
            terminal_view.print_result(last_buyer_name, 'Name of last buyer is:')
        elif choice == '2':
            last_buyer_id = data_analyser.get_the_last_buyer_id()
            terminal_view.print_result(last_buyer_id, "Id of last buyer is:")
        elif choice == '3':
            biggest_spender_name = data_analyser.get_the_buyer_name_spent_most_and_the_money_spent()
            terminal_view.print_result(biggest_spender_name, 'Name of biggest spender and the amount is:')
        elif choice == '4':
            biggest_spender_id = data_analyser.get_the_buyer_id_spent_most_and_the_money_spent()
            terminal_view.print_result(biggest_spender_id, 'Id of biggest spender and the amount is:')
        elif choice == '5':
            most_frequent_buyers_names = data_analyser.get_the_most_frequent_buyers_names(num=1)
            terminal_view.print_result(most_frequent_buyers_names, 'Names of most frequent buyer(s) are:')
        elif choice == '6':
            most_frequent_buyers_ids = data_analyser.get_the_most_frequent_buyers_ids(num=1)
            terminal_view.print_result(most_frequent_buyers_ids, 'Names of most frequent buyer(s) are:')
        elif choice == '7':
            customers_who_did_not_buy_anything = data_analyser.get_customers_who_did_not_buy_anything()
            terminal_view.print_result(customers_who_did_not_buy_anything, 'Customers who did not buy anything:')
        elif choice != '0':
            terminal_view.print_error_message("There is no such choice.")
