import re


def is_eligible(record: str):
    late = re.search("L{3,}", record.upper())
    absent = record.upper().count('A')
    if late or absent > 2:
        return False
    return True


if __name__ == '__main__':
    records = [
        "PPALLP", "PPALLL", "PPPPPP",
        "LLLAAA", "AAAAAA", "llaplll"
    ]
    for record in records:
        print(is_eligible(record))
