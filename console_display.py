def capitalize_first_letter(original_string):
    return original_string[0].upper() + original_string[1:]

def review_trip_details(destination, transportation, restaurant, entertainment):
    print()
    print(f'''Your selected trip details are:
    Destination: {capitalize_first_letter(destination)}
    Transportation: {capitalize_first_letter(transportation)}
    Restaurant: {capitalize_first_letter(restaurant)}
    Entertainment: {capitalize_first_letter(entertainment)}''')

def display_reselection_options(all_categories):
    print()
    print('Okay! Any of the below can be reselected:')
    for index, value in enumerate(all_categories):
        print(f'{str(index + 1)} - {value}')

def display_confirmed_trip_details(destination, transportation, restaurant, entertainment):
    print()
    print(f'''Thank you for confirming your trip details!
    Your adventure will take you to {destination} by {transportation}.
    There you will get to {entertainment}!
    Be sure to enjoy a tasty meal at {restaurant} before you leave!''')