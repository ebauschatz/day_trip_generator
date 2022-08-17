import random

def confirm_selection(selection, selection_type):
    print(f'The currently suggested {selection_type} is: {selection[0].upper() + selection[1:]}.')
    user_confirmation = input(f'Would you like to confirm this {selection_type}? Please enter Y/N: ')
    if user_confirmation.upper() == 'Y':
        return True
    else:
        return False

def select_random_list_element(values):
    return random.choice(values)

def select_independent_option(option_type, all_options):
    option_confirmed = False
    while option_confirmed is False:
        random_selection = select_random_list_element(all_options)
        option_confirmed = confirm_selection(random_selection, option_type)
    return random_selection

def select_dependent_option(option_type, all_options, controlling_key):
    potential_options = all_options[controlling_key]
    return select_independent_option(option_type, potential_options)