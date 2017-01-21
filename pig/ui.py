def positive_int_input(question, min_val=0):

    valid_response = None
    while not valid_response:
        try:
            valid_response = int(input(question + ': '))
            if valid_response < min_val:
                valid_response = None
                raise ValueError
            return valid_response
        except ValueError:
            print('That\'s not a valid response. Please enter a positive integer number.')
            print('The number must be greater than {}'.format(min_val))



def get_unique_names(number, type_of_thing):

    names = []
    for n in range(number):

        name = input('Enter the name of {} {}: '.format(type_of_thing, n+1))

        while name in names:
            name = input('There\'s already a {} with that name. Please enter the name of {} {}: '.format(type_of_thing, type_of_thing, n+1))

        names.append(name)

    return names
