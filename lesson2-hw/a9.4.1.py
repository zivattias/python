string = input("Enter something: ")

if string.endswith("a") or \
        string.endswith("u") or \
        string.endswith("i") or \
        string.endswith("e") or \
        string.endswith("o") or \
        string.endswith("u"):
    print("Your string ends with a vowel.")
else:
    print("Your string doesn't end with a vowel.")