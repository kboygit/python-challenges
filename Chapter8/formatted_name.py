def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def my_bestfriend_name(first_name, last_name):
    fully_name = first_name + ' ' + last_name
    return fully_name.title()

bestfriend = my_bestfriend_name('Mary', 'Janeene')
print(bestfriend)

def my_bestfriend_name(first_name, middle_name, last_name):
    fully_name = first_name + ' ' + middle_name + ' ' + last_name
    return fully_name.title()

bestfriend = my_bestfriend_name('Mary', 'Janeene' , 'Negro')
print(bestfriend)

