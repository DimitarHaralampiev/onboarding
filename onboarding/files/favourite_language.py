file_name = 'favorite_language.txt'

while True:
    language = input('Which is your favorite language ')
    if language == 'stop':
        break
    with open(file_name, 'a') as file_object:
        file_object.writelines(f'{language}\n')