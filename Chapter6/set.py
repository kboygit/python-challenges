favorite_languages = {
    'jen': 'python',
    'aning': 'c',
    'ning': 'ruby',
    'zed': 'c++',
    'phil': 'java',
    'jon': 'python',
}

print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())
