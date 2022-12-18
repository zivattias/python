# Map:

my_list = ['Apple is nice', 'baNana is yellow', 'ANANAS is Big']

strings = map(str.split, map(str.lower, my_list))

for string in strings:
    print(string)

print(list(strings))  # will print an empty list due to lack of iterations on strings


def foo_sum(*args):
    return sum(args)


my_tuple1, my_tuple2 = (1, 2, 3, 4), (10, 20, 30, 40)

ret_val = map(foo_sum, my_tuple1, my_tuple2, [100, 200, 300, 400])
print(list(ret_val))

ret_val = map(lambda x: x[-1],
              map(lambda x: x.split(' '),
                  map(str.lower, my_list)))

print(list(ret_val))


# Filter:

def filter_upper_words(word: str):
    return word.islower()


filter_obj = filter(filter_upper_words, ['hello', 'hi', 'WORLD', 'yes'])
print(list(filter_obj))

filter_obj = filter(str.islower, ['hello', 'hi', 'WORLD', 'yes'])
print(set(filter_obj))

# Sorted:

students = [
    {'name': 'Moshe', 'grade': 89},
    {'name': 'David', 'grade': 93},
    {'name': 'Jack', 'grade': 73},
]

# def my_key_func(student):
#     return student['grade']

print(sorted(students, key=lambda s: s['grade']))
print(sorted(students, key=lambda s: s['grade'], reverse=True))


participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]

# Sort participants by highest grade & lowest age

print(sorted(participant_list,
             key=lambda x: (100 - x[1], x[2])))