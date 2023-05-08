list_names = ['Pesho', 'Gosho', 'Ivan', 'Stefan', 'Dimo', 'Ivailo']
print(list_names)

first_three_items = list_names[0:3]
print(f'First three items in the list are: {first_three_items}')

mid_list = len(list_names) // 2
from_mid_to_end = list_names[mid_list:]
print(f'Three items from the middle of the list are: {from_mid_to_end}')

last_three_items = list_names[2:-1]
print(f'Last three items in the list are: {last_three_items}')