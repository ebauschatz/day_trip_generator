def confirm_selection(selection, selection_type):
    print(f'The currently suggested {selection_type} is {selection}.')
    user_confirmation = input('Would you like to confirm this {selection_type}? Please enter Y/N: ')
    if user_confirmation.upper() == 'Y':
        return True
    else:
        return False