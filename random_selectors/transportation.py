from random_selectors.select_random_element import select_random_list_element
from random_selectors.selection_confirmation import confirm_selection

def select_transportation(potential_transportations):
    transportation_confirmed = False
    while transportation_confirmed is False:
        random_selection = select_random_list_element(potential_transportations)
        transportation_confirmed = confirm_selection(random_selection, 'transportation')
    return random_selection