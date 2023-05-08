def elements_sandwich(*args):
    """Print sandwich with elements"""
    print('Sandwich with: ')
    for element in args:
        print(f'- {element.title()}')


elements_sandwich('tomato', 'cucumber', 'egg')
elements_sandwich('ketchup', 'meat')
elements_sandwich('white cheese', 'becon', 'egg', 'chicken meat')