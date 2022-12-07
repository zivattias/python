import json

if __name__ == '__main__':
    # Load the list into persons
    with open("my_persons.json", "r") as fh:
        persons = json.load(fh)

    print(f"We already have {len(persons)} people in our database!")

    # Add 3 people
    for i in range(3):
        name = input('name: ')
        year = input('year: ')
        person_id = input('person id: ')
        # Append each person to given persons list by JSON
        persons.append({
            'name': name,
            'year': year,
            'person_id': person_id
        })
    # Overwrite new persons list in JSON file
    with open("my_persons.json", "w") as fh:
        json.dump(persons, fh)