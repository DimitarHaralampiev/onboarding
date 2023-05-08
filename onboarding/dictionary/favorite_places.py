favorite_places = {
    'ivan': ['mountain', 'village'],
    'pesho': ['bar', 'restaurant'],
    'stamat': ['bolling', 'shooting']
}

for name, places in favorite_places.items():
    print(f'{name.title()}:')
    for place in places:
        print(f'\t{place.title()}')