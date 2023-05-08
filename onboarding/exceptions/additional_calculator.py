while True:
    try:
        num_one = input('Please enter num: ')
        if num_one == 'stop':
            break

        num_one = int(num_one)

        num_two = input('Please enter num: ')
        if num_two == 'stop':
            break

        num_two = int(num_two)
    except ValueError:
        print('Please enter number!')
    else:
        sum = num_one + num_two
        print(f'The sum is {sum}')
