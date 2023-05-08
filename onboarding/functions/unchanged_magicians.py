def show_magicians(names):
    """Print all names"""
    for name in names:
        print(name)


def make_great(names):
    """Print all names with greetings"""
    for name in names:
        print(f'Great {name.title()}')


list_names = ['Pesho', 'Gosho', 'Ivan']
new_list_names = list_names[:]

show_magicians(list_names)
make_great(new_list_names)