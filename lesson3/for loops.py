grades = [95, 98, 97, 100, 95]

for grade in grades:
    print(f"The grade is: {grade}")

for i, grade in enumerate(grades):  # enumerate returns 2 values: index + value - in given list
    print(f"The grade #{i+1} is {grade}")  # i+1 for immersion (index starts on 0 if not)

text = "Hello World"
for char in text:
    print(char)

# Best practice:
words_list = text.split(" ")
print(len(words_list))
for word in words_list:
    print(word)

# Bad practice: - code duplication + less efficient:
print(len(text.split(" ")))
for word in text.split(" "):
    print(word)
