import json


def remembered_favorite_number():
    file_name = 'new_favorite_number.json'
    try:
        with open(file_name) as file_object:
            content = json.load(file_object)
    except FileNotFoundError:
        with open(file_name, 'w') as file_object:
            favorite_number = input('What is your favorite number? ')
            json.dump(favorite_number, file_object)
            print(f'File name: {file_name}\nFavorite number: {content}')
    print(f'File name: {file_name}\nFavorite number: {content}')


remembered_favorite_number()