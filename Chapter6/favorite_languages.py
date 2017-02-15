favorite_languages = {
    'jen': 'python',
    'aning': 'c',
    'ning': 'ruby',
    'zed': 'c++',
    'phil': 'java'
}


friends = ['phil', 'zed']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("\nHi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!\n")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")