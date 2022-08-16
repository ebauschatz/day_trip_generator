from random_selectors.destination import select_destination
from random_selectors.transportation import select_transportation
from random_selectors.restaurant import select_restaurant
from random_selectors.entertainment import select_entertainment

def main():
    #Consolidate hard-coded option values
    all_transportations = ['Train', 'Car', 'Bus', 'Boat', 'Airplane']
    #If adding / removing a destination, be sure the edit the corresponding restaurant and entertainment values
    all_destinations = ['Wisconsin Dells', 'Chicago', 'New York City', 'Phoenix', 'Salt Lake City']
    all_restaurants = {
        'Wisconsin Dells': ['Paul Bunyan', 'Dells Pizza Lab', 'Triple Play', 'High Rock Cafe', 'Monk\'s'],
        'Chicago': ['Gino\'s East', 'The Purple Pig', 'Luella\'s Southern Kitchen','Jade Court', 'Kasama'],
        'New York City': ['Famous Amadeus Pizza', 'Olio e Piu', 'Bleeker Street Pizza', 'Boucherie West Village', 'Spot Dessert Bar'],
        'Phoenix': ['Breakfast Club', 'Cornish Pasty Company', 'CiBO', 'The Churchill', 'Monroe\'s Hot Chicken'],
        'Salt Lake City': ['Tamarind', 'The Bayou', 'Sapa Sushi Bar', 'La-Cai Noodle House', 'Guras Spice House']
    }
    all_entertainment = {
        'Wisconsin Dells': ['Go Rock Climbing', 'Go Hiking', 'Visit a Water Park', 'Go Camping', 'Go Kayaking'],
        'Chicago': ['Visit the Aquarium', 'Watch the Chicago Marathon', 'Visit the Bean', 'Visit the Planetarium','Visit the Field Museum'],
        'New York City': ['Watch a Broadway Play', 'Visit the Museum of Modern Art','Watch the NYC marathon', 'Visit Central Park', 'Visit Times Square'],
        'Phoenix': ['Go for a Desert Hike','Visit the Archeological Park','Go for a Trail Ride', 'Visit the Musical Instrument Museum','Visit the Nature Preserve'],
        'Salt Lake City': ['Visit the USA Climbing Team Gym','Go Rock Climbing', 'Go Hiking', 'Vist the Planetarium', 'Vist the Natural History Museum']
    }    

    selected_destination = select_destination(all_destinations)
    selected_transportation = select_transportation(all_transportations)
    selected_restaurant = select_restaurant(selected_destination, all_restaurants)
    selected_entertainment = select_entertainment(selected_destination, all_entertainment)
    
    trip_confirmed = False
    while trip_confirmed is False:
        trip_review_message = create_trip_review_message(selected_destination, selected_transportation, selected_restaurant, selected_entertainment)
        print(trip_review_message)
        user_confirmation = input('Would you like to confirm these trip details? Please enter Y/N: ')
        if user_confirmation.upper() == 'Y':
            trip_confirmed = True
            break
        reselection_message = '''
        1 - Destination
        2 - Transportation
        3 - Restaurant
        4 - Entertainment'''
        print(reselection_message)
        reselection_option = input('Please enter an option to reselect: ')
        if reselection_option == '1':
            selected_destination = select_destination(all_destinations)
            #Since destination affects restaurants and entertainment, reselect those as well
            selected_restaurant = select_restaurant(selected_destination, all_restaurants)
            selected_entertainment = select_entertainment(selected_destination, all_entertainment)
        elif reselection_option == '2':
            selected_transportation = select_transportation(all_transportations)
        elif reselection_option == '3':
            selected_restaurant = select_restaurant(selected_destination, all_restaurants)
        elif reselection_option == '4':
            selected_entertainment = select_entertainment(selected_destination, all_entertainment)

def create_trip_review_message(destination, transportation, restaurant, entertainment):
    return f'''Your selected trip details are:
    Destination: {destination}
    Transportation: {transportation}
    Restaurant: {restaurant}
    Entertainment: {entertainment}'''

main()