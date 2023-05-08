pizza_names = ['Margarita', 'Quattro Formadji', 'Peperoni']
friend_pizza = pizza_names[:]

pizza_names.append('Chicken')
friend_pizza.append('Vegan')

print(f'My favorite pizza are: ')
for pizza in pizza_names:
    print(pizza)

print(f'My friend favorite pizza are: ')
for pizza in friend_pizza:
    print(pizza)