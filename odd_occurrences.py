words = input().split()
elements = {}

for word in words:
    word = word.lower()

    if word not in elements.keys():
        elements[word] = 0
    elements[word] += 1

for key, value in elements.items():
    if value % 2 != 0 or value == 1:
        print(key, end=" ")
