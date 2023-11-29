chars = [char for char in input() if char != ' ']

elements = {}

for character in chars:
    if character not in elements.keys():
        elements[character] = 0
    elements[character] += 1

for key, value in elements.items():
    print(f'{key} -> {value}')
