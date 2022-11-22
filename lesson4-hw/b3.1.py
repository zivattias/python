# Sample input : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

s1 = 'green-red-yellow-black-white'

def sorting(s: str) -> str:
    l1: list = s.split('-')
    l1.sort()
    s = "-".join(l1)
    return s

print(sorting(s1))