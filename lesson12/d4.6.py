# Use lambda and filter/map/sort. Given a list of strings, filter out those containing less than 2 "a" chars.
# For example, for ["apple", "ananas", "banana", "pear"], your code should return ["ananas", "banana"]

fruits_list = ["apple", "ananas", "banana", "pear"]

def fruit_filter(fruits: list[str]) -> list[str]:
    return list(filter(lambda fruit: fruit.count('a') > 2, fruits))

print(fruit_filter(fruits_list))