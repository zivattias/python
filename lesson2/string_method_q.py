string = input("Enter a sentence: ")

words = string.split(" ")
string_no_spaces = string.replace(" ", "")

vowels = string.count("a")
vowels += string.count("u")
vowels += string.count("e")
vowels += string.count("o")
vowels += string.count("i")

print(f"Your string ({string}) statistics:\n"
      f"Number of words: {len(words)}\n"
      f"Number of characters with spaces: {len(string)}\n"
      f"Number of characters without spaces: {len(string_no_spaces)}\n"
      f"Number of vowels in string: {vowels}")

