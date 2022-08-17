import console_display
from random_selections import select_random_option, select_random_object_by_name

def main():
    all_trip_categories = ['Destination', 'Transportation', 'Restaurant', 'Entertainment']
    all_transportations = ['train', 'car', 'bus', 'boat', 'airplane']
    all_destinations = configure_all_destinations()

    #Configure initial selections
    trip = configure_initial_trip_details(all_destinations, all_transportations)
    
    #Confirm or reconfigure as necessary
    confirm_trip_details(trip, all_destinations, all_transportations, all_trip_categories)
    
    #Display confirmation message and trip summary
    console_display.display_confirmed_trip_details(trip)

class Destination:
    def __init__(self, name, restaurants, entertainments):
        self.name = name
        self.restaurants = restaurants
        self.entertainments = entertainments

class Trip:
    def __init__(self, destination, transportation, restaurant, entertainment):
        self.destination = destination
        self.transportation = transportation
        self.restaurant = restaurant
        self.entertainment = entertainment

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

def confirm_trip_details(trip, all_destinations, all_transportations, trip_categories):
    trip_confirmed = False
    while trip_confirmed is False:
        console_display.review_trip_details(trip)
        
        trip_confirmed = get_user_confirmation()
        if trip_confirmed is True:
            break

        console_display.display_reselection_options(trip_categories)
        reselection_option = input('Please enter an option to reselect: ')
        if reselection_option == '1':
            trip.destination = select_random_object_by_name('destination', all_destinations)
            #Since destination affects restaurants and entertainment, reselect those as well
            trip.restaurant = select_random_option('restaurant', trip.destination.restaurants)
            trip.entertainment = select_random_option('entertainment', trip.destination.entertainments)
        elif reselection_option == '2':
            trip.transportation = select_random_option('transportation', all_transportations)
        elif reselection_option == '3':
            trip.restaurant = select_random_option('restaurant', trip.destination.restaurants)
        elif reselection_option == '4':
            trip.entertainment = select_random_option('entertainment', trip.destination.entertainments)

def configure_all_destinations():
    all_destinations = []
    dells_destination = Destination('the Wisconsin Dells',
        ['Paul Bunyan', 'Dells Pizza Lab', 'Triple Play', 'High Rock Cafe', 'Monk\'s'],
        ['go rock climbing', 'go hiking', 'visit a water park', 'go camping', 'go kayaking'])
    all_destinations.append(dells_destination)

    chicago_destination = Destination('Chicago', 
        ['Gino\'s East', 'The Purple Pig', 'Luella\'s Southern Kitchen','Jade Court', 'Kasama'],
        ['visit the Aquarium', 'watch the Chicago Marathon', 'visit the Bean', 'visit the Planetarium','visit the Field Museum'])
    all_destinations.append(chicago_destination)

    nyc_destination = Destination('New York City',
        ['Famous Amadeus Pizza', 'Olio e Piu', 'Bleeker Street Pizza', 'Boucherie West Village', 'Spot Dessert Bar'],
        ['watch a Broadway play', 'visit the Museum of Modern Art','watch the NYC marathon', 'visit Central Park', 'visit Times Square'])
    all_destinations.append(nyc_destination)

    phoenix_destination = Destination('Phoenix',
        ['Breakfast Club', 'Cornish Pasty Company', 'CiBO', 'The Churchill', 'Monroe\'s Hot Chicken'],
        ['go for a desert hike','visit the Archeological Park','go for a trail ride', 'visit the Musical Instrument Museum','visit the nature preserve'])
    all_destinations.append(phoenix_destination)

    slc_destination = Destination('Salt Lake City',
        ['Tamarind', 'The Bayou', 'Sapa Sushi Bar', 'La-Cai Noodle House', 'Guras Spice House'],
        ['visit the USA Climbing Team gym','go rock climbing', 'go hiking', 'vist the Planetarium', 'vist the Natural History Museum'])
    all_destinations.append(slc_destination)
    return all_destinations


main()