calculation_to_units=24
name_of_unit='hours'

def days_to_units(num_of_days):
    return f'{num_of_days} days are {num_of_days*calculation_to_units} {name_of_unit}'

def validate_and_execute():
    try:
        user_input_number=int(num_of_days_element)
        if user_input_number>0:
            calculated_value=days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number==0:
            print('you entered a 0, please enter a valid positive number')
        else:
            print('User not negative number!')
    except ValueError:
        print('your input is not a valid number. Don\'t ruin my program!')
user_input =''
while user_input !='exit':

    user_input=input('Hey user, enter a number of as a comma separeted list and I will convert it to hours!\n')
    list_of_days=set(user_input)
    print(type(user_input.split(", ")))
    print(user_input.split(", "))
    print(set(user_input.split(", ")))
    print(type(list_of_days))
    for num_of_days_element in set(user_input.split(", ")):
        validate_and_execute()