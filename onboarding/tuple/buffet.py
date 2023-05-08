foods = ('Wish', 'Soup', 'Meat', 'Potato', 'Pasta')

for food in foods:
    print(food)

list_foods = list(foods)
list_foods[0] = 'Salad'
list_foods[-1] = 'Beef'

new_foods = tuple(list_foods)
for food in new_foods:
    print(food)