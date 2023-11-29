elements = input().split()

bakery = {}

for i in range(0, len(elements), + 2):
    product = elements[i]
    quantity = elements[i + 1]
    quantity = int(quantity)

    bakery[product] = quantity

print(bakery)
