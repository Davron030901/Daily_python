def days_to_units(num_of_days,conversion_unit):
    if conversion_unit=='hours':
        return f'{num_of_days} days are {num_of_days*24} {conversion_unit}'
    elif conversion_unit=='minutes':
        return f'{num_of_days} days are {num_of_days*24*60} {conversion_unit}'
    else:
        return f"Unsupported unit"

def validate_and_execute(dict_and_unit_dictionary):
    try:
        user_input_number=int(dict_and_unit_dictionary['days'])
        if user_input_number>0:
            calculated_value=days_to_units(user_input_number,dict_and_unit['units'])
            print(calculated_value)
        elif user_input_number==0:
            print('you entered a 0, please enter a valid positive number')
        else:
            print('User not negative number!')
    except ValueError:
        print('your input is not a valid number. Don\'t ruin my program!')
user_input_message='Hey user, enter a number of as a comma separeted list and I will convert it to hours!\n'
