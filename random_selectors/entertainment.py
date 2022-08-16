from random_selectors.select_random_element import select_random_list_element
from random_selectors.selection_confirmation import confirm_selection

def select_entertainment(destination, destination_entertainments):
    potential_entertainments = find_potential_entertainments(destination, destination_entertainments)
    entertainment_confirmed = False
    while entertainment_confirmed is False:
        random_selection = select_random_list_element(potential_entertainments)
        entertainment_confirmed = confirm_selection(random_selection, 'entertainment')
    return random_selection

def find_potential_entertainments(destination, destination_entertainments):
    return destination_entertainments[destination]