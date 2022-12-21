import re

# user_email = input('Enter email: ')
#
# pattern = "[a-z]+@[a-z]+\.[a-z]+"
#
# result = re.match(pattern, user_email)
#
# print(result)
# print(type(result))

# re.search - returns first matching string
# re.findall - returns all matching strings in a list

print(re.match('c', 'cat'))
print(re.match('cat', 'cat'))
print(re.match('cat', 'ccat'))
print(re.match('c.', 'cat'))
print(re.match('c.', 'c$t'))
print(re.match('c[a-c]', 'cat'))
print(re.match('c[a-c][A-Z]', 'caT'))
print(re.match('[A-Z][a-z]', 'CaT'))
print(re.match('[A-Za-z]', 'CaT'))
print('\n')
# quantity: * + ? {}
print(re.match('[A-Z][a-z]*', 'Cat'))   # * = 0 or more characters matching the expression [a-z]
print(re.match('[A-Z][a-z]*', 'Ca'))
print(re.match('[A-Z][a-z]*', 'C'))
print('\n')
print(re.match('[A-Z][a-z]+', 'Cat'))   # + = 1 or more characters matching the expression [a-z]
print(re.match('[A-Z][a-z]+', 'Ca'))
print(re.match('[A-Z][a-z]+', 'C'))     # None
print('\n')
# pairs of letter & digit:
# a7b8c1 - valid
# aa - invalid
# a77 - only 'a7' is valid
print(re.match('([a-c][0-9])+', 'Cat'))
print(re.match('([a-c][0-9])+', 'aa'))
print(re.match('([a-c][0-9])+', 'a77'))
print(re.match('([a-c][0-9])+', 'a7b8c1'))
print('\n')
print(re.match('([a-c][0-9])?', 'a7b8c1'))
print(re.match('([a-c][0-9])?', 'a'))
# Search:
print(re.search('c', 'search'))
print(re.match(".*[!@#$%^&*()].*", 'p@ssword'))

