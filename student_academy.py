students_count = int(input())
diary = {}

for _ in range(students_count):
    name = input()
    grade = float(input())

    if name not in diary.keys():
        diary[name] =[]
    diary[name].append(grade)

for name, grades in diary.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.5:
        print(f'{name} -> {average_grade:.02f}')

