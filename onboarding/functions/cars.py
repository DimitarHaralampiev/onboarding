def car_info(manufacturer, model_name, **info):
    """Make a dictionary with car arguments"""
    car = {
        'manufacturer': manufacturer.title(),
        'model': model_name.title()
    }
    for key, value in info.items():
        car[key] = value.title()
    return car


car_information = car_info('vw', 'audi a4', color='black', engine='diesel')
print(car_information)
