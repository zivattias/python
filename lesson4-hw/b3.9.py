# Write a Python program to execute a string containing Python code.
# Hint: search for exec() function in Python


def exec_s(s: str):
    return exec(s)

code_s = 'print("Hello World")'
exec_s(code_s)