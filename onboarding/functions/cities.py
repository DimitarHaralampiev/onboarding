def describe_city(name, country='Bulgaria'):
    """Return city name and country"""
    return f'{name} is in {country}'


print(describe_city('Sofia'))
print(describe_city('Pleven'))
print(describe_city('London', 'England'))