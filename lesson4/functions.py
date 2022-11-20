def print_greeting():
    print("**********")
    print("*Welcome*")
    print("**********")


def print_greeting_name(name, surname):
    print_greeting()
    print(f"Hello {name} {surname}")


print_greeting_name('Ziv', 'Attias')
