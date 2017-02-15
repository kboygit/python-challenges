favorite_languages = {
    'jen': 'python',
    'aning': 'c',
    'ning': 'ruby',
    'zed': 'c++',
    'phil': 'java',
    'zik': 'none',
    'malik': 'none',
    'han': 'none'
}


pollnames = ['jen', 'zed', 'zik', 'malik', 'han']
for names in favorite_languages.keys():
    print(names.title())
    if names in pollnames:
        print("\nHi " + names.title() +
              ", Thank you for responding to our poll. " +
              favorite_languages[names].title() + "!\n")
    elif names in favorite_languages.keys():
        print(names.title() + ",please take our poll!")