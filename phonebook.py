phonebook = {}
command = input()

while "-" in command:
    name, number = command.split('-')

    phonebook[name] = number
    command = input()

count_for_search = int(command)

for _ in range(count_for_search):
    search_name = input()

    if search_name in phonebook.keys():
        print(f'{search_name} -> {phonebook[search_name]}')
    else:
        print(f'Contact {search_name} does not exist.')

