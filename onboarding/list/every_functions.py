mix_names = ['English', 'Bulgarian', 'Rila', 'Pirin', 'England', 'Spain', 'Madrid', 'London']
print(f'Not modification \n{sorted(mix_names)}')
print(f'Reverse without modification \n{sorted(mix_names, reverse=True)}')

mix_names.sort()
print(f'Modify \n{mix_names}')

mix_names.sort(reverse=True)
print(f'Reverse modification \n{mix_names}')

pop_element = mix_names.pop()
print(f'Pop element \n{pop_element}')

length_list = len(mix_names)
print(f'Length \n{length_list}')

index_error = mix_names[8]




