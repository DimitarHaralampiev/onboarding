favorite_numbers = {
    'pesho': [10, 8, 6],
    'gosho': [18, 11, 34],
    'ivan': [3, 13],
    'stamat': [8, 18, 33],
    'ivailo': [12, 24]
}

for name, numbers in favorite_numbers.items():
    print(f'{name.title()}: {[number for number in numbers]}')