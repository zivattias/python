# Tutorial: birthday dictionary
# Write a program that has 2 modes: insert mode and lookup mode.
# The program asks the user whether he wants to insert a birthday date
# or to look up a birthday. If the user chooses to insert a new date,
# ask for the person's name and then ask for the person's birthday, and store them.
# If the user chooses lookup mode, ask for a name and return the birthday of the person.

birthday_dict: dict = {
    "Ziv Attias": "23/08/1998"
}

def lookup_birthday() -> str:
    name: str = input('Enter a name: ')
    return birthday_dict.get(name)

def insert_birthday() -> str:

