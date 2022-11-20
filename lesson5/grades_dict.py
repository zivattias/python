grades = {
    'Ziv': [100, 90, 80],
    'Valeria': [89, 70],
    'Yael': [99, 98, 100]
}

for name, grades_list in grades.items():
    print(f'{name}: {sum(grades_list) / len(grades_list)}')

name = input('Enter name: ')
grades_list = grades.get(name, [-1])
print(f'{name}: {sum(grades_list) / len(grades_list)}')

name = input('Enter name: ')
grades_list = grades.get(name, f'> Key "{name}" is missing')
print(grades_list)