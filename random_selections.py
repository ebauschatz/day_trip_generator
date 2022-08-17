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

def select_random_option(option_category, all_options):
    option_confirmed = False
    while option_confirmed is False:
        random_selection = select_random_list_element(all_options)
        option_confirmed = confirm_selection(random_selection, option_category)
    return random_selection

#If there are multiple objects with the same name propertry, only the first will be returned
def select_random_object_by_name(option_category, all_objects):
    all_object_names = [x.name for x in all_objects]
    selected_object_name = select_random_option(option_category, all_object_names)
    selected_objects = [x for x in all_objects if x.name == selected_object_name]
    return selected_objects[0]