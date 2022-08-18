import console_display
import hard_coded_data
from data_models import Trip
from random_selections import select_random_option, select_random_object_by_name

def main():
    #Get pre-populated options from hard-coded data
    all_trip_categories = hard_coded_data.all_trip_categories
    all_transportations = hard_coded_data.all_transportations
    all_destinations = hard_coded_data.all_destinations

    #Configure initial selections
    trip = configure_initial_trip_details(all_destinations, all_transportations)
    
    #Confirm or reconfigure as necessary
    confirm_trip_details(trip, all_destinations, all_transportations, all_trip_categories)
    
    #Display confirmation message and trip summary
    console_display.display_confirmed_trip_details(trip)

def configure_initial_trip_details(destinations, transportations):
    selected_destination = select_random_object_by_name('destination', destinations)
    selected_transportation = select_random_option('transportation', transportations)
    selected_restaurant = select_random_option('restaurant', selected_destination.restaurants)
    selected_entertainment = select_random_option('entertainment', selected_destination.entertainments)
    new_trip = Trip(selected_destination, selected_transportation, selected_restaurant, selected_entertainment)
    return new_trip

def get_user_confirmation():
    user_confirmation = input('Would you like to confirm these trip details? Please enter Y/N: ')
    if user_confirmation.upper() == 'Y':
        return True
    else:
        return False

def confirm_trip_details(trip, destinations, transportations, trip_categories):
    trip_confirmed = False
    while trip_confirmed is False:
        console_display.review_trip_details(trip)
        
        trip_confirmed = get_user_confirmation()
        if trip_confirmed is True:
            break

        console_display.display_reselection_options(trip_categories)
        reselection_option = input('Please enter an option to reselect: ')
        if reselection_option == '1':
            trip.destination = select_random_object_by_name('destination', destinations)
            #Since destination affects restaurants and entertainment, reselect those as well
            trip.restaurant = select_random_option('restaurant', trip.destination.restaurants)
            trip.entertainment = select_random_option('entertainment', trip.destination.entertainments)
        elif reselection_option == '2':
            trip.transportation = select_random_option('transportation', transportations)
        elif reselection_option == '3':
            trip.restaurant = select_random_option('restaurant', trip.destination.restaurants)
        elif reselection_option == '4':
            trip.entertainment = select_random_option('entertainment', trip.destination.entertainments)


main()