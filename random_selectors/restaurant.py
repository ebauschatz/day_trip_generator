from random_selectors.select_random_element import select_random_list_element
from random_selectors.selection_confirmation import confirm_selection

def select_restaurant(destination, destination_restaurants):
    potential_restaurants = find_potential_restaurants(destination, destination_restaurants)
    restaurant_confirmed = False
    while restaurant_confirmed is False:
        random_selection = select_random_list_element(potential_restaurants)
        restaurant_confirmed = confirm_selection(random_selection, 'restaurant')
    return random_selection

def find_potential_restaurants(destination, destination_restaurants):
    return destination_restaurants[destination]