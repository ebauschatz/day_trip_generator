import console_display
from random_selections import select_independent_option, select_dependent_option

def main():
    #Consolidate hard-coded option values
    all_trip_categories = ['Destination', 'Transportation', 'Restaurant', 'Entertainment']
    all_transportations = ['train', 'car', 'bus', 'boat', 'airplane']
    #If adding / removing a destination, be sure the edit the corresponding restaurant and entertainment values
    all_destinations = ['the Wisconsin Dells', 'Chicago', 'New York City', 'Phoenix', 'Salt Lake City']
    all_restaurants = {
        'the Wisconsin Dells': ['Paul Bunyan', 'Dells Pizza Lab', 'Triple Play', 'High Rock Cafe', 'Monk\'s'],
        'Chicago': ['Gino\'s East', 'The Purple Pig', 'Luella\'s Southern Kitchen','Jade Court', 'Kasama'],
        'New York City': ['Famous Amadeus Pizza', 'Olio e Piu', 'Bleeker Street Pizza', 'Boucherie West Village', 'Spot Dessert Bar'],
        'Phoenix': ['Breakfast Club', 'Cornish Pasty Company', 'CiBO', 'The Churchill', 'Monroe\'s Hot Chicken'],
        'Salt Lake City': ['Tamarind', 'The Bayou', 'Sapa Sushi Bar', 'La-Cai Noodle House', 'Guras Spice House']
    }
    all_entertainments = {
        'the Wisconsin Dells': ['go rock climbing', 'go hiking', 'visit a water park', 'go camping', 'go kayaking'],
        'Chicago': ['visit the Aquarium', 'watch the Chicago Marathon', 'visit the Bean', 'visit the Planetarium','visit the Field Museum'],
        'New York City': ['watch a Broadway play', 'visit the Museum of Modern Art','watch the NYC marathon', 'visit Central Park', 'visit Times Square'],
        'Phoenix': ['go for a desert hike','visit the Archeological Park','go for a trail ride', 'visit the Musical Instrument Museum','visit the nature preserve'],
        'Salt Lake City': ['visit the USA Climbing Team gym','go rock climbing', 'go hiking', 'vist the Planetarium', 'vist the Natural History Museum']
    }    

    #Configure initial selections
    trip = configure_initial_trip_details(all_destinations, 
        all_transportations, all_restaurants, all_entertainments)
    
    #Confirm or reconfigure as necessary
    confirm_trip_details(trip, all_destinations, all_transportations, all_restaurants, all_entertainments, all_trip_categories)
    
    #Display confirmation message and trip summary
    console_display.display_confirmed_trip_details(trip)

class Trip:
    def __init__(self, destination, transportation, restaurant, entertainment):
        self.destination = destination
        self.transportation = transportation
        self.restaurant = restaurant
        self.entertainment = entertainment

def configure_initial_trip_details(destinations, transportations, restaurants, entertainments):
    selected_destination = select_independent_option('destination', destinations)
    selected_transportation = select_independent_option('transportation', transportations)
    selected_restaurant = select_dependent_option('restaurant', restaurants, selected_destination)
    selected_entertainment = select_dependent_option('entertainment', entertainments, selected_destination)
    new_trip = Trip(selected_destination, selected_transportation, selected_restaurant, selected_entertainment)
    return new_trip

def get_user_confirmation():
    user_confirmation = input('Would you like to confirm these trip details? Please enter Y/N: ')
    if user_confirmation.upper() == 'Y':
        return True
    else:
        return False

def confirm_trip_details(trip, all_destinations, all_transportations, all_restaurants, all_entertainments, trip_categories):
    trip_confirmed = False
    while trip_confirmed is False:
        console_display.review_trip_details(trip)
        
        trip_confirmed = get_user_confirmation()
        if trip_confirmed is True:
            break

        console_display.display_reselection_options(trip_categories)
        reselection_option = input('Please enter an option to reselect: ')
        if reselection_option == '1':
            trip.destination = select_independent_option('destination', all_destinations)
            #Since destination affects restaurants and entertainment, reselect those as well
            trip.restaurant = select_dependent_option('restaurant', all_restaurants, trip.destination)
            trip.entertainment = select_dependent_option('entertainment', all_entertainments, trip.destination)
        elif reselection_option == '2':
            trip.transportation = select_independent_option('transportation', all_transportations)
        elif reselection_option == '3':
            trip.restaurant = select_dependent_option('restaurant', all_restaurants, trip.destination)
        elif reselection_option == '4':
            trip.entertainment = select_dependent_option('entertainment', all_entertainments, trip.destination)

main()