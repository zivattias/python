names = []
grades = []
typer = None
while typer != '$$$':
    name = input("Enter a student's name: ")
    if name == '$$$':
        break
    else:
        grade = int(input(f"Enter {name}'s grade: "))
        names.append(name)
        grades.append(grade)
print(names)
print(len(names))
print(f"Avg: {sum(grades) / len(grades)}")
