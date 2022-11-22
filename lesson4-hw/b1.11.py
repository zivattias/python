# Write a Python function to check whether a number falls in a given range.
# (The function receives number and range (from/to) as parameters and returns True/False)

# 4, 2-6 (num, from-to)
# [4] ", " [2-6]
#          [2] "-" [6]

s1 = '4, 7-9'

def is_in_range(s: str) -> bool:
    num = int(s.split(', ')[0])
    range_from = int(s.split(', ')[1].split('-')[0])
    range_to = int(s.split(', ')[1].split('-')[1])
    if num in range(range_from, range_to):
        return True
    else:
        return False

print(is_in_range(s1))