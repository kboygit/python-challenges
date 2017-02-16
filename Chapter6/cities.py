cities = {
    'cebu': {
        'country': 'Philippines',
        'region': 'Region VII',
        'language': 'bisaya',
        'population': 'two million',
        'fact': 'sinulog festival',
    },
    'baguio': {
        'country': 'Philippines',
        'region': 'Region I',
        'language': 'tagalog',
        'population': 'three million',
        'fact': 'summer capital',
    },
    'boracay': {
        'country': 'Philippines',
        'region': 'Region IV',
        'language': 'universal',
        'population': 'four million',
        'fact': 'best beach in the world',
    },
}

for city, city_info in cities.items():
    print("City Name: " + city.title())
    country = city_info['country']
    region = city_info['region']
    language = city_info['language']
    population = city_info['population']
    fact = city_info['fact']

    print("\tCountry: " + country.title())
    print("\tRegion: " + region.title().upper())
    print("\tLanguage: " + language.title())
    print("\tPopulation Estimate: " + population.title())
    print("\tFact: " + fact.title())