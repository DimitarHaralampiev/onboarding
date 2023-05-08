cities = {
    'sofia': {
        'county': 'bulgaria',
        'population': '1000000',
        'fact': 'capital'
    },
    'london': {
        'country': 'england',
        'population': '10000000',
        'fact': 'capital'
    },
    'madrid': {
        'country': 'spain',
        'population': '10000000',
        'fact': 'capital'
    }
}

for city, info in cities.items():
    print(f'{city.title()}')
    for key, value in info.items():
        print(f'{key.title()}: {value.title()}')
