import json

from downloading.country_codes import get_country_code

file_name = 'population_data.json'

try:
    with open(file_name) as file_object:
        pop_date = json.load(file_object)
    for pop_dict in pop_date:
        if pop_dict['Year'] == '1960':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                print(f'{code}: {population}')
            else:
                print(f'ERROR - {country_name}')
except FileNotFoundError:
    print(f'File {file_name} does not exist')

