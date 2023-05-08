list_names = []

list_names.append('Pesho')
list_names.append('Gosho')
list_names.append('Ivan')
print(list_names)

messages = '\n'.join(['Do you want to be together on dinner ' + i for i in list_names])
print(messages)

list_names[0] = 'Stamat'
list_names[2] = 'Dancho'
messages = '\n'.join(['Do you want to be together on dinner ' + i for i in list_names])
print(messages)

list_names.insert(0, 'Stefan')
list_names.insert(2, 'Pencho')
list_names.append('Ivelin')
messages = '\n'.join(['Do you want to be together on dinner ' + i for i in list_names])
print(messages)