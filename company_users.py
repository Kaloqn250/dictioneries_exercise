companies = {}

command = input()

while command != 'End':
    company, employee_id = command.split(' -> ')
    if company not in companies.keys():
        companies[company] = []
    if employee_id not in companies[company]:
        companies[company].append(employee_id)
    command = input()

for key, value in companies.items():
    print(f'{key}')
    for employee in value:
        print(f'-- {employee}')


