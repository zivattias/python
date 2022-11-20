# Receive a string from a user, and print out whether the string
# contains only whitespaces.
string = input("Enter a string: ").lower()
if string.isspace():
    print("Your string contains only whitespaces.")
else:
    print("Your string contains not only whitespaces.")
