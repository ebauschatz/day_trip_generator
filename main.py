from random_selectors.destination import select_destination
from random_selectors.transportation import select_transportation

def main():
    trip_confirmed = False
    while trip_confirmed is False:
        selected_destination = select_destination()
        selected_transportation = select_transportation()
        selected_restaurant = '' #add restaurant selection function
        selected_entertainment = '' #add entertainment selection function
        trip_review_message = create_trip_review_message(selected_destination, selected_transportation, selected_restaurant, selected_entertainment)

        print(trip_review_message)
        user_confirmation = input('Would you like to confirm these trip details? Please enter Y/N: ')
        if user_confirmation.upper() == 'Y':
            trip_confirmed = True

def create_trip_review_message(destination, transportation, restaurant, entertainment):
    return f'''Your selected trip details are:
    Destination: {destination}
    Transportation: {transportation}
    Restaurant: {restaurant}
    Entertainment: {entertainment}'''

main()