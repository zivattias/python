total_digits = 0
total_words = 0
total_chars = 0

digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

word = None
while word != '$':
    if word is not None:
        # total chars
        total_chars += len(word)
        if word.isalpha():
            total_words += len(word)
        # count digits in input
        i = 0
        while i < len(digits):
            total_digits += word.count(digits[i])
            i += 1
    word = input("Enter a word: ")

print(f"Total words: {total_words}\n"
      f"Total chars: {total_chars}\n"
      f"Total digits: {total_digits}")