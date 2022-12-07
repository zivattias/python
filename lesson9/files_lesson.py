import string

# File paths:
relative_path = "data/alice_in_wonderland.txt"
absolute_path = "/Users/ziv.attias/PycharmProjects/python-course/lesson9/data/alice_in_wonderland.txt"

# MANUAL OPEN & CLOSE:
file_handler = open(relative_path, 'r')     # Open file ('r' - Read-Only)
print(file_handler)                         # Prints file_handler's type
# Do stuff with file
file_handler.close()                        # Close file - OS has a limited amount of open file paths

# AUTOMATIC OPEN & CLOSE:
# Python knows that 'file_handler' is a special object that has context (Context Manager).
# When the last line beneath 'with' statement is executed, Python will perform file_handler.__exit__():
with open(relative_path, 'r') as file_handler:
    words_count: int = 0
    check_first_space = False
    # content = file_handler.read()   - Read entire file
    # print(content[100: 1_000]) - Print content from index 100 to index 999
    # print(content[::-1])       - Print the entire content in reverse

    # Print from CHAPTER II to CHAPTER III:
    # print(content[content.index("CHAPTER II"): content.index("CHAPTER III")])
    # print(len(content.split()))       # Print amount of words
    # print(content.split()[100: 200])  # Print list of words from index 100 to 199

    # # In case of multiple .read methods, the result will continue from last reader index:
    # content = file_handler.read(50)
    # print(content, end='')
    # content = file_handler.read(50)
    # print(content, end='')
    # # Hard position the reader at index 500 of ALL content in file:
    # file_handler.seek(500)
    # # Read 50 characters after index 500:
    # content = file_handler.read(50)
    # print(content, end='')
    while True:
        c = file_handler.read(1000)
        if not c:
            break
        if check_first_space and c[0] in string.whitespace:
            words_count += 1
        if c[-1] in string.whitespace:
            words_count += len(c.split())
        else:
            words_count += len(c.split()) - 1
            check_first_space = True
    print(words_count)

