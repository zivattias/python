text = "The sun is shining and the life is beautiful!"

print(text.upper())
print(text.lower())
new_text = text.lower()
print(type(new_text))

# String method - Receive the 3rd word in the string:
ret_val = text.split(" ")
print(ret_val)
print(type(ret_val))
print(ret_val[2])
print(ret_val[::-1])

# lists
my_list = []  # <-- this is an empty list
my_list = ['Hello', 'World']
grades = [90, 95, 97, 85]
print(grades[2])  # will output the 3rd value (0, 1, 2 [...])
various_list = [9, 'Hello', 0.54, True,
                ['aaa', 'hi', 0.98,
                 ['ziv', 1998, 'attias']]]
print(type(various_list[3]))  # bool type
print(type(various_list[2]))  # float type
print(type(various_list[-1]))  # list type (first in reverse)
temp = various_list[4]
print(temp[0])  # nested list, usage of variable in-between 'temp'
print(various_list[-1][-1][2])  # nested list, usage of more '[]'

print(len(various_list))  # will return how many values are in the variable various_list
print(len(text))  # will return how many CHARACTERS including " " are in the text
print(text[3] == ' ')  # will return whether index 3 in text is space ' '
print(len(""))  # will return the length of the provided string
print(len([]))  # will return zero since list has no values
print(type(len([])))
print(type(len))

# operator 'in' - boolean operator: True/False
print(50 in grades)  # is 50 in list 'grades'? False
print(97 in grades)  # is 97 in list 'grades'? True
print("sun" in text)  # as same as before
print("sun" in text.lower())  # safety precaution: transforms text to lowercase

# Can use .lower() in inputs & 'if' statements when input is string. Best practice!

# More string method:
# 1. find - 'find' returns the index number of first match
print(text)
ret_val = text.find("sun")  # 'find' returns the index number of first find matching to "sun"
ret_val = text.find(" ", 10)  # start searching from index 10
# look for a space starting from the word 'shining'
shining_idx = text.find("shining")
ret_val = text.find(" ", shining_idx)
ret_val = text.find("blahblah")  # will return index '-1' that means 'not found'
print(ret_val)

# 2. index - returns starting point index
ret_val = text.index(" ")  # will return starting index
ret_val = text.index("shining")  # same

# 3. count - counts input appearance times in
ret_val = text.count(" ")
print(ret_val)

# 4. strip - removes spaces from beginning and end
ret_val = "     sun     ".strip()
print(ret_val)

# combination of all
ret_val = "    SUN    ".strip().lower().index("s")

# 5. endswith - does a string end with your input?
ret_val = text.endswith("!")
print(ret_val)

# 6. join
words_list = text.split(" ")  # split words_list to a list of values
print(words_list)  # print list
ret_val = "$".join(words_list)  # add $ between each item in list
print(ret_val)  # print new str

hours = 9
minutes = 20
seconds = 9
watch = ":".join([str(hours), str(minutes), str(seconds)])
print(watch)

# 7. replace
ret_val = text.replace(" ", "!")
print(ret_val)


