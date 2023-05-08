person_one = {
    'first_name': 'Ivan',
    'last_name': 'Ivanov',
    'age': 45,
    'city': 'Sofia'
}
person_two = {
    'first_name': 'Tom',
    'last_name': 'Johnson',
    'age': 30,
    'city': 'California'
}
person_three = {
    'first_name': 'Stamat',
    'last_name': 'Stamatov',
    'age': 32,
    'city': 'Plovdiv'
}


persons = [person_one, person_two, person_three]

for person in persons:
    for key, value in person.items():
        print(f'{key}\n{value}')
