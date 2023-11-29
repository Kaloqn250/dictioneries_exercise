orders = {}
command = input()

while command != 'buy':
    command_parts = command.split()
    name = command_parts[0]
    price = float(command_parts[1])
    quantity = float(command_parts[2])

    if name not in orders.keys():
        orders[name] = [0, 0]
    orders[name][0] = price
    orders[name][1] += quantity

    command = input()

for product, value in orders.items():
    print(f'{product} -> {(value[0] * value[1]):.02f}')
