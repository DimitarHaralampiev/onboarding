import json


def write_favorite_number(number):
    file_name = 'favorite_number.json'
    with open(file_name, 'w') as file_object:
        json.dump(number, file_object)


def check_and_read_file():
    file_name = 'favorite_number.json'
    try:
        with open(file_name) as file_object:
            content = json.load(file_object)
    except FileNotFoundError:
        return None
    return f'{file_name}\nYour favorite number is: {content}'


number = int(input('Please input number: '))
write_favorite_number(number)
print(check_and_read_file())