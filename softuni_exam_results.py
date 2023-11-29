students_score = {}
language_submissions = {}

command = input()

while command != 'exam finished':
    command_parts = command.split('-')
    name = command_parts[0]

    if command_parts[1] == 'banned':
        students_score.__delitem__(name)
        command = input()
        continue

    language = command_parts[1]
    score = int(command_parts[2])

    if name not in students_score.keys():
        students_score[name] = 0
    if students_score[name] < score:
        students_score[name] = score
    if language not in language_submissions.keys():
        language_submissions[language] = 0
    language_submissions[language] += 1

    command = input()


print('Results:')
for student, score in students_score.items():
    print(f'{student} | {score}')

print('Submissions:')
for language, count in language_submissions.items():
    print(f'{language} - {count}')
