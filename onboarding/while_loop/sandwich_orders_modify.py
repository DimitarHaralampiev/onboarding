sandwich_orders = ['chicken burger', 'becon burger', 'vegan burger']
finished_sandwiches = []

for pastrami in range(3):
    sandwich_orders.append('pastrami')

print('Sandwich pastrami is finished')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
