count_of_words = int(input())
elements = {}

for _ in range(count_of_words):
    word = input()
    synonym = input()

    if word not in elements.keys():
        elements[word] = []
    elements[word].append(synonym)

for key,value in elements.items():
    print(f'{key} - {", ".join(value)}')

