rivers_and_countries = {
    'nile': 'egypt',
    'iskar': 'bulgaria',
    'tevere': 'italy'
}

for river, country in rivers_and_countries.items():
    print(f'The {river.title()} runs through {country.title()}')

for river in rivers_and_countries.keys():
    print(river.title())

for country in rivers_and_countries.values():
    print(country.title())