resources = {'shards': 0, 'fragments': 0, 'motes': 0}
obtained_item = ''
is_obtained = False

while not is_obtained:
    current_items = input().split()
    for index in range(0, len(current_items), 2):
        quantity = int(current_items[index])
        item = current_items[index + 1].lower()
        if item not in resources.keys():
            resources[item] = 0
        resources[item] += quantity

        for key, value in resources.items():
            if key == 'shards' or key == 'fragments' or key == 'motes':
                if value >= 250:
                    obtained_item = key
                    resources[key] -= 250
                    is_obtained = True
                    break
        if is_obtained:
            if obtained_item == 'fragments':
                obtained_item = "Valanyr"
            elif obtained_item == 'shards':
                obtained_item = "Shadowmourne"
            elif obtained_item == 'motes':
                obtained_item = "Dragonwrath"
            break
    if is_obtained:
        break

print(f'{obtained_item} obtained!')
for item, quantity in resources.items():
    print(f'{item}: {quantity}')

