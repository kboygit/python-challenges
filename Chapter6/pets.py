pets = {
    "jota" : {
        'kind': 'chihuahua',
        'owner': 'kboy',
    },

    "gringo": {
        'kind': 'german sheperd',
        'owner': 'hana',
    },

    "burgis": {
        'kind': 'greyhoundz',
        'owner': 'neil',
    },
}

for pet_name, pet_info in pets.items():
    print("\nPet Name: " + pet_name.title())
    kind = pet_info['kind']
    owner= pet_info['owner']

    print("\t" + "Kind: " + kind.title())
    print("\t" + "Owner: " + owner.title())