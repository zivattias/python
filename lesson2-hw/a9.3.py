string = input("Enter a string: ")
words = len(string.split(' '))
chars = len(string)
chars_no_space = len(string.replace(' ', ''))

vowels = string.count("a")
vowels += string.count("u")
vowels += string.count("e")
vowels += string.count("o")
vowels += string.count("i")

print(f"Amount of words: {words}\n"
      f"Amount of characters: {chars}\n"
      f"Amount of net characters: {chars_no_space}\n"
      f"Amount of vowels: {vowels}")
