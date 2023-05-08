sandwich_orders = ['chicken burger', 'becon burger', 'vegan burger']
finished_sandwiches = []

print('Sandwich pastrami is finished')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich}')
    finished_sandwiches.append(sandwich)

print(f'We made every sandwiches {len(finished_sandwiches)}')
