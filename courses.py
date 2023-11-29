courses = {}

while True:
    command = input()
    if command == 'end':
        break

    course, name = command.split(" : ")
    if course not in courses.keys():
        courses[course] = []
    courses[course].append(name)

for key, value in courses.items():
    print(f'{key}: {len(value)}')
    for names in value:
        print(f'-- {names}')

