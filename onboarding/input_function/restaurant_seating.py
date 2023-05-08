group_persons = input('How many people are dinner? ')
group_persons = int(group_persons)
if group_persons > 8:
    print('You have to wait for a table')
else:
    print('You table is ready')