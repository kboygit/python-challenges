                # Setting Default Value for an argument
                # Cannot left an argument last without a default value
def describe_pet(pet_name , animal_type = 'dog'):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'jota')
# The keyword arguments can be interchangeably
describe_pet(animal_type='cat',pet_name='ming2')
# Calling the function can omit the argument with a default value's information
describe_pet(pet_name='willie')
