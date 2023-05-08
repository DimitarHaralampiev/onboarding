file_name = 'guest_book.txt'
while True:
    name = input('Please enter your name: ')
    if name == 'stop':
        break
    with open(file_name, 'a') as file_object:
        file_object.writelines(f'{name}\n')

