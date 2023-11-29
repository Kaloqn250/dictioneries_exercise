all_info = []

check_course = input()

while ':' in check_course:
    name, ID, course = check_course.split(':')
    ID = int(ID)
    all_info.append({'name': name, 'ID': ID, 'course': course})

    check_course = input()

for element in all_info:
    if check_course.startswith(element['course'][0:3]):
        print(f"{element['name']} - {element['ID']}")
