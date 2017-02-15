persons = {
    'first_name': 'Janeene',
    'last_name': 'Negro',
    'age': 25,
    'city': 'Mandaue',
}

print(persons)

for person in persons.keys():
    print(person)

for keys, value in persons.items():
    print(keys, ":" , value)