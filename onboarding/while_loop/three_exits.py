active = True

while active:
    topping = input()
    if topping == 'quit':
        active = False
        continue
    print(f'We will add topping {topping} to your pizza')