# persons = {
#     'first_name': 'Janeene',
#     'last_name': 'Negro',
#     'age': 25,
#     'city': 'Mandaue',
# }
#
# print(persons)
#
# for person in persons.keys():
#     print(person)
#
# for keys, value in persons.items():
#     print(keys, ":" , value)

people = {
    'aneene': {
    'first': 'janeene',
    'last': 'negro',
    'age': 25,
    'location': 'mandaue',
},
    'kboy': {
    'first': 'kirby',
    'last': 'james',
    'age': 18,
    'location': 'losangeles',
},
    'zack': {
    'first': 'zack',
    'last': 'galifaniakis',
    'age': 25,
    'location': 'vegas',
}
}

for nickname, infos in people.items():
    print("\nName: " + nickname.title())
    full_name = infos['first'] + " " + infos['last']
    age = infos['age']
    location = infos['location']

    print("\t" + full_name)
    print("\t" + str(age))
    print("\t" + location)
