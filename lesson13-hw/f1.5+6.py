# Check whether the given string contains at least two TATA-lke patterns
import re

def search_2_tata(seq: str) -> tuple[str, str] | str:
    search = re.search('(.*TATAA[ACGT]{3}TT){2}', seq)
    pattern = re.compile('TATAA[ACGT]{3}TT')

    occurrences = pattern.finditer(seq)
    no_of_occurrences = sum(1 for _ in occurrences)

    if no_of_occurrences >= 2:
        return f"Object: {search}", f"Occurrences #: {no_of_occurrences}"

    return f"Occurrences #: {no_of_occurrences}"

def max_2_tata(seq: str) -> tuple[str, str] | str:
    search = re.search('TATAA[ACGT]{3}TT.*TATAA[ACGT]{3}TT', seq)
    pattern = re.compile('TATAA[ACGT]{3}TT')

    occurrences = pattern.finditer(seq)
    no_of_occurrences = sum(1 for _ in occurrences)

    if no_of_occurrences <= 2:
        return f"Object: {search}", f"Occurrences #: {no_of_occurrences}"

    return f"Occurrences #: {no_of_occurrences}"


if __name__ == '__main__':
    seq_1 = "ZZZTATAAGGGTT_TATAACCCTT_TATAATTTTTZZZ"
    seq_2 = "TATAAGGGTTZZZTATAACCCTT"
    print('At least 2 TATAA:')
    print(f'Seq 1: {search_2_tata(seq_1)}')
    print(f'Seq 2: {search_2_tata(seq_2)}')
    print('\n')
    print('Max 2 TATAA occurrences:')
    print(f'Seq 1: {max_2_tata(seq_1)}')
    print(f'Seq 2: {max_2_tata(seq_2)}')






# def has_two_patterns(string):
#     # Compile the regular expression pattern
#     pattern = re.compile(r'TATAA[ACGT]{3}TT')
#
#     # Use the `finditer` function to find all occurrences of the pattern in the string
#     matches = pattern.finditer(string)
#
#     # Count the number of matches and return True if there are at least two, False otherwise
#     return sum(1 for _ in matches) >= 2
#
#
# # Test the function
# print(has_two_patterns('TATAAGTTTACGTAGTTT'))  # True
# print(has_two_patterns('TATAAGTTT'))  # False