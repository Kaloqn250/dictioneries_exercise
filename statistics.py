command = input()
stats = {}

while command != 'statistics':
    product, quantity = command.split(": ")
    quantity = int(quantity)

    if product in stats:
        stats[product] += quantity
    else:
        stats[product] = quantity
    command = input()

product_count = len(stats.keys())
total_quantity = sum(stats.values())

print('Products in stock:')
for key, value in stats.items():
    print(f'- {key}: {value}')
print(f'Total Products: {product_count}')
print(f'Total Quantity: {total_quantity}')
