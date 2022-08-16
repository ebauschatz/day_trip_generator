from random import random
from random_selectors.select_random_element import select_random_list_element
from random_selectors.selection_confirmation import confirm_selection

def select_destination(potential_destinations):
    destination_confirmed = False
    while destination_confirmed is False:
        random_selection = select_random_list_element(potential_destinations)
        destination_confirmed = confirm_selection(random_selection, 'destination')
    return random_selection