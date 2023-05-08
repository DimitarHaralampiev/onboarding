file_names = ['cat.txt', 'dog.txt', 'rabbit.txt']

for file in file_names:
    try:
        with open(file) as file_object:
            contents = file_object.read()
            print(f'{contents.title()}\n')
    except FileNotFoundError:
        print(f'File name {file} is not exist')
