# Implement a function insert_persons that receives int
# number n as argument, and asks the user to insert
# details of n persons. The details for each person include:
# id, first_name, last_name, year, phone.
# The function returns a dictionary with all the
# persons details

import pprint

# one way
# def insert_persons(num: int) -> dict:
#     people: dict = {}
#     for i in range(num):
#         person: dict = {}
#         person['id']: str = input('Enter ID number: ')
#         person['first_name']: str = input('Enter first name: ')
#         person['last_name']: str = input('Enter last name: ')
#         person['year']: str = input('Enter year of birth: ')
#         person['phone']: str = input('Enter phone number: ')
#         people[person['id']] = person
#     return people
# pprint.pprint(insert_persons(int(input('Enter number of people: '))))

# second way
def insert_persons(num: int) -> dict:
    people: dict = {}
    fields = ('id', 'first_name', 'phone')
    for i in range(num):
        person: dict = {}
        for field in fields:
            person[field]: str = input(f'Enter {field}: ')
            people[person['id']] = person
    return people

pprint.pprint(insert_persons(int(input('Enter number of people: '))))

