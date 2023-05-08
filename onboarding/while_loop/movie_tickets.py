age = ''

while age != 'stop':
    age = input('What is your age? ')
    age = int(age)
    if age < 0:
        print('Incorrect age')
        continue
    if age < 3:
        print('Your ticket is free')
        continue
    if 3 <= age < 12:
        print('Price is $10')
        continue
    else:
        print('Price is $15')
