favorite_places = {
    'ning': {
        'cebu',
        'mandaue',
        'colon',
    },

    'zing': {
        'ayala',
        'sm',
        'colonade',
    },

    'ting': {
        'gaisano',
        'fooda',
        'robinsons'
    }
}

for name, places in favorite_places.items():
    print("Name: " + name.title())
    print("\tPlaces: " + str(places).title())