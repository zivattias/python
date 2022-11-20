string = input("Enter anything: ")
is_palindrome = string[::1] == string[::-1]
if is_palindrome:
    print("Your string is a palindrome.")
else:
    print("Your string isn't a palindrome.")
