def car_profile(manufacturer, model_name, **car_info):
    """X"""
    profile = {}
    profile['Manufacturer'] = manufacturer
    profile['Model Name'] = model_name
    for key, value in car_info.items():
        profile[key] = value
    return profile

car = car_profile('subaru', 'outback',
                  color = 'blue', tow_package = True)

print(car)