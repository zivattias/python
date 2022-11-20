string = input("Enter something: ")
print(slice(string))
if slice(string) == "":
    print("Your input has only spaces")
else:
    print("Your input has other characters than only space")