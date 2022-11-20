goods = [['apple', 'pear', 'peach', 'chery'],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit', 'bayberry',
          'blueberry', 'cloudberry', 'raspberry', 'blackberry']]

longest_word = None
vowels = 0
max_len = 0
vowels_chars = 'aeiouAEIOU'
words_start_vowel = 0

# longest word + its index:
for x, basket in enumerate(goods):
    for y, fruit in enumerate(basket):
        fruit_len = len(fruit)
        if fruit_len > max_len:
            max_len = fruit_len
            longest_word = fruit
            ext_index = x
            int_index = y
for char in longest_word:
    if char in vowels_chars:
        vowels += 1
print(f"Longest: {longest_word}, has {vowels} vowels")

# words start with vowel:
for x, basket in enumerate(goods):
    for y, fruit in enumerate(basket):
        if fruit[0] in vowels_chars:
            words_start_vowel += 1
            print(f'{words_start_vowel}, "{fruit}", index: [{x}][{y}]')

# find all words starting with 'b', store in new list
start_with_b_list = []
for x, basket in enumerate(goods):
    for y, fruit in enumerate(basket):
        if fruit[0] == ('b' or 'B'):
            start_with_b_list.append(fruit)
print(start_with_b_list)

# In which sublist are there the maximum number of vowels? Print its index.
vowels_count = []
vowels_amount_per_list = 0

# # vowel counter function and loops:


def vowel_counter(target):
    counter = 0
    for _ in vowels_chars:
        counter += target.count('a')
        counter += target.count('e')
        counter += target.count('i')
        counter += target.count('o')
        counter += target.count('u')
        return counter


for x, basket in enumerate(goods):
    for y, fruit in enumerate(basket):
        vowels_amount_per_list += vowel_counter(fruit)
    vowels_count.append(vowels_amount_per_list)

for x in range(len(vowels_count)-1):
    if vowels_count[x] > vowels_count[x+1]:
        more_vl_index = x+1
    else:
        more_vl_index = x
    print(vowels_count)
    print(f'List index with more vowels: {more_vl_index}')
