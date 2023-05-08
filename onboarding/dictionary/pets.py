dog = {
    'roshko': 'Ivan',
    'tara': 'Pesho',
    'sara': 'Gosho'
}
cat = {
    'felix': 'Iva',
    'oskar': 'Stamat',
    'angel': 'Vanko'
}
rabbit = {
    'floppy': 'Sanq',
    'hopper': 'Tako',
    'bun bun': 'Ivaila'
}

pets = [dog, cat, rabbit]

for pet in pets:
    for pet_name, pet_owner in pet.items():
        print(f'{pet_name.title()}: {pet_owner.title()}')