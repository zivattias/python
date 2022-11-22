# Write a program that can execute 2 actions (according to user choice): insert and search.
# Insert asks the user to insert a word and stores it.
# Search asks for a letter and a number. From all the words that have been stored
# it displays only words in which the provided letter appeared exactly number times.
# Divide the program into functions.

# Insert: 'bus', 'bar', 'barbeque', 'door', 'bell'
# Search: B, 1
# OUTPUT: 'bus', 'bar', 'bell'

# Insert: 'bus', 'bar', 'barbeque', 'door', 'bell'
# Search: D, 1
# OUTPUT: 'door'
i_list: list = []

def greetings():
    return print('Welcome! In this program you can do two things: Insert & Search.\n'
                 'If you choose to Insert - you will be prompted to insert words to your kind.\n'
                 'When you finish, you will be brought back to the main menu.\n'
                 'If you choose to Search - you will be prompted to enter a letter and a number.\n'
                 'The program will then start searching for words that include your letter number times,'
                 ' and print them.')

def main_menu():
    print('>> MAIN MENU:\n'
          '> "INSERT" or "SEARCH"')
    while True:
        choice: str = input('Enter your choice (case-insensitive): ').upper()
        if choice == 'INSERT':
            return insert_words()
        elif choice == 'SEARCH':
            return search_words()
        else:
            print('Wrong input. Please type either INSERT or SEARCH.')


def insert_words():
    print('>> INSERT:')
    while True:
        s = input("Please insert a word to store, '$' to return to the menu: ").lower()
        if s == '$':
            return main_menu()
        elif not s.isalpha():
            print('Wrong input. Please use alphabetical words.')
        else:
            i_list.append(s)


def search_words():
    # i_list - insert list
    # s_list - search list
    s_list: list = []
    print('>> SEARCH:')
    while True:
        query_letter = input('Enter a letter and a times number to search (ex: B): ').lower()
        query_number = input('Enter a times number to search (ex: 3): ')
        if not (query_letter.isalpha() or query_number.isdigit()):
            print('Use alphabetical characters for letter and digits for number, please.')
        else:
            break
    for item in i_list:
        if str(item).count(str(query_letter)) == int(query_number):
            s_list.append(item)
    print(f'> YOUR QUERY ({query_letter.upper()}, {query_number}): {s_list}')
    main_menu()


greetings()
main_menu()